#!/usr/bin/env python3
"""Generates ~/dssatva/ports/8002/kit-bag-variations.html - 12 DS SATVA kit
bags drawn as pictures, each shown in the kit block as it would sit on the
site. The lockup follows the owner's reference (finalsatva.jpeg): DS mark,
thin spaced SATVA, Dil Se Pure between two wheat sprigs."""
import os
OUT = os.path.expanduser("~/dssatva/ports/8002/kit-bag-variations.html")

POUCH = [("u-turmeric", "Haldi", "#e8a713"), ("u-chilli-powder", "Mirchi", "#c3341a"),
         ("u-garam-masala", "Garam Masala", "#7d5630"), ("u-himalayan-pink-salt", "Pink Salt", "#d98a8a"),
         ("u-chia-seeds", "Chia", "#68737e")]

def noise(uid, op=".22"):
    return ('<filter id="n%s" x="0" y="0" width="100%%" height="100%%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/>'
            '<feColorMatrix values="0 0 0 0 .3  0 0 0 0 .22  0 0 0 0 .1  0 0 0 %s 0"/></filter>' % (uid, op))

def weave(uid, base, line):
    return ('<pattern id="w%s" width="7" height="7" patternUnits="userSpaceOnUse"><rect width="7" height="7" fill="%s"/>'
            '<path d="M0 2h7M0 5.5h7" stroke="%s" stroke-width="1.6"/><path d="M2 0v7M5.5 0v7" stroke="%s" stroke-opacity=".6" stroke-width="1.2"/></pattern>' % (uid, base, line, line))

def wrinkles(clip):
    # soft vertical folds and a darker foot, clipped to the body
    return ('<g clip-path="url(#%s)"><rect x="0" y="0" width="400" height="460" fill="url(#fold%s)"/>'
            '<rect x="0" y="0" width="400" height="460" fill="url(#foot%s)"/></g>') % (clip, clip[1:], clip[1:])

def fold_defs(uid):
    return ('<linearGradient id="fold%s" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".16"/>'
            '<stop offset=".12" stop-color="#fff" stop-opacity=".10"/><stop offset=".3" stop-color="#000" stop-opacity=".05"/>'
            '<stop offset=".46" stop-color="#fff" stop-opacity=".12"/><stop offset=".62" stop-color="#000" stop-opacity=".07"/>'
            '<stop offset=".8" stop-color="#fff" stop-opacity=".08"/><stop offset="1" stop-color="#000" stop-opacity=".2"/></linearGradient>'
            '<linearGradient id="foot%s" x1="0" y1="0" x2="0" y2="1"><stop offset=".55" stop-color="#000" stop-opacity="0"/>'
            '<stop offset="1" stop-color="#000" stop-opacity=".18"/></linearGradient>') % (uid, uid)

# ------------------------------------------------------------------ bags
# each returns (back_svg, front_svg, logo_box(top%, width%), peek(bool), rim_y%)
def tote(uid, fab, handle, hem, texture="noise", patch=None):
    fill = "url(#w%s)" % uid if texture == "jute" else fab
    defs = noise(uid) + fold_defs("b" + uid) + (weave(uid, fab, hem) if texture == "jute" else "")
    back = ('<svg viewBox="0 0 400 460"><path d="M118 124C118 4 182 4 182 124" fill="none" stroke="%s" stroke-width="17" stroke-linecap="round"/>'
            '<path d="M218 124C218 4 282 4 282 124" fill="none" stroke="%s" stroke-width="17" stroke-linecap="round"/>'
            '<path d="M44 112H356L360 132H40Z" fill="%s" opacity=".55"/><path d="M44 112H356L360 132H40Z" fill="#000" opacity=".28"/></svg>') % (handle, handle, fab)
    body = "M40 124H360L374 444Q200 456 26 444Z"
    p = ""
    if patch:
        p = ('<rect x="112" y="168" width="176" height="196" rx="10" fill="%s"/>'
             '<rect x="120" y="176" width="160" height="180" rx="7" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="6 5"/>') % (patch, hem)
    front = ('<svg viewBox="0 0 400 460"><defs>%s<clipPath id="cb%s"><path d="%s"/></clipPath></defs>'
             '<path d="%s" fill="%s"/>%s'
             '<g clip-path="url(#cb%s)"><rect width="400" height="460" filter="url(#n%s)"/></g>'
             '<rect x="40" y="124" width="320" height="26" fill="%s" opacity=".45" clip-path="url(#cb%s)"/>'
             '<path d="M44 146H356" stroke="%s" stroke-width="1.6" stroke-dasharray="5 4" opacity=".7"/>'
             '%s'
             '<path d="M118 124v26M182 124v26M218 124v26M282 124v26" stroke="%s" stroke-width="17" opacity=".9"/></svg>'
             ) % (defs, uid, body, body, fill, p, uid, uid, hem, uid, hem, wrinkles("cb" + uid), handle)
    return back, front, (patch and 38 or 37, patch and 38 or 50), True, 27

def kraft(uid, paper="#c99a5c", dark="#a87638", rope="#e9dcc3", window=False):
    defs = noise(uid, ".28") + fold_defs("b" + uid)
    back = ('<svg viewBox="0 0 400 460"><path d="M140 134C140 30 200 30 200 70" fill="none" stroke="%s" stroke-width="7" stroke-dasharray="3 2"/>'
            '<path d="M140 134C140 30 200 30 200 70" fill="none" stroke="#8a7a60" stroke-width="7" stroke-dasharray="2 3" stroke-dashoffset="2" opacity=".5"/>'
            '<path d="M200 70C200 30 260 30 260 134" fill="none" stroke="%s" stroke-width="7" stroke-dasharray="3 2"/>'
            '<path d="M58 118H342L346 140H54Z" fill="%s"/><path d="M58 118H342L346 140H54Z" fill="#000" opacity=".35"/></svg>') % (rope, rope, paper)
    body = "M56 132H344L352 444H48Z"
    win = ""
    if window:
        win = ('<rect x="104" y="262" width="192" height="150" rx="16" fill="#f7efe0"/>'
               '<rect x="104" y="262" width="192" height="150" rx="16" fill="none" stroke="%s" stroke-width="3"/>') % dark
    front = ('<svg viewBox="0 0 400 460"><defs>%s<clipPath id="cb%s"><path d="%s"/></clipPath></defs>'
             '<path d="%s" fill="%s"/><path d="M56 132L86 444H48Z" fill="%s" opacity=".55"/><path d="M344 132L314 444H352Z" fill="%s" opacity=".55"/>'
             '<path d="M56 132H344V168H56Z" fill="#fff" opacity=".08"/><path d="M56 168H344" stroke="%s" stroke-width="2" opacity=".6"/>'
             '<g clip-path="url(#cb%s)"><rect width="400" height="460" filter="url(#n%s)"/></g>%s'
             '<circle cx="146" cy="150" r="5" fill="#5a3f1e"/><circle cx="254" cy="150" r="5" fill="#5a3f1e"/>%s</svg>'
             ) % (defs, uid, body, body, paper, dark, dark, dark, uid, uid, wrinkles("cb" + uid), win)
    return back, front, ((32, 36) if window else (40, 46)), True, 28

def potli(uid, cloth="#f3ead7", cord="#b5832a", trim="#c0392b"):
    defs = noise(uid) + fold_defs("b" + uid)
    body = "M200 150C116 150 64 196 64 306C64 420 124 446 200 446C276 446 336 420 336 306C336 196 284 150 200 150Z"
    front = ('<svg viewBox="0 0 400 460"><defs>%s<clipPath id="cb%s"><path d="%s"/></clipPath>'
             '<radialGradient id="pr%s" cx=".4" cy=".35" r=".8"><stop offset="0" stop-color="#fff" stop-opacity=".25"/><stop offset="1" stop-color="#000" stop-opacity=".22"/></radialGradient></defs>'
             '<path d="M150 150C140 112 120 92 126 70C150 84 170 76 184 62C196 80 212 80 226 62C238 78 254 84 276 70C282 92 262 112 252 150Z" fill="%s"/>'
             '<path d="M150 150C140 112 120 92 126 70C150 84 170 76 184 62C196 80 212 80 226 62C238 78 254 84 276 70C282 92 262 112 252 150Z" fill="#000" opacity=".1"/>'
             '<path d="M160 120L170 70M186 124L192 66M214 124L210 66M240 120L232 70" stroke="#000" stroke-opacity=".12" stroke-width="3"/>'
             '<path d="%s" fill="%s"/><path d="%s" fill="url(#pr%s)"/>'
             '<g clip-path="url(#cb%s)"><rect width="400" height="460" filter="url(#n%s)"/></g>'
             '<path d="M66 380Q200 420 334 380" stroke="%s" stroke-width="10" fill="none" opacity=".85"/><path d="M70 396Q200 436 330 396" stroke="%s" stroke-width="3" fill="none" stroke-dasharray="2 6" opacity=".9"/>'
             '<path d="M142 150Q200 168 258 150" stroke="%s" stroke-width="9" fill="none"/>'
             '<path d="M250 152C270 170 268 200 276 236" stroke="%s" stroke-width="6" fill="none"/><path d="M256 154C286 168 296 196 300 226" stroke="%s" stroke-width="6" fill="none"/>'
             '<circle cx="276" cy="244" r="9" fill="%s"/><circle cx="300" cy="234" r="9" fill="%s"/></svg>'
             ) % (defs, uid, body, uid, cloth, body, cloth, body, uid, uid, uid, trim, trim, cord, cord, cord, cord, cord)
    return "", front, (52, 44), False, 0

def jhola(uid, cloth="#efe3cb", strap="#8a5a2b", print_="#a0442e"):
    defs = noise(uid) + fold_defs("b" + uid) + ('<pattern id="bp%s" width="34" height="34" patternUnits="userSpaceOnUse"><rect width="34" height="34" fill="%s"/>'
            '<path d="M17 5c5 4 5 10 0 12-5-2-5-8 0-12ZM17 29c5-4 5-10 0-12-5 2-5 8 0 12ZM5 17c4-5 10-5 12 0-2 5-8 5-12 0ZM29 17c-4 5-10 5-12 0 2-5 8-5 12 0Z" fill="%s"/>'
            '<circle cx="0" cy="0" r="3" fill="%s"/><circle cx="34" cy="34" r="3" fill="%s"/></pattern>') % (uid, cloth, print_, print_, print_)
    back = ('<svg viewBox="0 0 400 460"><path d="M78 160C60 -40 340 -40 322 160" fill="none" stroke="%s" stroke-width="20"/>'
            '<path d="M78 160C60 -40 340 -40 322 160" fill="none" stroke="#000" stroke-opacity=".15" stroke-width="2" stroke-dasharray="4 4"/></svg>') % strap
    body = "M52 154H348V444H52Z"
    front = ('<svg viewBox="0 0 400 460"><defs>%s<clipPath id="cb%s"><path d="%s"/></clipPath></defs>'
             '<path d="%s" fill="%s"/><rect x="52" y="384" width="296" height="60" fill="url(#bp%s)"/><rect x="52" y="378" width="296" height="6" fill="%s"/>'
             '<rect x="52" y="154" width="296" height="10" fill="%s"/>'
             '<g clip-path="url(#cb%s)"><rect width="400" height="460" filter="url(#n%s)"/></g>%s'
             '<rect x="64" y="150" width="28" height="44" rx="4" fill="%s"/><rect x="308" y="150" width="28" height="44" rx="4" fill="%s"/></svg>'
             ) % (defs, uid, body, body, cloth, uid, print_, print_, uid, uid, wrinkles("cb" + uid), strap, strap)
    return back, front, (38, 44), True, 33

def box(uid, paper="#c8955a", side="#a87638", top="#d9ad74", rope="#7a4f22"):
    defs = noise(uid, ".25")
    front = ('<svg viewBox="0 0 400 460"><defs>%s</defs>'
             '<path d="M56 196L106 150H386L336 196Z" fill="%s"/><path d="M336 196L386 150V400L336 446Z" fill="%s"/>'
             '<path d="M56 196H336V446H56Z" fill="%s"/>'
             '<path d="M56 196H336V446H56Z" filter="url(#n%s)"/><path d="M56 196L106 150H386L336 196Z" filter="url(#n%s)" opacity=".7"/>'
             '<path d="M180 172C180 112 262 112 262 172" fill="none" stroke="%s" stroke-width="9" stroke-linecap="round"/>'
             '<ellipse cx="180" cy="174" rx="12" ry="6" fill="#5a3f1e"/><ellipse cx="262" cy="174" rx="12" ry="6" fill="#5a3f1e"/>'
             '<path d="M56 196H336" stroke="%s" stroke-width="3"/><rect x="300" y="196" width="22" height="250" fill="#c0392b" opacity=".9"/><path d="M300 196L350 150H372L322 196Z" fill="#c0392b" opacity=".75"/>'
             '<path d="M106 150L120 196M386 150L336 196" stroke="%s" stroke-width="2" opacity=".5"/></svg>'
             ) % (defs, top, side, paper, uid, uid, rope, side, side)
    return "", front, (60, 40), False, 0

# ------------------------------------------------------------------ lockup
def lockup(tone):
    # tone: "print" (green + gold on light), "cream" (cream + gold on dark)
    mark = "mark-dark.png" if tone == "print" else "mark-cream.png"
    return ('<div class="lk %s"><img class="lk-m" src="assets/%s" alt=""><b class="lk-s">SATVA</b>'
            '<span class="lk-d"><img src="assets/kit-sprig-l.png" alt=""><i>Dil Se Pure</i><img src="assets/kit-sprig-r.png" alt=""></span></div>') % (tone, mark)

def pouches(rim, n=5):
    xs = [22, 36, 50, 64, 78][:n]
    hs = [30, 38, 34, 40, 31][:n]
    out = []
    for k, (img, nm, col) in enumerate(POUCH[:n]):
        out.append('<div class="pch" style="left:%s%%;top:calc(%s%% - %s%%);--c:%s"><span><img src="assets/%s.jpg" alt=""></span><b>%s</b></div>'
                   % (xs[k], rim, hs[k] * .5, col, img, nm))
    return "".join(out)

def tag(text, x, y):
    return ('<div class="htag" style="left:%s%%;top:%s%%"><i></i><b>Healthy Grocery Kit</b><span>%s</span></div>' % (x, y, text))

def window_items():
    imgs = ["u-turmeric", "u-cumin-seeds", "u-chilli-powder", "u-coriander-seeds", "u-garam-masala", "u-methi-seeds"]
    return '<div class="win">%s</div>' % "".join('<span><img src="assets/%s.jpg" alt=""></span>' % i for i in imgs)

def bowls(side_imgs):
    (a, b) = side_imgs
    return ('<div class="bowl" style="left:6%%;bottom:7%%"><img src="assets/%s.jpg" alt=""></div>'
            '<div class="bowl sm" style="right:7%%;bottom:6%%"><img src="assets/%s.jpg" alt=""></div>') % (a, b)

# ------------------------------------------------------------------ the 12
V = [
 dict(n="Natural canvas tote", cap="Your design on plain natural canvas, exactly as in your picture, on a linen table",
      bag=lambda u: tote(u, "#f1e9d8", "#e6dcc6", "#d9cdb2"), tone="print", scene="linen", peek=False, tag=None, bowls=("u-coriander-seeds", "u-turmeric")),
 dict(n="Canvas tote, kit peeking out", cap="The same canvas tote, packed: five of the pouches showing over the top, kit tag on the handle",
      bag=lambda u: tote(u, "#f1e9d8", "#e6dcc6", "#d9cdb2"), tone="print", scene="wood", peek=True, tag=("13 items", 66, 28), bowls=("u-chilli-powder", "u-cumin-seeds")),
 dict(n="Forest green tote", cap="Brand green canvas with the logo in cream and gold - stands out on any shelf",
      bag=lambda u: tote(u, "#2f5238", "#24412c", "#1e3725"), tone="cream", scene="linen", peek=True, tag=("13 items", 66, 28), bowls=("u-garam-masala", "u-mustard-seeds")),
 dict(n="Jute bag, canvas patch", cap="Jute weave with a stitched canvas patch carrying the logo - earthy and sturdy",
      bag=lambda u: tote(u, "#c9a46a", "#a9834c", "#b08a50", texture="jute", patch="#f6efe0"), tone="print", scene="wood", peek=True, tag=None, bowls=("u-methi-seeds", "u-turmeric")),
 dict(n="Kraft paper bag", cap="Brown kraft paper with twisted rope handles, logo printed, the kit showing at the top",
      bag=lambda u: kraft(u), tone="print", scene="sage", peek=True, tag=("13 items", 64, 30), bowls=("u-coriander-seeds", "u-chilli-powder")),
 dict(n="Kraft bag with a window", cap="Kraft paper bag with a cut-out window, so the spices inside are on show",
      bag=lambda u: kraft(u, window=True), tone="print", scene="linen", peek=False, tag=None, window=True, bowls=("u-chia-seeds", "u-turmeric")),
 dict(n="Cotton potli", cap="A drawstring cotton potli with a red border and gold cord - very Indian, very giftable",
      bag=lambda u: potli(u), tone="print", scene="peach", peek=False, tag=("13 items", 72, 30), bowls=("u-garam-masala", "u-coriander-seeds")),
 dict(n="Block-print jhola", cap="A cloth jhola with a long strap and a block-print border along the foot",
      bag=lambda u: jhola(u), tone="print", scene="wood", peek=True, tag=None, bowls=("u-cumin-seeds", "u-chilli-powder")),
 dict(n="Turmeric yellow tote", cap="Warm haldi-yellow canvas with the logo in deep green - bright and cheerful",
      bag=lambda u: tote(u, "#f0c35a", "#d9a73a", "#d6a53e"), tone="print", scene="sage", peek=True, tag=("13 items", 66, 28), bowls=("u-himalayan-pink-salt", "u-methi-seeds")),
 dict(n="Saheli peach tote", cap="Soft Saheli peach canvas, with a \"Packed by Satva Sahelis\" tag on the handle",
      bag=lambda u: tote(u, "#f6dcd0", "#ebc7b6", "#e2b8a5"), tone="print", scene="linen", peek=True, tag=("Packed by Sahelis", 64, 28), bowls=("u-coconut-sugar", "u-turmeric")),
 dict(n="Kraft kit box", cap="A kraft carry-box with a rope handle and a red band - the kit as a gift box",
      bag=lambda u: box(u), tone="print", scene="sage", peek=False, tag=None, bowls=("u-chilli-powder", "u-coriander-seeds")),
 dict(n="Premium green paper bag", cap="Deep green paper bag with the logo in cream and gold, on a dark table - the premium one",
      bag=lambda u: kraft(u, paper="#24412c", dark="#17291c", rope="#d9b45a"), tone="cream", scene="dark", peek=True, tag=("13 items", 64, 30), bowls=("u-garam-masala", "u-turmeric")),
]

COPY = ('<div class="cp"><p class="k">Healthy Grocery Kit &middot; sold only by our Sahelis</p>'
        '<h2>One kit, <em>straight from a Saheli</em></h2>'
        '<p class="d">Our Sahelis don&rsquo;t sell loose packets. Every Saheli brings the same Healthy Grocery Kit to your door &mdash; thirteen pure kitchen essentials, three of them masalas blended at home by the Sahelis themselves.</p>'
        '<a class="bt">Buy the kit</a><span class="tl">or call +91-9689888822</span></div>')

figs = []
for i, v in enumerate(V, 1):
    uid = "v%d" % i
    back, front, (ltop, lw), canpeek, rim = v["bag"](uid)
    peek = pouches(rim) if (v["peek"] and canpeek) else ""
    win = window_items() if v.get("window") else ""
    tg = tag(v["tag"][0], v["tag"][1], v["tag"][2]) if v["tag"] else ""
    lk = lockup(v["tone"]).replace('class="lk ', 'style="top:%s%%;width:%s%%" class="lk ' % (ltop, lw))
    bagdiv = ('<div class="bag"><div class="bl">%s</div>%s<div class="bl fr">%s</div>%s%s%s</div>' % (back, peek, front, win, lk, tg))
    scene = '<div class="scene %s"><div class="table"></div>%s<div class="shadow"></div>%s</div>' % (v["scene"], bowls(v["bowls"]), bagdiv)
    figs.append('<figure><div class="frame" tabindex="0" role="button" aria-label="Option %d, click for full size"><div class="st">%s%s</div></div>'
                '<figcaption><b>%02d</b> <strong>%s</strong> &mdash; %s</figcaption></figure>' % (i, COPY, scene, i, v["n"], v["cap"]))

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
body{background:#22261e;color:#f4efe6;font-family:"Jost",system-ui,sans-serif;padding:0 16px 70px}
header{max-width:1400px;margin:0 auto;padding:36px 0 10px}
header .k0{letter-spacing:.28em;text-transform:uppercase;font-size:.78rem;color:#e9cf98}
header h1{font-family:"Fraunces",serif;font-weight:600;font-size:clamp(1.8rem,3.4vw,2.7rem);margin:8px 0}
header p{color:#c9bfb0;max-width:80ch;line-height:1.6} header a{color:#e9cf98}
.grid{max-width:1400px;margin:30px auto 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,620px),1fr));gap:34px 26px}
figcaption{margin-top:10px;color:#d9cfbf;font-size:.98rem;line-height:1.45}
figcaption b{color:#e9cf98;font-family:"Fraunces",serif;font-size:1.15rem;margin-right:6px}
figcaption strong{color:#f4efe6;font-weight:600}
.frame{position:relative;aspect-ratio:1245/569;overflow:hidden;border-radius:12px;cursor:zoom-in;outline:none}
.frame.full{position:fixed;inset:0;z-index:50;border-radius:0;aspect-ratio:auto;background:rgba(14,12,10,.92);cursor:zoom-out}
.st{position:absolute;left:0;top:0;width:1245px;height:569px;transform-origin:0 0;transform:scale(var(--s,.5));overflow:hidden;
  background:radial-gradient(120% 140% at 85% 20%,#2d5236 0%,#1c3322 55%,#15261a 100%);color:#f4efe6}
.frame.full .st{left:50%;top:50%;transform:translate(-50%,-50%) scale(var(--s))}
/* the block's words, as on the site */
.cp{position:absolute;left:56px;top:50%;transform:translateY(-50%);width:470px}
.cp .k{font:500 12px/1.3 "Jost";letter-spacing:.26em;text-transform:uppercase;color:#e9cf98}
.cp h2{font:600 44px/1.06 "Fraunces",serif;margin:12px 0 14px;color:#f4efe6}.cp h2 em{display:block;color:#e9cf98}
.cp .d{font:300 16px/1.55 "Jost";color:#d8ceb8;max-width:44ch}
.cp .bt{display:inline-block;margin-top:24px;padding:14px 28px;border-radius:999px;background:linear-gradient(160deg,#f7dc96,#e0a51a 42%,#a8760f);color:#1e2c16;font:600 15px/1 "Jost";letter-spacing:.04em}
.cp .tl{margin-left:18px;font:500 15px/1 "Jost";color:#e9cf98}
/* the picture */
.scene{position:absolute;left:600px;top:34px;width:600px;height:501px;border-radius:22px;overflow:hidden;box-shadow:0 34px 60px -30px rgba(0,0,0,.85)}
.scene .table{position:absolute;left:0;right:0;bottom:0;height:30%}
.scene.linen{background:radial-gradient(90% 80% at 30% 20%,#fffaf1,#efe6d6)}
.scene.linen .table{background:#e7dcc8;background-image:repeating-linear-gradient(0deg,rgba(120,100,70,.06) 0 2px,transparent 2px 4px),repeating-linear-gradient(90deg,rgba(120,100,70,.05) 0 2px,transparent 2px 5px);box-shadow:inset 0 10px 18px -12px rgba(80,60,30,.5)}
.scene.wood{background:radial-gradient(90% 80% at 70% 15%,#fbf3e4,#eadbc2)}
.scene.wood .table{background:#a8743d;background-image:repeating-linear-gradient(0deg,rgba(60,30,5,.18) 0 1px,transparent 1px 9px),linear-gradient(180deg,#b9824a,#8f5e2e);box-shadow:inset 0 8px 14px -8px rgba(0,0,0,.4)}
.scene.sage{background:radial-gradient(90% 80% at 30% 20%,#f3f6ec,#dfe7d2)}
.scene.sage .table{background:linear-gradient(180deg,#f1ece0,#e4dccb);box-shadow:inset 0 10px 18px -12px rgba(60,70,40,.4)}
.scene.peach{background:radial-gradient(90% 80% at 30% 20%,#fff6f2,#f6dfd4)}
.scene.peach .table{background:linear-gradient(180deg,#f3e6dc,#e8d4c6);box-shadow:inset 0 10px 18px -12px rgba(120,70,50,.4)}
.scene.dark{background:radial-gradient(90% 80% at 50% 10%,#3a3a34,#1a1b17)}
.scene.dark .table{background:#2a2621;background-image:repeating-linear-gradient(0deg,rgba(255,255,255,.04) 0 1px,transparent 1px 8px);box-shadow:inset 0 8px 14px -8px rgba(0,0,0,.7)}
.shadow{position:absolute;left:50%;bottom:8%;width:330px;height:34px;margin-left:-165px;border-radius:50%;background:radial-gradient(closest-side,rgba(40,25,10,.45),transparent)}
.dark .shadow{background:radial-gradient(closest-side,rgba(0,0,0,.7),transparent)}
.bowl{position:absolute;width:96px;height:96px;border-radius:50%;overflow:hidden;border:6px solid #fffaf2;box-shadow:0 14px 20px -12px rgba(40,25,5,.7);z-index:1}
.bowl.sm{width:74px;height:74px}
.bowl img{width:100%;height:100%;object-fit:cover}
.dark .bowl{border-color:#3d3a33}
/* the bag */
.bag{position:absolute;left:50%;bottom:9%;width:330px;height:380px;margin-left:-165px;container-type:inline-size;z-index:2}
.bl{position:absolute;inset:0}.bl svg{width:100%;height:100%;display:block;overflow:visible}
.bl.fr{z-index:3;filter:drop-shadow(0 16px 16px rgba(40,25,10,.25))}
.pch{position:absolute;z-index:2;width:16%;height:40%;margin-left:-8%;border-radius:10px 10px 4px 4px;background:var(--c);
  box-shadow:inset 0 -6px 0 rgba(0,0,0,.12),0 6px 10px -6px rgba(0,0,0,.5);display:flex;flex-direction:column;align-items:center;padding-top:8%}
.pch span{display:block;width:72%;aspect-ratio:1;border-radius:50%;overflow:hidden;border:2px solid #fffaf0}
.pch img{width:100%;height:100%;object-fit:cover}
.pch b{font:600 3.1cqw/1.05 "Jost";color:#fff;text-align:center;margin-top:5%;text-shadow:0 1px 2px rgba(0,0,0,.4);padding:0 3px}
/* lockup: as in the owner's picture */
.lk{position:absolute;left:50%;transform:translateX(-50%);z-index:4;text-align:center;container-type:inline-size;pointer-events:none}
.lk.print{mix-blend-mode:multiply}
.lk-m{display:block;width:60%;margin:0 auto}
.lk-s{display:block;font:400 22cqw/1 "Jost",sans-serif;letter-spacing:.2em;margin:5cqw 0 0 .2em;color:#4f6e47}
.lk-d{display:flex;align-items:center;justify-content:center;gap:3cqw;margin-top:3cqw}
.lk-d img{height:6.5cqw;width:auto}
.lk-d i{font:400 10cqw/1 "Jost",sans-serif;font-style:normal;color:#4f6e47;letter-spacing:.02em}
.lk.cream .lk-s,.lk.cream .lk-d i{color:#f4ecd8}
/* window in the kraft bag */
.win{position:absolute;z-index:4;left:26%;top:57%;width:48%;height:32.6%;border-radius:4.4cqw;overflow:hidden;display:grid;grid-template-columns:repeat(3,1fr);
  background:#f7efe0;box-shadow:inset 0 0 0 3px rgba(168,118,56,.9),inset 0 8px 14px -6px rgba(0,0,0,.35)}
.win span{display:block;overflow:hidden;border:2px solid rgba(255,250,240,.6)}
.win img{width:100%;height:100%;object-fit:cover;display:block}
.win::after{content:"";position:absolute;inset:0;background:linear-gradient(120deg,rgba(255,255,255,.35),transparent 40%,transparent 70%,rgba(255,255,255,.18))}
/* hang tag */
.htag{position:absolute;z-index:5;width:24%;padding:7% 2% 4%;background:#e6c99a;border-radius:4px 4px 10px 10px;text-align:center;transform:rotate(9deg);
  box-shadow:0 8px 12px -6px rgba(0,0,0,.45);clip-path:polygon(18% 0,82% 0,100% 14%,100% 100%,0 100%,0 14%)}
.htag i{position:absolute;left:50%;top:5%;width:9%;aspect-ratio:1;margin-left:-4.5%;border-radius:50%;background:#7a5418}
.htag b{display:block;font:600 4cqw/1.1 "Fraunces",serif;color:#3a2a14}
.htag span{display:block;font:500 3.2cqw/1.2 "Jost";letter-spacing:.08em;text-transform:uppercase;color:#7a5418;margin-top:3%}
"""
JS = """
function fit(){document.querySelectorAll('.frame').forEach(function(f){var full=f.classList.contains('full');
  f.style.setProperty('--s', full?Math.min(innerWidth/1245,innerHeight/569)*.96:f.clientWidth/1245);});}
addEventListener('resize',fit); fit();
document.querySelectorAll('.frame').forEach(function(f){
  function t(){var on=!f.classList.contains('full'); document.querySelectorAll('.frame.full').forEach(function(x){x.classList.remove('full')}); if(on)f.classList.add('full'); fit();}
  f.addEventListener('click',t); f.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();t();}});
});
addEventListener('keydown',function(e){if(e.key==='Escape'){document.querySelectorAll('.frame.full').forEach(function(x){x.classList.remove('full')});fit();}});
"""
html = """<!DOCTYPE html>
<html lang="en">
<!-- 14 Oct 2026. Owner: "can you give variations in the form of a kit instead
     of just a block here. give me some variations creating a bag with DS Satva
     [their tote picture] this design and create a bag picture atleast 10 and
     i will choose one". Review page only - not linked, noindex. Each option is
     the kit block at the owner's screen size (1245 x 569) with a drawn bag in
     place of the flat kit box. The lockup follows the owner's picture: DS mark
     (assets/mark-*.png), thin spaced SATVA, Dil Se Pure between the wheat
     sprigs (assets/kit-sprig-l/r.png, cut from logo-stack-dark.png).
     Generated by kit-bag-variations.gen.py beside this file. -->
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Kit Bag Options</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>%s</style>
</head>
<body>
<header>
  <p class="k0">DS Satva &middot; kit bag review</p>
  <h1>The Healthy Grocery Kit as a bag &mdash; 12 options</h1>
  <p>Each bag carries your DS SATVA design (DS mark, SATVA, Dil Se Pure with the wheat sprigs) and is shown inside the kit block as it would sit on the site, in place of the flat kit box. Click any option to see it full size (click again or press Esc to come back). Tell me the number you like. <a href="index.html#kit">Back to the site</a></p>
</header>
<div class="grid">
%s
</div>
<script>%s</script>
</body>
</html>
""" % (CSS, "\n".join(figs), JS)
open(OUT, "w").write(html)
print("wrote", OUT, len(html) // 1024, "KB")
