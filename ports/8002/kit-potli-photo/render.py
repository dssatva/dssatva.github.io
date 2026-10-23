#!/usr/bin/env python3
"""Renders a shaded, product-style potli as a transparent PNG.
Height-field shading (body, gathered folds, frilled top), linen weave,
a tube-shaded cord with knot and tassels, and the DS SATVA logo printed
on the cloth (wrapped round the curve). Usage: render(colours, out_path)."""
import numpy as np, os, math
from PIL import Image, ImageDraw, ImageFilter

ASSETS = os.path.expanduser("~/dssatva/ports/8002/assets/")
SS = 2                      # supersample
W, H = 800, 920             # output size
w, h = W * SS, H * SS

def smooth(t):
    t = np.clip(t, 0, 1); return t * t * (3 - 2 * t)

def hexrgb(c):
    c = c.lstrip("#"); return np.array([int(c[i:i + 2], 16) / 255 for i in (0, 2, 4)])

rng = np.random.default_rng(7)
y, x = np.mgrid[0:h, 0:w].astype(np.float32)
u = x / w; v = y / h
dx = u - .5

# ---- silhouette profiles -------------------------------------------------
NECK_V, NECK_R = .30, .082
def r_body(v):
    r = np.zeros_like(v)
    up = (v >= NECK_V) & (v < .63)
    t = (v[up] - NECK_V) / (.63 - NECK_V)
    r[up] = NECK_R + (.415 - NECK_R) * smooth(t) ** .62
    lo = (v >= .63) & (v <= .975)
    t = (v[lo] - .63) / (.975 - .63)
    r[lo] = .415 * np.clip(1 - t ** 2.6, 0, 1) ** .5
    return r
def r_ruff(v):
    t = np.clip((NECK_V - v) / (NECK_V - .13), 0, 1)
    return NECK_R + (.205 - NECK_R) * t ** 1.6

rb = r_body(v)
rr = r_ruff(v)
top_edge = .135 + .010 * np.abs(np.sin(np.pi * u / .046)) ** .6 * -1 + .010 + .003 * np.sin(2 * np.pi * u / .019) - .03 * np.cos(np.clip(dx / .21, -1, 1) * np.pi / 2)
m_body = (np.abs(dx) < rb) & (v >= NECK_V - .004)
m_ruff = (np.abs(dx) < rr) & (v < NECK_V + .004) & (v > top_edge)

# ---- height field --------------------------------------------------------
def cyl(dx, r):
    q = np.clip(dx / np.maximum(r, 1e-4), -1, 1)
    return np.sqrt(1 - q * q) * r, np.arcsin(q)

hb, ang_b = cyl(dx, rb)
gather = .05 * (1 - smooth((v - NECK_V) / .42)) ** 1.5          # folds fade from neck
folds = gather * np.cos(9 * ang_b + .5 * np.sin(v * 24))
wrinkle = .002 * np.sin(u * 37 + np.sin(v * 21) * 2) * np.sin(v * 29)
Hb = hb * 1.15 + folds + wrinkle

hr, ang_r = cyl(dx, rr)
pleat = .02 * np.cos(11 * ang_r + 1.3)
Hr = hr * 1.05 + pleat

Hf = np.where(m_ruff & ~m_body, Hr, Hb)
mask = (m_body | m_ruff).astype(np.float32)

gy, gx = np.gradient(Hf * w * 1.0)
nx, ny, nz = -gx, -gy, np.ones_like(gx)
nl = np.sqrt(nx * nx + ny * ny + nz * nz); nx /= nl; ny /= nl; nz /= nl
L = np.array([-.42, -.58, .70]); L /= np.linalg.norm(L)
diff = np.clip((nx * L[0] + ny * L[1] + nz * L[2] + .5) / 1.5, 0, 1)
Hv = L + np.array([0, 0, 1.0]); Hv /= np.linalg.norm(Hv)
spec = np.clip(nx * Hv[0] + ny * Hv[1] + nz * Hv[2], 0, 1) ** 24
sheen = (1 - nz) ** 2.2 * np.where(m_ruff & ~m_body, .35, 1)

# ambient occlusion: fold troughs, under the frill, the neck pinch, the base
ao = np.ones_like(u)
trough = np.clip(-np.cos(9 * ang_b + .5 * np.sin(v * 24)), 0, 1) * (gather / .05)
ao -= .30 * trough * m_body
ao -= .45 * np.exp(-((v - NECK_V - .012) / .022) ** 2) * m_body
ao -= .28 * np.clip(-np.cos(11 * ang_r + 1.3), 0, 1) * m_ruff
ao -= .16 * smooth((v - .91) / .065) * m_body
ao -= .10 * np.clip((np.abs(dx) / np.maximum(rb, 1e-3) - .82) / .18, 0, 1) * m_body
ao = np.clip(ao, .25, 1)

# linen weave (threads vary per row / column, plus slubs)
rows = rng.normal(0, 1, h).astype(np.float32); cols = rng.normal(0, 1, w).astype(np.float32)
rows = np.convolve(rows, np.ones(3) / 3, "same"); cols = np.convolve(cols, np.ones(3) / 3, "same")
weave = (.014 * rows[:, None] + .014 * cols[None, :]
         + .018 * np.sin(x * 2.6) * np.sin(y * 2.6)
         + .016 * rng.normal(0, 1, (h, w)).astype(np.float32))

# logo, printed round the curve
def logo_layer(dark):
    lg = Image.open(ASSETS + ("logo-stack-dark.png" if dark else "logo-stack-cream.png")).convert("RGBA")
    a = np.asarray(lg).astype(np.float32) / 255
    lw = .33                                        # logo width (fraction of W)
    lh = lw * a.shape[0] / a.shape[1] * (w / h)
    v0 = .505
    arc = rb * ang_b                               # arc length from centre
    su = (arc / lw + .5) * a.shape[1]
    sv = ((v - v0) / lh) * a.shape[0]
    ok = m_body & (su >= 0) & (su < a.shape[1] - 1) & (sv >= 0) & (sv < a.shape[0] - 1)
    out = np.zeros((h, w, 4), np.float32)
    out[ok] = a[sv[ok].astype(int), su[ok].astype(int)]
    return out

def tube(draw, pts, width, base, light=(-.6, -.7), steps=7):
    """fake a shaded cylinder with stacked strokes"""
    b = np.array(base)
    for i in range(steps):
        t = i / (steps - 1)
        col = np.clip(b * (.45 + .9 * t) + .25 * t ** 3, 0, 1)
        off = (light[0] * width * .22 * t, light[1] * width * .22 * t)
        wd = max(1, int(width * (1 - .78 * t)))
        draw.line([(p[0] + off[0], p[1] + off[1]) for p in pts], fill=tuple(int(c * 255) for c in col) + (255,), width=wd, joint="curve")

def bez(p0, p1, p2, p3, n=40):
    return [((1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t * t * p2[0] + t ** 3 * p3[0],
             (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t * t * p2[1] + t ** 3 * p3[1]) for t in np.linspace(0, 1, n)]

def render(cloth, cord, tassel, out, dark_logo=True, logo_mix=.92, weave_amt=1.0):
    alb = np.ones((h, w, 3), np.float32) * hexrgb(cloth)
    alb *= (1 + weave * weave_amt)[..., None]
    lg = logo_layer(dark_logo)
    la = lg[..., 3:4] * logo_mix
    alb = alb * (1 - la) + lg[..., :3] * la
    shade = (.42 + .68 * diff) * ao
    col = alb * shade[..., None] + (.035 * spec + .14 * sheen * diff)[..., None]
    col = np.clip(col, 0, 1) ** (1 / 1.05)
    rgba = np.dstack([col, mask])
    img = Image.fromarray((rgba * 255).astype(np.uint8), "RGBA")

    # cord round the neck, knot, two hanging cords with tassels
    lay = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    cw = int(.024 * w); cb = hexrgb(cord)
    nv = (NECK_V + .006) * h
    front = [( (.5 + (NECK_R + .012) * math.cos(t)) * w, nv + .022 * h * math.sin(t)) for t in np.linspace(math.pi, 0, 60)]
    front = front[::-1]
    tube(d, front, cw, cb)
    # twist marks
    for i, p in enumerate(front[3:-3:3]):
        d.line([(p[0] - cw * .25, p[1] - cw * .3), (p[0] + cw * .25, p[1] + cw * .3)], fill=tuple(int(c * 160) for c in cb) + (150,), width=max(1, cw // 7))
    kx, ky = (.5 + NECK_R + .005) * w, nv + .016 * h
    for k, (ex, ey, c1) in enumerate([(.66, .56, (.66, .40)), (.725, .52, (.76, .36))]):
        pts = bez((kx, ky), (c1[0] * w, c1[1] * h), ((ex - .01) * w, (ey - .08) * h), (ex * w, ey * h))
        tube(d, pts, int(cw * .82), cb)
        tb = hexrgb(tassel)
        tx, ty = ex * w, ey * h
        tw, tl = .03 * w, .095 * h
        for s_ in range(60):                       # strands, flaring out
            f = s_ / 59
            sx = tx - tw / 2 + tw * f
            ex2 = tx + (f - .5) * tw * 2.1
            col = np.clip(tb * (.55 + .65 * f) + .05 * rng.normal(), 0, 1)
            d.line([(sx, ty + .02 * h), (ex2, ty + tl + .01 * h * rng.normal())], fill=tuple(int(c * 255) for c in col) + (255,), width=max(1, int(w * .0018)))
        d.ellipse([tx - tw * .55, ty - .004 * h, tx + tw * .55, ty + .03 * h], fill=tuple(int(c * 255) for c in np.clip(tb * .8, 0, 1)) + (255,))
        for bnd in (.006, .02):
            d.line([(tx - tw * .52, ty + bnd * h), (tx + tw * .52, ty + bnd * h)], fill=tuple(int(c * 255) for c in np.clip(tb * .55, 0, 1)) + (255,), width=max(1, int(w * .003)))
    d.ellipse([kx - cw * .95, ky - cw * .95, kx + cw * .95, ky + cw * .95], fill=tuple(int(c * 255) for c in np.clip(cb * .9, 0, 1)) + (255,))
    d.ellipse([kx - cw * .55, ky - cw * .75, kx + cw * .2, ky - cw * .05], fill=tuple(int(min(1, c * 1.3 + .1) * 255) for c in cb) + (200,))
    shadow = lay.split()[3].filter(ImageFilter.GaussianBlur(w * .006))
    sh = Image.new("RGBA", (w, h), (20, 10, 5, 0)); sh.putalpha(shadow.point(lambda p: int(p * .45)))
    sh = sh.transform(sh.size, Image.AFFINE, (1, 0, -w * .006, 0, 1, -h * .008))
    img.alpha_composite(sh); img.alpha_composite(lay)
    img = img.resize((W, H), Image.LANCZOS)
    img.save(out, optimize=True)
    return out

if __name__ == "__main__":
    render("#dcaea6", "#f6efe2", "#f6efe2", "/tmp/claude-1000/-home-jasmine-fmcg/a8d61cab-8c92-452b-8fa8-3d3820ec5c90/scratchpad/potli-test.png")
    print("ok")
