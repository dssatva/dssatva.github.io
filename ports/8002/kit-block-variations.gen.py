#!/usr/bin/env python3
"""Generates ~/dssatva/ports/8002/kit-block-variations.html - 20 animated
options for the Healthy Grocery Kit block under Satva Saheli."""
import math, os

OUT = os.path.expanduser("~/dssatva/ports/8002/kit-block-variations.html")
W, H = 1245, 569            # one screen under the nav at the owner's window
D = 14                      # seconds per loop

ITEMS = [("u-turmeric","Haldi"),("u-chilli-powder","Mirchi"),("u-mustard-seeds","Mustard"),
 ("u-cumin-seeds","Jeera"),("u-coriander-seeds","Coriander"),("u-garam-masala","Garam Masala"),
 ("u-sambar-masala","Sambar Masala"),("u-chatpat-masala","Chatpat Masala"),
 ("u-himalayan-pink-salt","Pink Salt"),("u-coconut-sugar","Coconut Sugar"),
 ("u-chia-seeds","Chia Seeds"),("u-methi-seeds","Methi"),("j-monk-3-powder","Monk Fruit")]
N = len(ITEMS)

def f(x): return ("%.2f" % x).rstrip("0").rstrip(".")

# ---------------------------------------------------------------- keyframes
def kf_fly(name, i, dx, dy, arc=90, t0=4, step=3.3, mv=7, rot=0, endop=0, ends=.42):
    s = t0 + i*step; m = s + mv*.55; e = s + mv
    mx, my = dx*.6, dy*.6 - arc
    return ("@keyframes %s{0%%,%s%%{transform:translate(0,0) scale(1) rotate(0);opacity:1}"
            "%s%%{transform:translate(%spx,%spx) scale(.85) rotate(%sdeg);opacity:1}"
            "%s%%,100%%{transform:translate(%spx,%spx) scale(%s) rotate(%sdeg);opacity:%s}}"
            % (name, f(s), f(m), f(mx), f(my), f(rot/2), f(e), f(dx), f(dy), ends, rot, endop))

def kf_land(name, i, fx, fy, t0=4, step=3.3, mv=5, s0=1.3, rot=0):
    s = t0 + i*step; e = s + mv
    return ("@keyframes %s{0%%,%s%%{transform:translate(%spx,%spx) scale(%s) rotate(%sdeg);opacity:0}"
            "%s%%{opacity:1}%s%%,100%%{transform:none;opacity:1}}"
            % (name, f(s), f(fx), f(fy), s0, rot, f(s+mv*.3), f(e)))

def kf_pop(name, i, fx=0, fy=0, t0=63, step=1.5, mv=4, s0=.3):
    s = t0 + i*step; e = s + mv
    return ("@keyframes %s{0%%,%s%%{transform:translate(%spx,%spx) scale(%s);opacity:0}"
            "%s%%,100%%{transform:none;opacity:1}}" % (name, f(s), f(fx), f(fy), s0, f(e)))

def kf_belt(name, i, bx, dx, dy, t0=4, step=3.3, mv=11):
    s = t0 + i*step
    return ("@keyframes %s{0%%,%s%%{transform:translate(0,0);opacity:0}%s%%{opacity:1;transform:translate(0,0)}"
            "%s%%{transform:translate(%spx,0) rotate(360deg);opacity:1}"
            "%s%%,100%%{transform:translate(%spx,%spx) scale(.4) rotate(360deg);opacity:0}}"
            % (name, f(s), f(s+1), f(s+mv*.72), f(bx), f(s+mv), f(dx), f(dy)))

def kf_orbit(name, i, vx, vy, t0=4, step=3.3, mv=8):
    # start at C+v, spiral to C: translate values relative to start
    s = t0 + i*step
    pts = []
    for k, (a, r) in enumerate([(55, .7), (115, .38), (170, 0)]):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        px, py = (vx*ca - vy*sa)*r, (vx*sa + vy*ca)*r
        pts.append((px - vx, py - vy))
    return ("@keyframes %s{0%%,%s%%{transform:translate(0,0) scale(1);opacity:1}"
            "%s%%{transform:translate(%spx,%spx) scale(.85)}%s%%{transform:translate(%spx,%spx) scale(.65);opacity:1}"
            "%s%%,100%%{transform:translate(%spx,%spx) scale(.3);opacity:0}}"
            % (name, f(s), f(s+mv*.35), f(pts[0][0]), f(pts[0][1]), f(s+mv*.7), f(pts[1][0]), f(pts[1][1]),
               f(s+mv), f(pts[2][0]), f(pts[2][1])))

def kf_tick(name, i, t0=4, step=3.3, mv=7):
    s = t0 + i*step + mv*.6
    return "@keyframes %s{0%%,%s%%{transform:scale(0)}%s%%,100%%{transform:scale(1)}}" % (name, f(s), f(s+1.2))

def kf_rowdim(name, i, t0=4, step=3.3):
    s = t0 + i*step
    return "@keyframes %s{0%%,%s%%{opacity:1}%s%%,100%%{opacity:.45}}" % (name, f(s), f(s+3))

# ---------------------------------------------------------------- bags
LABELS = {"tote": (63, 10.5, 4.6, "HEALTHY GROCERY KIT", ""), "kraft": (66.5, 8.5, 4, "GROCERY KIT", ""),
          "carton": (66, 10, 4.5, "HEALTHY KIT", ""), "basket": (70, 8.5, 0, "", ""),
          "gold": (85, 10, 3.8, "HEALTHY GROCERY KIT", " gl")}

def bag_svg(kind, uid, front, ink="#2e2210"):
    out = _bag_svg(kind, uid, front)
    if front:
        top, big, small, sub, cls = LABELS[kind]
        out += ('<i class="blab%s" style="top:%s%%;font-size:%scqw"><b>SATVA</b>%s</i>'
                % (cls, top, big, '<small style="font-size:%scqw">%s</small>' % (small, sub) if sub else ''))
    return out

def _bag_svg(kind, uid, front, ink="#2e2210"):
    """kind: tote kraft carton basket gold jar. 200x240 box, mouth ~ y 70."""
    if kind == "tote":
        if not front:
            return ('<svg viewBox="0 0 200 240"><path d="M58 74C58 8 142 8 142 74" fill="none" stroke="#8a6a3a" stroke-width="10" stroke-linecap="round"/>'
                    '<ellipse cx="100" cy="74" rx="88" ry="11" fill="#5e4524"/></svg>')
        return ('<svg viewBox="0 0 200 240"><defs><pattern id="j%s" width="8" height="8" patternUnits="userSpaceOnUse">'
                '<rect width="8" height="8" fill="#c9a46a"/><path d="M0 4h8M4 0v8" stroke="#b08a50" stroke-width="1.4"/></pattern></defs>'
                '<path d="M12 74H188L198 236H2Z" fill="url(#j%s)"/><path d="M12 74H188" stroke="#9a7640" stroke-width="3"/>'
                '<rect x="52" y="116" width="96" height="70" rx="8" fill="#fbf4e4"/>'
                '</svg>') % (uid, uid)
    if kind == "kraft":
        if not front:
            return '<svg viewBox="0 0 200 240"><path d="M24 50H176L180 80H20Z" fill="#8d6434"/></svg>'
        return ('<svg viewBox="0 0 200 240"><path d="M20 66L36 76L52 66L68 76L84 66L100 76L116 66L132 76L148 66L164 76L180 66L172 236H28Z" fill="#c99a5c"/>'
                '<path d="M60 236L66 120M140 236L134 120" stroke="#b5864a" stroke-width="2"/>'
                '<circle cx="100" cy="160" r="40" fill="#f6ead2"/>'
                '</svg>')
    if kind == "carton":
        if not front:
            return ('<svg viewBox="0 0 200 240"><path d="M10 84L30 56H170L190 84Z" fill="#6e4b25"/>'
                    '<path d="M30 56L4 30L22 26L46 56Z M170 56L196 30L178 26L154 56Z" fill="#b8844b"/></svg>')
        return ('<svg viewBox="0 0 200 240"><rect x="10" y="84" width="180" height="150" rx="4" fill="#c8955a"/>'
                '<path d="M10 84H190" stroke="#a87638" stroke-width="3"/><rect x="40" y="128" width="120" height="62" rx="4" fill="none" stroke="#1f3a26" stroke-width="2.4" stroke-dasharray="5 4"/>'
                '</svg>')
    if kind == "basket":
        if not front:
            return ('<svg viewBox="0 0 200 240"><path d="M30 92C30 0 170 0 170 92" fill="none" stroke="#8a5a2b" stroke-width="9"/>'
                    '<ellipse cx="100" cy="94" rx="92" ry="22" fill="#5a3a1a"/></svg>')
        return ('<svg viewBox="0 0 200 240"><defs><pattern id="b%s" width="16" height="12" patternUnits="userSpaceOnUse">'
                '<rect width="16" height="12" fill="#b9874e"/><path d="M0 6Q4 0 8 6T16 6" fill="none" stroke="#8f6232" stroke-width="2"/></pattern></defs>'
                '<path d="M8 94Q100 130 192 94L170 226Q100 246 30 226Z" fill="url(#b%s)"/><path d="M8 94Q100 130 192 94" fill="none" stroke="#7a4f22" stroke-width="7"/>'
                '<rect x="60" y="150" width="80" height="34" rx="6" fill="#fbf4e4"/></svg>') % (uid, uid)
    if kind == "gold":
        if not front:
            return ('<svg viewBox="0 0 200 240"><path d="M62 72C62 14 138 14 138 72" fill="none" stroke="#d9b45a" stroke-width="5"/>'
                    '<path d="M22 60H178L182 84H18Z" fill="#0f1d13"/></svg>')
        return ('<svg viewBox="0 0 200 240"><path d="M18 72H182L190 236H10Z" fill="#1f3a26" stroke="#d9b45a" stroke-width="2.5"/>'
                '<path d="M30 86H170" stroke="#d9b45a" stroke-width="1"/><path d="M100 120l10 16 18 3-13 13 3 18-18-9-18 9 3-18-13-13 18-3Z" fill="none" stroke="#d9b45a" stroke-width="1.6"/>'
                '</svg>')
    raise ValueError(kind)

def bag(kind, uid, x, y, w, extra_cls=""):
    h = w*1.2
    st = 'left:%spx;top:%spx;width:%spx;height:%spx' % (f(x), f(y), f(w), f(h))
    return ('<div class="bag bk %s" style="%s">%s</div>' % (extra_cls, st, bag_svg(kind, uid, False)),
            '<div class="bag bf %s" style="%s">%s</div>' % (extra_cls, st, bag_svg(kind, uid, True)),
            (x + w/2, y + h*0.30))     # mouth (centre of rim)

def it(cls, x, y, s, img, shape="c", label=None, anim=None):
    st = 'left:%spx;top:%spx;--s:%spx' % (f(x), f(y), f(s))
    if anim: st += ';animation-name:%s' % anim
    lab = '<b>%s</b>' % label if label else ''
    return '<div class="it %s %s" style="%s"><span><img src="assets/%s.jpg" alt=""></span>%s</div>' % (shape, cls, st, img, lab)

# ---------------------------------------------------------------- grid helpers
def grid_rows(rows, x0, x1, y0, dy):
    out = []
    for r, n in enumerate(rows):
        for k in range(n):
            out.append((x0 + (x1-x0)*(k+.5)/n, y0 + r*dy))
    return out

AW, AH = 730, 510   # animation area

# ---------------------------------------------------------------- pack scenes
def pack(style, v, bagkind, dark):
    """returns (html, css). coordinates relative to the area."""
    h, css = [], []
    if style == "arc":          # grid of items arcs into a bag at the right
        bk, bf, (mx, my) = bag(bagkind, "p%d" % v, AW-235, AH-275, 215)
        pos = grid_rows([5, 4, 4], 10, 440, 90, 120)
        h.append(bk)
        for i, (x, y) in enumerate(pos):
            n = "v%dp%d" % (v, i); css.append(kf_fly(n, i, mx-x, my-y+20, arc=110, rot=200))
            h.append(it("lab", x, y, 76, ITEMS[i][0], label=ITEMS[i][1], anim=n))
        h.append(bf)
    elif style == "check":      # checklist ticks while each item flies in
        bk, bf, (mx, my) = bag(bagkind, "p%d" % v, AW-245, AH-290, 225)
        h.append(bk)
        rows = []
        for i, (img, name) in enumerate(ITEMS):
            y = 22 + i*36.5
            rn, tn = "v%dr%d" % (v, i), "v%dt%d" % (v, i)
            css.append(kf_rowdim(rn, i)); css.append(kf_tick(tn, i))
            rows.append('<li style="top:%spx;animation-name:%s"><img src="assets/%s.jpg" alt=""><span>%s</span><i style="animation-name:%s">&#10003;</i></li>'
                        % (f(y-14), rn, img, name, tn))
            n = "v%dp%d" % (v, i); css.append(kf_fly(n, i, mx-30, my-y+20, arc=70, rot=120))
            h.append(it("", 30, y, 50, img, anim=n))
        h.insert(0, '<ul class="chk">%s</ul>' % "".join(rows))
        h.append(bf)
    elif style == "belt":       # conveyor into a carton
        bk, bf, (mx, my) = bag("carton", "p%d" % v, AW-230, AH-290, 215)
        by = AH - 120
        h.append('<div class="belt" style="left:0;top:%spx;width:%spx"></div>' % (by, AW-215))
        h.append(bk)
        for i, (img, name) in enumerate(ITEMS):
            x0, y0 = 40, by - 36
            n = "v%dp%d" % (v, i); css.append(kf_belt(n, i, AW-300-x0, mx-x0, my-y0+26))
            h.append(it("", x0, y0, 64, img, anim=n))
        h.append(bf)
        h.append('<div class="lid" style="left:%spx;top:%spx;width:200px"></div>' % (AW-222, AH-250))
    elif style == "rain":       # falls from a top row into a basket
        bk, bf, (mx, my) = bag("basket" if bagkind == "basket" else bagkind, "p%d" % v, AW/2-130, AH-300, 260)
        pos = grid_rows([7, 6], 20, AW-20, 40, 86)
        h.append(bk)
        for i, (x, y) in enumerate(pos):
            n = "v%dp%d" % (v, i); css.append(kf_fly(n, i, mx-x+((i % 3)-1)*30, my-y+30, arc=20, rot=260))
            h.append(it("", x, y, 66, ITEMS[i][0], anim=n))
        h.append(bf)
    elif style == "orbit":      # items orbit then spiral into the bag
        cx, cy = AW/2, AH/2 + 10
        bk, bf, (mx, my) = bag(bagkind, "p%d" % v, cx-100, cy-110, 200)
        h.append('<div class="ring" style="left:%spx;top:%spx;width:640px;height:440px"></div>' % (f(cx-320), f(cy-220)))
        h.append(bk)
        for i, (img, name) in enumerate(ITEMS):
            a = math.radians(-90 + i*360/N)
            x, y = cx + 300*math.cos(a), cy + 205*math.sin(a)
            n = "v%dp%d" % (v, i); css.append(kf_orbit(n, i, x-mx, y-my))
            h.append(it("", x, y, 62, img, anim=n))
        h.append(bf)
    elif style == "slots":      # flat-lay box, items land in slots, lid closes
        bx, by, bw, bh = AW/2-290, 30, 580, 380
        h.append('<div class="flat" style="left:%spx;top:%spx;width:%spx;height:%spx"><p>Healthy Grocery Kit &middot; 13</p></div>' % (bx, by, bw, bh))
        pos = grid_rows([5, 4, 4], bx+20, bx+bw-20, by+90, 110)
        for i, (x, y) in enumerate(pos):
            h.append('<div class="slot" style="left:%spx;top:%spx"></div>' % (f(x-37), f(y-37)))
            n = "v%dp%d" % (v, i); css.append(kf_land(n, i, 0, -140, s0=1.5, rot=-30))
            h.append(it("lab", x, y, 74, ITEMS[i][0], label=ITEMS[i][1], anim=n))
        h.append('<div class="flid" style="left:%spx;top:%spx;width:%spx;height:%spx"><span>SATVA</span><i>Healthy Grocery Kit</i></div>' % (bx, by, bw, bh))
    elif style == "saheli":     # out of the Saheli's photograph into the bag
        h.append('<div class="sarch" style="left:0;top:30px;width:240px;height:450px"><img src="assets/sah-maker.jpg" alt=""><p>Packed by our Sahelis</p></div>')
        bk, bf, (mx, my) = bag(bagkind, "p%d" % v, AW-225, AH-280, 210)
        h.append(bk)
        pos = grid_rows([4, 3, 3, 3], 290, 520, 50, 100)
        for i, (x, y) in enumerate(pos):
            n = "v%dp%d" % (v, i); css.append(kf_fly(n, i, mx-x, my-y+20, arc=80, rot=180))
            h.append(it("", x, y, 62, ITEMS[i][0], anim=n))
        h.append(bf)
    elif style == "jars":       # jars on two shelves slide into a carton
        h.append('<div class="plank" style="left:0;top:210px;width:440px"></div><div class="plank" style="left:0;top:420px;width:440px"></div>')
        bk, bf, (mx, my) = bag("carton" if bagkind != "gold" else "gold", "p%d" % v, AW-235, AH-290, 215)
        h.append(bk)
        pos = [(30 + k*63, 160) for k in range(7)] + [(60 + k*63, 370) for k in range(6)]
        for i, (x, y) in enumerate(pos):
            n = "v%dp%d" % (v, i); css.append(kf_fly(n, i, mx-x, my-y+30, arc=60))
            h.append(it("", x, y, 54, ITEMS[i][0], shape="jar", anim=n))
        h.append(bf)
    elif style == "marquee":    # from both edges into a centre bag
        cx = AW/2
        bk, bf, (mx, my) = bag(bagkind, "p%d" % v, cx-110, AH-300, 220)
        h.append('<div class="track" style="top:150px"></div><div class="track" style="top:250px"></div>')
        h.append(bk)
        for i, (img, name) in enumerate(ITEMS):
            left = i % 2 == 0
            x = -10 - (i//2)*70 + 70*3 if left else AW + 10 + (i//2)*70 - 70*3
            x = max(min(x, AW-20), 20)
            y = 150 if (i//2) % 2 == 0 else 250
            n = "v%dp%d" % (v, i); css.append(kf_fly(n, i, mx-x, my-y+20, arc=40, rot=-200 if left else 200))
            h.append(it("", x, y, 60, img, anim=n))
        h.append(bf)
    elif style == "stack":      # a clear jar-bag fills in layers
        jx, jy, jw, jh = AW-330, 20, 300, 470
        h.append('<div class="glass" style="left:%spx;top:%spx;width:%spx;height:%spx"><p>SATVA &middot; Healthy Grocery Kit</p></div>' % (jx, jy, jw, jh))
        slots = []
        rows = [4, 3, 3, 3]
        for r, n_ in enumerate(rows):
            for k in range(n_):
                slots.append((jx + 22 + (jw-44)*(k+.5)/n_, jy + jh - 60 - r*78))
        src = grid_rows([5, 4, 4], 10, 360, 110, 120)
        for i, ((x, y), (tx, ty)) in enumerate(zip(src, slots)):
            n = "v%dp%d" % (v, i); css.append(kf_fly(n, i, tx-x, ty-y, arc=90, rot=180, endop=1, ends=1))
            h.append(it("", x, y, 68, ITEMS[i][0], anim=n))
    return "".join(h), css

# ---------------------------------------------------------------- serve scenes
DISHES = [("rec-methi-dal", "Methi dal"), ("rec-jeera-bhaat", "Jeera bhaat"), ("rec-haldi-doodh", "Haldi doodh")]

def serve(style, v, bagkind, dark):
    h, css = [], []
    if style == "dishes":
        h.append('<div class="mbag" style="left:20px;top:170px;width:140px">%s%s</div>' % (bag_svg(bagkind, "s%d" % v, False), bag_svg(bagkind, "s%d" % v, True)))
        h.append('<div class="arrow" style="left:175px;top:250px"></div>')
        for i, (img, name) in enumerate(DISHES):
            x = 330 + i*168
            n = "v%ds%d" % (v, i); css.append(kf_pop(n, i, 0, 50, t0=63, step=4, mv=5, s0=.7))
            h.append('<div class="dish" style="left:%spx;top:255px;animation-name:%s"><span><img src="assets/%s.jpg" alt=""></span><b>%s</b><i class="steam"></i></div>' % (x, n, img, name))
        h.append('<p class="scap" style="left:250px;top:430px;width:480px">One kit, a month of dinners</p>')
    elif style == "thali":
        cx, cy = AW/2, AH/2
        h.append('<div class="thali" style="left:%spx;top:%spx"><p>Served<span>from one kit</span></p></div>' % (f(cx-245), f(cy-245)))
        for i, (img, name) in enumerate(ITEMS):
            a = math.radians(-90 + i*360/N)
            x, y = cx + 178*math.cos(a), cy + 178*math.sin(a)
            n = "v%ds%d" % (v, i); css.append(kf_pop(n, i, cx-x, cy-y, t0=62, step=1.4))
            h.append(it("katori", x, y, 64, img, anim=n))
    elif style == "door":
        h.append('<div class="road"></div><div class="door"><i></i></div>')
        h.append('<div class="scoot" style="animation-name:v%dsc"><div class="sbag">%s%s</div>%s</div>' % (v, bag_svg(bagkind, "s%d" % v, False), bag_svg(bagkind, "s%d" % v, True), SCOOTER))
        css.append("@keyframes v%dsc{0%%,60%%{transform:translateX(-200px)}78%%,100%%{transform:translateX(330px)}}" % v)
        css.append("@keyframes v%dok{0%%,79%%{transform:scale(0)}83%%,100%%{transform:scale(1)}}" % v)
        css.append("@keyframes v%dmsg{0%%,82%%{opacity:0;transform:translateY(10px)}86%%,100%%{opacity:1;transform:none}}" % v)
        h.append('<div class="okb" style="animation-name:v%dok">&#10003;</div>' % v)
        h.append('<div class="msg" style="animation-name:v%dmsg"><b>SATVA</b>Your Healthy Grocery Kit is at the door &#128578;</div>' % v)
    elif style == "shelf":
        h.append('<div class="mbag" style="left:10px;top:250px;width:150px">%s%s</div>' % (bag_svg(bagkind, "s%d" % v, False), bag_svg(bagkind, "s%d" % v, True)))
        h.append('<div class="plank" style="left:200px;top:215px;width:520px"></div><div class="plank" style="left:200px;top:420px;width:520px"></div>')
        h.append('<p class="scap" style="left:200px;top:450px;width:520px">Your shelf, stocked for the month</p>')
        pos = [(245 + k*72, 165) for k in range(7)] + [(280 + k*72, 370) for k in range(6)]
        for i, (x, y) in enumerate(pos):
            n = "v%ds%d" % (v, i); css.append(kf_pop(n, i, 85-x, 320-y, t0=62, step=1.4, s0=.2))
            h.append(it("", x, y, 56, ITEMS[i][0], shape="jar", anim=n))
    elif style == "burst":
        cx, cy = AW/2, AH-90
        h.append('<div class="mbag" style="left:%spx;top:%spx;width:170px">%s%s</div>' % (f(cx-85), f(cy-130), bag_svg(bagkind, "s%d" % v, False), bag_svg(bagkind, "s%d" % v, True)))
        for i, (img, name) in enumerate(ITEMS):
            a = math.radians(180 + i*180/(N-1))
            r = 300 if i % 2 == 0 else 215
            x, y = cx + r*math.cos(a)*1.12, cy - 60 + r*math.sin(a)*1.08
            n = "v%ds%d" % (v, i); css.append(kf_pop(n, i, cx-x, cy-60-y, t0=62, step=1.3))
            h.append(it("lab", x, y, 60, img, label=name, anim=n))
    elif style == "dabba":
        cx, cy = 245, AH/2
        h.append('<div class="dabba" style="left:%spx;top:%spx"></div>' % (cx-225, cy-225))
        ring = list(range(7)); centre = 7
        for k, i in enumerate(ring + [centre]):
            if i == centre: x, y = cx, cy
            else:
                a = math.radians(-90 + k*360/7); x, y = cx + 140*math.cos(a), cy + 140*math.sin(a)
            n = "v%ds%d" % (v, i); css.append(kf_pop(n, k, 0, -60, t0=62, step=1.3, s0=.5))
            h.append(it("bowl", x, y, 104, ITEMS[i][0], anim=n))
        h.append('<p class="also" style="left:520px;top:40px">Also in the kit</p>')
        for k, i in enumerate(range(8, 13)):
            y = 110 + k*80
            n = "v%ds%d" % (v, i); css.append(kf_pop(n, 8+k, -40, 0, t0=62, step=1.3, s0=.8))
            h.append(it("row", 545, y, 58, ITEMS[i][0], label=ITEMS[i][1], anim=n))
    return "".join(h), css

SCOOTER = ('<svg class="sc" viewBox="0 0 220 130"><circle cx="40" cy="105" r="22" fill="#26302a"/><circle cx="40" cy="105" r="9" fill="#aaa"/>'
           '<circle cx="180" cy="105" r="22" fill="#26302a"/><circle cx="180" cy="105" r="9" fill="#aaa"/>'
           '<path d="M20 92Q30 60 80 62H150L170 30H190L196 40H178L162 92Z" fill="#c0392b"/><rect x="60" y="56" width="70" height="10" rx="5" fill="#26302a"/></svg>')

# ---------------------------------------------------------------- variations
H2 = ["Everything your kitchen needs, <em>in one bag</em>",
      "Thirteen essentials, <em>one kit</em>",
      "Packed at home, <em>served in yours</em>",
      "Your monthly kitchen, <em>sorted</em>"]
DESC = ("Haldi, mirchi, mustard, jeera and coriander, three masalas blended at home by our Sahelis, "
        "pink salt, coconut sugar, chia, methi and monk fruit &mdash; packed together and delivered to your kitchen.")

#      pack      serve     bag       side  bg-class  h2  caption
V = [
 ("arc",     "dishes", "tote",   "L", "cream", 0, "Each item arcs into a jute bag, then the dinners it makes come up on plates"),
 ("check",   "burst",  "kraft",  "L", "sage",  1, "A checklist ticks off each item as it drops into a kraft bag; the bag then opens out into all thirteen"),
 ("belt",    "door",   "carton", "L", "warm",  3, "Items ride a conveyor into the SATVA carton, the lid shuts, and it is scooted to your door"),
 ("rain",    "thali",  "basket", "R", "brass", 2, "Items fall into a basket, then come out served on a brass thali"),
 ("orbit",   "dishes", "gold",   "L", "dark",  1, "Dark and gold: the thirteen circle the bag and spiral in, then dinner is served"),
 ("slots",   "dabba",  "kraft",  "L", "cream", 0, "A flat-lay kit box fills slot by slot and the lid closes; then the masala dabba fills"),
 ("saheli",  "dishes", "tote",   "L", "blush", 2, "Straight out of a Saheli's hands and into the bag, then onto the table"),
 ("jars",    "thali",  "carton", "R", "sand",  3, "Jars slide off the shelf into the carton, then come out served on a thali"),
 ("marquee", "shelf",  "kraft",  "L", "mint",  0, "Items stream in from both sides into the bag, then stock your kitchen shelf"),
 ("stack",   "dishes", "tote",   "L", "cream", 1, "A clear kit fills up in layers, so you see everything inside, then the dinners"),
 ("arc",     "door",   "kraft",  "R", "warm",  0, "Arc into a kraft bag, then delivered to your door with a WhatsApp ping"),
 ("check",   "thali",  "tote",   "L", "brass", 3, "Checklist into a jute bag, then a full thali"),
 ("belt",    "burst",  "carton", "R", "sage",  1, "Conveyor into the carton, then the kit opens out into all thirteen"),
 ("rain",    "dabba",  "basket", "L", "sand",  2, "Rain into a basket, then into your masala dabba and pantry"),
 ("orbit",   "shelf",  "tote",   "R", "cream", 3, "Orbit into a jute bag, then onto your kitchen shelf"),
 ("slots",   "dishes", "kraft",  "R", "blush", 1, "Kit box fills slot by slot, then dinner is served"),
 ("saheli",  "door",   "kraft",  "L", "mint",  2, "From a Saheli's kitchen to your door"),
 ("jars",    "burst",  "gold",   "L", "dark",  3, "Dark shelf of jars into the gold bag, then the kit opens out"),
 ("marquee", "dabba",  "tote",   "R", "warm",  0, "Streams into a jute bag, then into the masala dabba"),
 ("stack",   "thali",  "gold",   "R", "dark",  2, "The clear kit fills in layers, then a brass thali, on dark green"),
]

def copy_html(side, hi):
    left = 56 if side == "L" else 835
    return ('<div class="cp" style="left:%spx"><p class="k">Healthy Grocery Kit &middot; new</p><h2>%s</h2><p class="d">%s</p>'
            '<a class="pl">Order the kit on WhatsApp <span>&rarr;</span></a><p class="ct">13 items &middot; 3 home-made masalas</p></div>'
            % (left, H2[hi], DESC))

figs, allcss = [], []
for n, (ps, ss, bk, side, pal, hi, cap) in enumerate(V, 1):
    ph, pc = pack(ps, n, bk, pal == "dark")
    sh, sc = serve(ss, n, bk, pal == "dark")
    allcss += pc + sc
    ax = 470 if side == "L" else 45
    stage = ('<div class="st %s"><div class="area" style="left:%spx"><div class="pk">%s</div><div class="sv">%s</div></div>%s'
             '<div class="phase"><i>Packed</i><i>Served</i></div></div>' % (pal, ax, ph, sh, copy_html(side, hi)))
    figs.append('<figure><div class="frame" tabindex="0" role="button" aria-label="Option %d, click for full size">%s</div>'
                '<figcaption><b>%02d</b> %s</figcaption></figure>' % (n, stage, n, cap))

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
.frame{position:relative;aspect-ratio:1245/569;overflow:hidden;border-radius:12px;cursor:zoom-in;outline:none}
.frame.full{position:fixed;inset:0;z-index:50;border-radius:0;aspect-ratio:auto;background:rgba(14,12,10,.92);cursor:zoom-out}
.st{position:absolute;left:0;top:0;width:1245px;height:569px;transform-origin:0 0;transform:scale(var(--s,.5));overflow:hidden;color:#1f3a26}
.frame.full .st{left:50%;top:50%;transform:translate(-50%,-50%) scale(var(--s))}
/* palettes */
.cream{background:radial-gradient(120% 120% at 80% 30%,#fbf6ea,#efe4cc)}
.sage{background:linear-gradient(160deg,#eef1e2,#d9e2c6)}
.warm{background:linear-gradient(160deg,#fbefdc,#f1d6ac)}
.brass{background:radial-gradient(120% 120% at 30% 20%,#fff4dc,#f0d39a)}
.blush{background:linear-gradient(160deg,#fdf3ef,#f4dcd3)}
.sand{background:#efe5d0;background-image:radial-gradient(rgba(120,90,40,.09) 1px,transparent 1.4px);background-size:7px 7px}
.mint{background:linear-gradient(160deg,#f1f6ee,#dcebdd)}
.dark{background:radial-gradient(120% 140% at 50% 0%,#28482f,#122016);color:#f4ecd8}
/* copy */
.cp{position:absolute;top:50%;transform:translateY(-50%);width:360px;z-index:6}
.cp .k{font:500 12px/1 "Jost";letter-spacing:.3em;text-transform:uppercase;color:#94660a}
.cp h2{font:600 40px/1.06 "Fraunces",serif;margin:14px 0 14px;color:#1f3a26}
.cp h2 em{display:block;color:#b5832a}
.cp .d{font:300 16px/1.55 "Jost";color:#3c4a35}
.cp .pl{display:inline-flex;gap:10px;align-items:center;margin-top:22px;padding:13px 22px;border-radius:999px;background:#1f3a26;color:#f4efe6;font:500 13px/1 "Jost";letter-spacing:.12em;text-transform:uppercase}
.cp .ct{margin-top:12px;font:500 12px/1 "Jost";letter-spacing:.14em;text-transform:uppercase;color:#7a6a48}
.dark .cp .k{color:#e0c27a}.dark .cp h2{color:#f2e8d0}.dark .cp h2 em{color:#e9cf98}.dark .cp .d{color:#d8ceb8}
.dark .cp .pl{background:linear-gradient(160deg,#f7dc96,#e0a51a 42%,#a8760f);color:#1e2c16}.dark .cp .ct{color:#c9a14a}
/* phase dots */
.phase{position:absolute;right:26px;top:20px;display:flex;gap:8px;z-index:8}
.phase i{font:500 11px/1 "Jost";letter-spacing:.2em;text-transform:uppercase;font-style:normal;padding:7px 12px;border-radius:999px;border:1px solid rgba(31,58,38,.3);color:#1f3a26;animation:14s linear infinite}
.phase i:first-child{animation-name:ph1}.phase i:last-child{animation-name:ph2}
@keyframes ph1{0%,58%{background:#1f3a26;color:#f4efe6}60%,100%{background:transparent;color:#1f3a26}}
@keyframes ph2{0%,58%{background:transparent;color:#1f3a26}60%,94%{background:#1f3a26;color:#f4efe6}96%,100%{background:transparent;color:#1f3a26}}
.dark .phase i{border-color:rgba(233,207,152,.5);color:#e9cf98}
.dark .phase i:first-child{animation-name:ph1d}.dark .phase i:last-child{animation-name:ph2d}
@keyframes ph1d{0%,58%{background:#e9cf98;color:#13221a}60%,100%{background:transparent;color:#e9cf98}}
@keyframes ph2d{0%,58%{background:transparent;color:#e9cf98}60%,94%{background:#e9cf98;color:#13221a}96%,100%{background:transparent;color:#e9cf98}}
/* area + scenes */
.area{position:absolute;top:30px;width:730px;height:510px}
.pk,.sv{position:absolute;inset:0;animation:14s linear infinite}
.pk{animation-name:pk}.sv{animation-name:sv}
@keyframes pk{0%{opacity:0}3%,56%{opacity:1}60%,100%{opacity:0}}
@keyframes sv{0%,58%{opacity:0}62%,92%{opacity:1}96%,100%{opacity:0}}
.bag,.mbag,.sbag{container-type:inline-size}
.blab{position:absolute;left:0;right:0;transform:translateY(-50%);text-align:center;font-style:normal;z-index:2;line-height:1;pointer-events:none}
.blab b{display:block;font-family:"Fraunces",serif;font-weight:700;font-size:1em;color:#1f3a26}
.blab small{display:block;font-family:"Jost",sans-serif;font-weight:500;letter-spacing:.12em;color:#94660a;margin-top:.35em}
.blab.gl b{color:#e9cf98;font-weight:600}.blab.gl small{color:#c9a14a}
.bag{position:absolute}.bag svg{width:100%;height:100%;display:block;overflow:visible}
.bk{z-index:1}.bf{z-index:3;filter:drop-shadow(0 18px 18px rgba(60,40,10,.28))}
.it{position:absolute;width:var(--s);height:var(--s);margin:calc(var(--s)/-2) 0 0 calc(var(--s)/-2);z-index:2;
  animation:14s cubic-bezier(.5,0,.3,1) infinite both;display:flex;flex-direction:column;align-items:center}
.it span{display:block;width:100%;height:100%;flex:0 0 auto;border-radius:50%;overflow:hidden;border:3px solid #fffaf0;box-shadow:0 8px 16px -8px rgba(40,25,5,.6);background:#fffaf0}
.it img{width:100%;height:100%;object-fit:cover;display:block}
.it b{white-space:nowrap;font:600 12px/1.1 "Jost";margin-top:5px;color:#2e2210}
.dark .it b{color:#f2e8d0}
.it.jar span{border-radius:12px 12px 14px 14px;height:calc(var(--s)*1.25);border-top:9px solid #8a5a2b}
.it.katori span{border:5px solid #d9a441;box-shadow:0 0 0 2px #a8760f,0 8px 14px -8px rgba(60,30,0,.6)}
.it.bowl span{border:7px solid #d7dadc;box-shadow:inset 0 0 0 3px #9aa0a4,0 6px 12px -6px rgba(0,0,0,.4)}
.it.row{flex-direction:row;width:auto;gap:14px;margin-left:calc(var(--s)/-2)}
.it.row span{width:var(--s)}.it.row b{font-size:15px;margin:0}
/* checklist */
.chk{list-style:none;position:absolute;left:0;top:0;width:280px}
.chk li{position:absolute;left:0;height:30px;display:flex;align-items:center;gap:10px;width:260px;animation:14s linear infinite both}
.chk li img{width:28px;height:28px;border-radius:50%;object-fit:cover;opacity:0}
.chk li span{font:500 15px/1 "Jost";color:#2e2210;margin-left:44px}
.chk li i{margin-left:auto;width:22px;height:22px;border-radius:50%;background:#1f3a26;color:#fff;font:700 12px/22px "Jost";text-align:center;font-style:normal;animation:14s linear infinite both}
.chk::after{content:"";position:absolute;left:252px;top:0;width:1px;height:480px;background:rgba(31,58,38,.15)}
/* belt + carton lid */
.belt{position:absolute;height:22px;border-radius:11px;background:repeating-linear-gradient(90deg,#3d3a35 0 18px,#57534c 18px 36px);background-size:36px 22px;animation:belt .8s linear infinite;box-shadow:0 10px 0 -4px #2a2723}
@keyframes belt{to{background-position:36px 0}}
.lid{position:absolute;height:40px;z-index:4;background:#b8844b;border-radius:4px;box-shadow:0 6px 0 #a87638;animation:lid 14s linear infinite both}
@keyframes lid{0%,50%{transform:translateY(-140px);opacity:0}54%,100%{transform:none;opacity:1}}
/* orbit ring */
.ring{position:absolute;border:1.5px dashed rgba(148,102,10,.35);border-radius:50%}
.dark .ring{border-color:rgba(233,207,152,.35)}
/* flat-lay box */
.flat{position:absolute;border-radius:18px;background:linear-gradient(160deg,#e9d3ad,#d9bb8a);box-shadow:inset 0 0 0 10px #c9a46a,0 30px 50px -30px rgba(60,35,5,.6)}
.flat p{position:absolute;left:28px;top:24px;font:600 20px/1 "Fraunces",serif;color:#3a2a14}
.slot{position:absolute;width:74px;height:74px;border-radius:50%;border:2px dashed rgba(90,60,25,.4);z-index:1}
.flid{position:absolute;z-index:5;border-radius:18px;background:linear-gradient(160deg,#1f3a26,#2d5236);display:flex;flex-direction:column;align-items:center;justify-content:center;
  box-shadow:0 30px 50px -30px rgba(0,0,0,.7);animation:flid 14s cubic-bezier(.5,0,.3,1) infinite both}
.flid span{font:700 54px/1 "Fraunces",serif;color:#e9cf98}.flid i{font:500 14px/1 "Jost";letter-spacing:.3em;text-transform:uppercase;color:#f4efe6;font-style:normal;margin-top:12px}
.flid::after{content:"";position:absolute;left:50%;top:0;bottom:0;width:26px;margin-left:-13px;background:#c0392b}
@keyframes flid{0%,48%{transform:translateX(120%);opacity:0}54%,100%{transform:none;opacity:1}}
/* saheli arch */
.sarch{position:absolute;border-radius:120px 120px 18px 18px;overflow:hidden;box-shadow:0 24px 40px -24px rgba(60,30,10,.6)}
.sarch img{width:100%;height:100%;object-fit:cover}
.sarch p{position:absolute;left:0;right:0;bottom:0;padding:40px 16px 18px;background:linear-gradient(0deg,rgba(20,15,8,.85),transparent);color:#f4efe6;font:600 18px/1.2 "Fraunces",serif;text-align:center}
/* planks */
.plank{position:absolute;height:14px;border-radius:3px;background:linear-gradient(180deg,#a8743d,#7d5228);box-shadow:0 10px 14px -8px rgba(60,30,0,.6)}
/* marquee tracks */
.track{position:absolute;left:0;right:0;height:2px;background:repeating-linear-gradient(90deg,rgba(148,102,10,.35) 0 8px,transparent 8px 16px)}
/* glass */
.glass{position:absolute;border-radius:40px 40px 26px 26px;border:3px solid rgba(255,255,255,.9);background:linear-gradient(90deg,rgba(255,255,255,.35),rgba(255,255,255,.12) 40%,rgba(255,255,255,.3));box-shadow:inset 0 0 0 1px rgba(31,58,38,.15),0 30px 50px -30px rgba(60,35,5,.5);z-index:4;pointer-events:none}
.glass::before{content:"";position:absolute;left:30px;right:30px;top:-22px;height:26px;border-radius:10px;background:#8a5a2b}
.glass p{position:absolute;left:0;right:0;top:22px;text-align:center;font:600 14px/1 "Jost";letter-spacing:.18em;text-transform:uppercase;color:#1f3a26}
.dark .glass{border-color:rgba(233,207,152,.7);background:linear-gradient(90deg,rgba(233,207,152,.14),rgba(233,207,152,.04) 40%,rgba(233,207,152,.12))}
.dark .glass p{color:#e9cf98}
/* serve: mini bag, arrow, dishes */
.mbag{position:absolute;aspect-ratio:200/240}.mbag svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.arrow{position:absolute;width:70px;height:2px;background:#b5832a}.arrow::after{content:"";position:absolute;right:-2px;top:-6px;border:7px solid transparent;border-left:12px solid #b5832a;border-right:0}
.dish{position:absolute;width:150px;margin-left:-75px;margin-top:-75px;text-align:center;animation:14s cubic-bezier(.3,1.4,.5,1) infinite both}
.dish span{display:block;width:150px;height:150px;border-radius:50%;overflow:hidden;border:8px solid #fffaf2;box-shadow:0 0 0 1px rgba(0,0,0,.08),0 20px 30px -18px rgba(40,25,5,.7)}
.dish img{width:100%;height:100%;object-fit:cover}
.dish b{display:block;margin-top:10px;font:600 18px/1 "Fraunces",serif;color:#1f3a26}
.dark .dish b{color:#f2e8d0}
.steam{position:absolute;left:50%;top:-40px;width:30px;height:36px;margin-left:-15px;border-left:3px solid rgba(150,150,150,.5);border-radius:50%;animation:steam 2s ease-in-out infinite}
@keyframes steam{0%{opacity:0;transform:translateY(10px)}50%{opacity:1}100%{opacity:0;transform:translateY(-12px)}}
.scap{position:absolute;text-align:center;font:italic 500 20px/1.2 "Fraunces",serif;color:#7a5418}
.dark .scap{color:#e9cf98}
/* thali */
.thali{position:absolute;width:490px;height:490px;border-radius:50%;background:radial-gradient(circle,#f3cf7a 0 52%,#e2b04a 53% 62%,#c99327 63% 66%,#f0c868 67% 100%);box-shadow:inset 0 0 0 6px #b58322,0 30px 50px -26px rgba(80,50,0,.7);display:grid;place-items:center}
.thali p{text-align:center;font:600 30px/1 "Fraunces",serif;color:#5a3a06}.thali p span{display:block;font:500 12px/1 "Jost";letter-spacing:.24em;text-transform:uppercase;margin-top:8px}
/* door scene */
.road{position:absolute;left:0;right:0;top:440px;height:8px;background:#5b5650;border-radius:4px}
.door{position:absolute;left:560px;top:150px;width:150px;height:290px;background:#7d5228;border:10px solid #f4ead6;border-bottom:0;border-radius:70px 70px 0 0}
.door i{position:absolute;right:16px;top:150px;width:12px;height:12px;border-radius:50%;background:#e0b04a}
.scoot{position:absolute;left:60px;top:300px;width:220px;animation:14s cubic-bezier(.5,0,.3,1) infinite both}
.scoot .sc{width:220px;display:block;margin-top:-4px}
.sbag{position:relative;width:96px;height:115px;margin-left:30px;margin-bottom:-60px}.sbag svg{position:absolute;inset:0;width:100%;height:100%}
.okb{position:absolute;left:600px;top:80px;width:64px;height:64px;border-radius:50%;background:#25a35a;color:#fff;font:700 32px/64px "Jost";text-align:center;animation:14s linear infinite both}
.msg{position:absolute;left:40px;top:60px;width:330px;padding:16px 18px;border-radius:16px 16px 16px 4px;background:#fff;box-shadow:0 14px 30px -18px rgba(0,0,0,.5);font:400 16px/1.4 "Jost";color:#1e2c16;animation:14s linear infinite both}
.msg b{display:block;font:600 12px/1 "Jost";letter-spacing:.2em;color:#25a35a;margin-bottom:6px}
/* dabba */
.dabba{position:absolute;width:450px;height:450px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#f4f6f7,#b9bfc3 70%,#8f969b);box-shadow:inset 0 0 0 10px #d5d9dc,0 30px 50px -26px rgba(0,0,0,.55)}
.also{position:absolute;font:600 22px/1 "Fraunces",serif;color:#1f3a26}
.dark .also{color:#f2e8d0}
"""

JS = r"""
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
<!-- 14 Oct 2026. Owner: "I want to create a block under satva saheli for the
     healthy grocery kit with these masalas inside ... give me variations 20 of
     masalas being added to the bag as a kit and being served". Review page
     only - not linked, noindex. Each preview is one screen of the section at
     the owner's window (1245 x 569, under the nav). Every loop is 14s: the
     thirteen are packed (first half), then served (second half).
     Generated by genkit.py in the session scratchpad. -->
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Grocery Kit Block Options</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>%s
%s
</style>
</head>
<body>
<header>
  <p class="k0">DS Satva &middot; kit block review</p>
  <h1>Healthy Grocery Kit block &mdash; 20 options</h1>
  <p>This block would sit right under Satva Saheli. In every option the thirteen kit items are first <b>packed</b> into a bag or box, then <b>served</b>. Each loop runs 14 seconds, and the pill at the top right shows which half you're watching. Click an option to see it full size (click again or press Esc to come back). Tell me the number you like. The three masalas shown are Garam, Sambar and Chatpat until you name yours. <a href="index.html">Back to the site</a></p>
</header>
<div class="grid">
%s
</div>
<script>%s</script>
</body>
</html>
""" % (CSS, "\n".join(allcss), "\n".join(figs), JS)

open(OUT, "w").write(html)
print("wrote", OUT, len(html)//1024, "KB")
