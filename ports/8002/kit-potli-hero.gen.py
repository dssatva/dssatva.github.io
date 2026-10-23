#!/usr/bin/env python3
"""Generates ~/dssatva/ports/8002/kit-potli-hero.html - 15 hero-style kit
blocks around the rose woven potli (kit-potli-lilac-rose 02), letters in the
olive green the owner pointed at (#3d4529, sampled from their screenshot)."""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ.pop("LIGHT", None); os.environ.pop("DIFF", None); os.environ.pop("MIX", None); os.environ.pop("ONE", None)
import genpotli as g   # reuses potli() (it also rewrites its own default page, unchanged)

OUT = os.path.expanduser("~/dssatva/ports/8002/kit-potli-hero.html")
ROSE_C = g.P_MIX[1][4]          # the rose weave, cream cord and border
LETTER = "#3d4529"
ITEMS = ["u-turmeric", "u-chilli-powder", "u-mustard-seeds", "u-cumin-seeds", "u-coriander-seeds", "u-garam-masala",
         "u-sambar-masala", "u-chatpat-masala", "u-himalayan-pink-salt", "u-coconut-sugar", "u-chia-seeds", "u-methi-seeds", "j-monk-3-powder"]
NAMES = ["Turmeric", "Chilli", "Mustard", "Cumin", "Coriander", "Garam Masala", "Sambar Masala", "Chatpat Masala",
         "Pink Salt", "Coconut Sugar", "Chia", "Methi", "Monk Fruit"]

def potli(uid, w, left, bottom, tag=True, z=3):
    h = w * 418 / 356
    lk = ('<div class="lk"><img class="lk-m" src="assets/mark-dark.png" alt=""><b class="lk-s">SATVA</b>'
          '<span class="lk-d"><img src="assets/kit-sprig-l.png" alt=""><i>Dil Se Pure</i><img src="assets/kit-sprig-r.png" alt=""></span></div>')
    tg = '<div class="htag"><i></i><b>Healthy Grocery Kit</b><span>13 items</span></div>' if tag else ''
    return ('<div class="potli" style="width:%dpx;height:%dpx;left:%dpx;bottom:%dpx;z-index:%d">%s%s%s</div>'
            % (w, h, left, bottom, z, g.potli(uid, **ROSE_C), lk, tg))

def shadow(cx, bottom, w):
    return '<div class="sh" style="left:%dpx;bottom:%dpx;width:%dpx"></div>' % (cx - w // 2, bottom, w)

def item(img, x, y, s, cls=""):
    return '<span class="it %s" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx"><img src="assets/%s.jpg" alt=""></span>' % (cls, x - s // 2, y - s // 2, s, s, img)

def copy(x, y, w, kick="Healthy Grocery Kit &middot; sold only by our Sahelis", h="One kit, <em>straight from a Saheli</em>",
         d="Thirteen pure kitchen essentials in one hand-tied potli &mdash; three of them masalas blended at home by our Sahelis.", cls="", align="left", cta=True):
    c = ('<div class="cp %s" style="left:%dpx;top:%s;width:%dpx;text-align:%s"><p class="k">%s</p><h2>%s</h2><p class="d">%s</p>%s</div>'
         % (cls, x, y, w, align, kick, h, d,
            ('<div class="ctas" style="justify-content:%s"><a class="bt">Buy the kit</a><span class="tl">or call +91-9689888822</span></div>' % ("center" if align == "center" else "flex-start")) if cta else ""))
    return c

V = []

# 01 orbit
ring = ""
for i, im in enumerate(ITEMS):
    a = -math.pi / 2 + i * 2 * math.pi / 13
    ring += '<span class="orb" style="--a:%.3frad"><span class="it"><img src="assets/%s.jpg" alt=""></span></span>' % (a, im)
V.append(("Orbit", "The thirteen ingredients circle slowly round the potli - everything inside, on show",
  "background:radial-gradient(80% 90% at 70% 50%,#fff6f2,#f6e2db 60%,#efd3ca)",
  copy(56, "50%", 420) + '<div class="ring" style="left:870px;top:300px">%s</div>' % ring + shadow(870, 70, 300) + potli("h1", 280, 730, 80, z=5)))

# 02 split panels
V.append(("Split", "Rose panel for the words, cream for the potli, framed by a thin gold arch",
  "background:linear-gradient(90deg,#efcfc7 0 46%,#fbf6ef 46%)",
  copy(56, "50%", 440, cls="onrose") + '<div class="arch-line" style="left:720px;top:40px;width:340px;height:490px"></div>'
  + shadow(890, 52, 300) + potli("h2", 290, 745, 60)))

# 03 arch window
V.append(("Arch window", "The potli standing in a tall rose arch - the site's own arch shape - with a Saheli stamp",
  "background:radial-gradient(90% 90% at 30% 30%,#fffaf6,#f7ebe4)",
  copy(56, "50%", 440) + '<div class="arch" style="left:690px;top:28px;width:430px;height:541px"></div>'
  + '<div class="stamp" style="left:650px;top:70px"><img src="assets/saheli-mark-bright.svg" alt=""><b>Packed by<br>Satva Sahelis</b></div>'
  + shadow(905, 26, 300) + potli("h3", 300, 755, 34)))

# 04 giant type
V.append(("Giant type", "Huge outlined KIT behind the potli - an editorial, magazine-cover feel",
  "background:linear-gradient(180deg,#fdf7f3,#f5e3dc)",
  '<div class="giant" style="left:600px;top:40px">KIT</div>' + copy(56, "50%", 440) + shadow(900, 50, 300) + potli("h4", 300, 750, 58)))

# 05 podium
V.append(("Podium", "The potli on a rose podium under a soft spotlight - a premium product shot",
  "background:radial-gradient(60% 80% at 75% 20%,#ffffff,#f6e6e0 55%,#ecd2ca)",
  copy(56, "50%", 440) + '<div class="spot" style="left:700px;top:-80px"></div><div class="podium" style="left:745px;bottom:30px;width:330px"></div>'
  + shadow(910, 120, 260) + potli("h5", 250, 785, 128)))

# 06 steps footer
V.append(("Steps along the foot", "Potli on the left, words on the right, and the three steps as cards along the bottom",
  "background:radial-gradient(90% 90% at 20% 30%,#fff7f3,#f4e1da)",
  shadow(250, 150, 250) + potli("h6", 240, 120, 156, tag=False) +
  copy(470, "44px", 700, h="One kit, <em>straight from a Saheli</em>", cta=True) +
  '<div class="steps"><div><b>01</b><span>Call us</span><i>or ask a Saheli near you</i></div><div><b>02</b><span>She brings it home</span><i>the whole kit, hand-tied</i></div><div><b>03</b><span>Refill every month</span><i>same kit, same Saheli</i></div></div>'))

# 07 shelf
shelf = "".join(item(im, 70 + i * 62, 497, 50, "shelf-it") for i, im in enumerate(ITEMS[:12]))
V.append(("On the shelf", "The potli standing on a wooden shelf with the kit's ingredients lined up beside it",
  "background:linear-gradient(180deg,#fdf8f4,#f4e4dd)",
  copy(56, "40px", 560, h="One kit, <em>straight from a Saheli</em>", d="Thirteen pure kitchen essentials, hand-tied in one potli.") +
  '<div class="shelf"></div>' + shelf + potli("h7", 270, 900, 76)))

# 08 sunburst
V.append(("Sunburst", "Soft rose rays behind the potli, the kit's contents listed beside it - festive and joyful",
  "background:#fbefea",
  '<div class="rays" style="left:500px;top:-160px"></div>' + copy(56, "50%", 380, d="Thirteen pure kitchen essentials, hand-tied in one potli.") +
  shadow(700, 40, 280) + potli("h8", 270, 565, 48) +
  '<div class="inside" style="left:930px;top:80px"><p>Inside</p><b>Spices</b><span>Turmeric &middot; Chilli &middot; Mustard &middot; Cumin &middot; Coriander</span>'
  '<b>Home-made by our Sahelis</b><span>Garam &middot; Sambar &middot; Chatpat masala</span><b>Healthy essentials</b><span>Pink salt &middot; Coconut sugar &middot; Chia &middot; Methi &middot; Monk fruit</span></div>'))

# 09 spill
arc = ""
for i, im in enumerate(ITEMS[:9]):
    x = 650 + i * 60                         # even steps, left to right
    u_ = (x - 890) / 280.0
    arc += item(im, x, int(452 + 64 * math.sqrt(max(0, 1 - u_ * u_))), 62, "bowl")
V.append(("Spilling out", "A curve of little bowls in front of the potli - the kit, opened and served",
  "background:radial-gradient(90% 90% at 70% 30%,#fffaf7,#f5e4dd)",
  copy(56, "50%", 420) + shadow(890, 120, 270) + potli("h9", 260, 760, 130) + arc))

# 10 magazine
V.append(("Magazine", "A tall picture panel with the potli, and a big serif line beside it - like a magazine spread",
  "background:#fbf6f1",
  '<div class="mag" style="left:40px;top:34px;width:540px;height:501px"></div>' + shadow(310, 70, 290) + potli("h10", 280, 170, 78) +
  '<div class="quote" style="left:640px;top:70px;width:540px"><p class="k">Healthy Grocery Kit</p><h2>Thirteen essentials.<br><em>One hand-tied potli.</em></h2>'
  '<p class="d">Every Saheli brings the same kit to your door &mdash; spices, three home-made masalas, salt, sweeteners and seeds.</p>'
  '<div class="ctas"><a class="bt">Buy the kit</a><span class="tl">or call +91-9689888822</span></div></div>'))

# 11 woven halo
V.append(("Woven halo", "A big round woven mat behind the potli, framed by wheat sprigs - warm, handmade",
  "background:radial-gradient(90% 90% at 25% 30%,#fffaf6,#f6e7e0)",
  copy(56, "50%", 440) + '<div class="halo" style="left:660px;top:30px"></div>'
  + '<img class="sprig" src="assets/kit-sprig-l.png" style="left:650px;top:470px;width:120px" alt=""><img class="sprig" src="assets/kit-sprig-r.png" style="left:1060px;top:470px;width:120px" alt="">'
  + shadow(895, 60, 280) + potli("h11", 280, 755, 66)))

# 12 diagonal
V.append(("Diagonal", "Cream and rose split on a slant, the potli standing across the line",
  "background:linear-gradient(112deg,#fdf8f3 0 57%,#eec9c0 57%)",
  copy(56, "50%", 440) + shadow(900, 50, 300) + potli("h12", 300, 750, 58)))

# 13 collage
V.append(("Collage", "Four ingredient photographs framed round the potli, like a gallery wall",
  "background:radial-gradient(90% 90% at 30% 30%,#fffaf7,#f5e5de)",
  copy(56, "50%", 420) +
  item("u-turmeric", 640, 140, 150, "tile") + item("u-garam-masala", 1160, 120, 130, "tile") +
  item("u-chilli-powder", 650, 440, 130, "tile") + item("u-coriander-seeds", 1150, 430, 150, "tile") +
  shadow(900, 52, 280) + potli("h13", 280, 760, 60)))

# 14 minimal luxe
V.append(("Minimal luxe", "Three quiet columns inside a thin gold frame - words, potli, contents - the calm, premium one",
  "background:#fcf8f4",
  '<div class="frame-gold"></div>' +
  copy(80, "50%", 340, h="One kit, <em>straight from a Saheli</em>", d="Thirteen pure essentials, hand-tied.") +
  shadow(622, 64, 250) + potli("h14", 250, 497, 70, tag=False) +
  '<div class="inside lux" style="left:860px;top:110px"><p>Inside every potli</p><b>Spices</b><span>Turmeric, chilli, mustard, cumin, coriander</span>'
  '<b>Home-made masalas</b><span>Garam, sambar, chatpat</span><b>Essentials</b><span>Pink salt, coconut sugar, chia, methi, monk fruit</span></div>'))

# 15 gift ribbon
V.append(("Gift ribbon", "A gold ribbon across the corner, a NEW seal and a little sparkle - the kit as a gift",
  "background:radial-gradient(90% 100% at 75% 40%,#fff7f3,#f3dcd4)",
  '<div class="ribbon"></div><div class="seal" style="left:1080px;top:60px"><b>NEW</b><span>Healthy Grocery Kit</span></div>' +
  copy(56, "50%", 440, kick="New &middot; the Healthy Grocery Kit") +
  '<i class="spark" style="left:740px;top:120px"></i><i class="spark s2" style="left:1030px;top:220px"></i><i class="spark s3" style="left:780px;top:330px"></i>' +
  shadow(900, 50, 300) + potli("h15", 290, 755, 58)))

figs = []
for i, (n, cap, bg, inner) in enumerate(V, 1):
    figs.append('<figure><div class="frame" tabindex="0" role="button" aria-label="Option %d, click for full size"><div class="st" style="%s">%s</div></div>'
                '<figcaption><b>%02d</b> <strong>%s</strong> &mdash; %s</figcaption></figure>' % (i, bg.replace('"', "'"), inner, i, n, cap))

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
body{background:#1e1f1b;color:#f4efe6;font-family:"Jost",system-ui,sans-serif;padding:0 16px 70px}
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
.st{position:absolute;left:0;top:0;width:1245px;height:569px;transform-origin:0 0;transform:scale(var(--s,.5));overflow:hidden;color:#1f3a26}
.frame.full .st{left:50%;top:50%;transform:translate(-50%,-50%) scale(var(--s))}
/* words */
.cp{position:absolute;transform:translateY(-50%);z-index:5}
.cp[style*="top:4"],.cp[style*="top:44px"]{transform:none}
.cp .k{font:500 12px/1.3 "Jost";letter-spacing:.26em;text-transform:uppercase;color:#a6475b}
.cp h2,.quote h2{font:600 46px/1.05 "Fraunces",serif;margin:12px 0 14px;color:#1f3a26}
.cp h2 em,.quote h2 em{display:block;color:#a6475b}
.cp .d,.quote .d{font:300 16.5px/1.55 "Jost";color:#4f4044;max-width:44ch}
.cp[style*="center"] .d{margin:0 auto}
.ctas{display:flex;align-items:center;gap:18px;margin-top:24px}
.bt{display:inline-block;padding:14px 30px;border-radius:999px;background:#1f3a26;color:#fbf1ec;font:600 15px/1 "Jost";letter-spacing:.04em;box-shadow:0 12px 24px -14px rgba(31,58,38,.8)}
.tl{font:500 15px/1 "Jost";color:#8f3a4c}
.cp.onrose .k{color:#7a2f3e}.cp.onrose .d{color:#4a3236}
.quote{position:absolute;z-index:5}
.quote .k{font:500 12px/1.3 "Jost";letter-spacing:.26em;text-transform:uppercase;color:#a6475b}
.quote h2{font-size:54px}
/* potli */
.potli{position:absolute;container-type:inline-size;filter:drop-shadow(0 18px 18px rgba(80,40,30,.25))}
.potli svg{width:100%;height:100%;display:block;overflow:visible}
.lk{position:absolute;left:50%;top:44%;width:38%;transform:translateX(-50%);text-align:center;container-type:inline-size;pointer-events:none}
.lk-m,.lk-d img{mix-blend-mode:multiply}
.lk-m{display:block;width:60%;margin:0 auto}
.lk-s{display:block;font:400 22cqw/1 "Jost",sans-serif;letter-spacing:.2em;margin:5cqw 0 0 .2em;color:""" + LETTER + r"""}
.lk-d{display:flex;align-items:center;justify-content:center;gap:3cqw;margin-top:3cqw}
.lk-d img{height:6.5cqw;width:auto}
.lk-d i{font:400 10cqw/1 "Jost",sans-serif;font-style:normal;color:""" + LETTER + r"""}
.htag{position:absolute;left:78%;top:43%;width:22%;padding:8% 2% 5%;background:#e3c595;border-radius:4px 4px 10px 10px;text-align:center;transform:rotate(-8deg);
  box-shadow:0 10px 14px -8px rgba(0,0,0,.5);clip-path:polygon(18% 0,82% 0,100% 14%,100% 100%,0 100%,0 14%)}
.htag::after{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(90,60,20,.06) 0 1px,transparent 1px 4px)}
.htag i{position:absolute;left:50%;top:5%;width:10%;aspect-ratio:1;margin-left:-5%;border-radius:50%;background:#6b4a14}
.htag b{display:block;font:600 4.2cqw/1.08 "Fraunces",serif;color:#3a2a14}
.htag span{display:block;font:500 3.2cqw/1.2 "Jost";letter-spacing:.1em;text-transform:uppercase;color:#7a5418;margin-top:4%}
.sh{position:absolute;height:36px;border-radius:50%;background:radial-gradient(closest-side,rgba(90,45,35,.35),transparent);z-index:2}
.it{position:absolute;border-radius:50%;overflow:hidden;border:4px solid #fffaf4;box-shadow:0 10px 18px -10px rgba(80,40,30,.6);z-index:4;display:block}
.it img{width:100%;height:100%;object-fit:cover;display:block}
/* 01 orbit */
.ring{position:absolute;width:0;height:0;z-index:4;animation:spin 60s linear infinite}
.orb{position:absolute;left:0;top:0;transform:rotate(var(--a)) translate(250px) rotate(calc(-1 * var(--a)))}
.orb .it{position:relative;display:block;width:54px;height:54px;margin:-27px 0 0 -27px;animation:spin 60s linear infinite reverse}
.ring::before{content:"";position:absolute;left:-250px;top:-250px;width:500px;height:500px;border-radius:50%;border:1.5px dashed rgba(166,71,91,.35)}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes spinr{to{transform:rotate(-360deg)}}
/* 02 */ .arch-line{position:absolute;border:1.5px solid #c9962a;border-bottom:0;border-radius:170px 170px 0 0;z-index:1}
/* 03 */ .arch{position:absolute;border-radius:215px 215px 0 0;background:linear-gradient(180deg,#f3d3cb,#e6b9ae);box-shadow:inset 0 0 0 10px rgba(255,255,255,.35);z-index:1}
.stamp{position:absolute;z-index:6;width:110px;height:110px;border-radius:50%;background:#fffaf4;display:flex;flex-direction:column;align-items:center;justify-content:center;
  box-shadow:0 12px 24px -14px rgba(80,40,30,.6);border:1.5px dashed #c98d84;text-align:center;transform:rotate(-10deg)}
.stamp img{width:34px}.stamp b{font:600 11px/1.15 "Jost";letter-spacing:.06em;text-transform:uppercase;color:#8f3a4c;margin-top:4px}
/* 04 */ .giant{position:absolute;font:700 400px/1 "Fraunces",serif;color:transparent;-webkit-text-stroke:2px rgba(166,71,91,.28);letter-spacing:-.02em;z-index:1}
/* 05 */ .spot{position:absolute;width:420px;height:560px;background:radial-gradient(50% 60% at 50% 30%,rgba(255,255,255,.9),transparent 70%);z-index:1}
.podium{position:absolute;height:110px;z-index:2;background:linear-gradient(90deg,#e2b2a7,#f1cfc6 45%,#d9a397);border-radius:0 0 50% 50%/0 0 30px 30px}
.podium::before{content:"";position:absolute;left:0;right:0;top:-34px;height:68px;border-radius:50%;background:linear-gradient(180deg,#f9e2dc,#efc9bf)}
/* 06 */ .steps{position:absolute;left:470px;right:56px;bottom:40px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px;z-index:5}
.steps div{background:#fffaf6;border-radius:16px;padding:16px 18px;box-shadow:0 14px 28px -20px rgba(80,40,30,.6);border:1px solid rgba(166,71,91,.12)}
.steps b{display:block;font:500 13px/1 "Fraunces",serif;color:#a6475b}.steps span{display:block;font:600 17px/1.2 "Fraunces",serif;color:#1f3a26;margin-top:6px}
.steps i{display:block;font:300 13px/1.4 "Jost";font-style:normal;color:#4f4044;margin-top:3px}
.cp[style*="top:44px"] h2{font-size:40px}.cp[style*="top:44px"] .d{max-width:60ch}
/* 07 */ .shelf{position:absolute;left:0;right:0;bottom:44px;height:16px;background:linear-gradient(180deg,#b9824a,#8a5a2b);box-shadow:0 12px 16px -8px rgba(60,30,0,.5);z-index:3}
.shelf-it{z-index:4}
.cp[style*="top:40px"]{transform:none}.cp[style*="top:40px"] h2{font-size:42px}
/* 08 */ .rays{position:absolute;width:880px;height:880px;border-radius:50%;z-index:0;
  background:repeating-conic-gradient(from 0deg,rgba(231,189,181,.55) 0 7deg,rgba(255,248,244,0) 7deg 15deg);
  -webkit-mask-image:radial-gradient(closest-side,#000 30%,transparent 72%);mask-image:radial-gradient(closest-side,#000 30%,transparent 72%)}
.inside{position:absolute;z-index:5;width:260px}
.inside p{font:500 12px/1 "Jost";letter-spacing:.26em;text-transform:uppercase;color:#a6475b;margin-bottom:14px}
.inside b{display:block;font:600 16px/1.2 "Fraunces",serif;color:#1f3a26;margin-top:14px;padding-top:12px;border-top:1px solid rgba(166,71,91,.25)}
.inside span{display:block;font:300 14px/1.5 "Jost";color:#4f4044;margin-top:4px}
.inside.lux b{border-top-color:rgba(201,150,42,.5)}
/* 09 */ .bowl{z-index:4;border-width:5px}
/* 10 */ .mag{position:absolute;border-radius:24px;background:linear-gradient(180deg,#f3d6ce 0 72%,#e8c2b7 72%);box-shadow:inset 0 0 0 1px rgba(166,71,91,.12)}
/* 11 */ .halo{position:absolute;width:470px;height:470px;border-radius:50%;z-index:1;
  background:repeating-radial-gradient(circle,#e9cdb0 0 6px,#dcb995 6px 9px,#ecd5bb 9px 14px);box-shadow:inset 0 0 0 12px #d9b28c,0 30px 50px -30px rgba(80,40,20,.5);opacity:.9}
.sprig{position:absolute;z-index:4}
/* 13 */ .tile{border-radius:20px;border:6px solid #fffaf4}
/* 14 */ .frame-gold{position:absolute;inset:22px;border:1px solid rgba(201,150,42,.55);border-radius:6px;z-index:1}
/* 15 */ .ribbon{position:absolute;left:-120px;top:70px;width:520px;height:46px;transform:rotate(-38deg);background:linear-gradient(90deg,#e6c27a,#c9962a);box-shadow:0 8px 16px -8px rgba(80,50,0,.5);z-index:1;opacity:.9}
.seal{position:absolute;z-index:6;width:120px;height:120px;border-radius:50%;background:#a6475b;color:#fff4ef;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
  box-shadow:0 0 0 6px #fbefea,0 0 0 7px #a6475b,0 16px 30px -16px rgba(80,20,30,.7);transform:rotate(10deg)}
.seal b{font:700 30px/1 "Fraunces",serif}.seal span{font:500 9.5px/1.2 "Jost";letter-spacing:.14em;text-transform:uppercase;margin-top:6px;padding:0 14px}
.spark{position:absolute;width:22px;height:22px;z-index:6;background:#c9962a;clip-path:polygon(50% 0,60% 40%,100% 50%,60% 60%,50% 100%,40% 60%,0 50%,40% 40%);animation:tw 2.4s ease-in-out infinite}
.spark.s2{animation-delay:.8s;width:16px;height:16px}.spark.s3{animation-delay:1.6s;width:12px;height:12px}
@keyframes tw{0%,100%{opacity:.25;transform:scale(.7)}50%{opacity:1;transform:scale(1.1)}}
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
<!-- 14 Oct 2026. Owner, pointing at the rose potli (kit-potli-lilac-rose 02):
     "i want the colour of the letters to be in this colour and give me 15
     variations with stunning block for hero designs". Review page only - not
     linked, noindex. The rose woven potli, SATVA / Dil Se Pure in the olive
     green of their screenshot (#3d4529), the DS mark printed on the cloth as
     there; fifteen block compositions at the owner's screen size (1245 x 569).
     Generated by kit-potli-hero.gen.py beside this file. -->
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Kit Potli Hero Blocks</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>%s</style>
</head>
<body>
<header>
  <p class="k0">DS Satva &middot; kit block review</p>
  <h1>The rose potli &mdash; 15 hero blocks</h1>
  <p>The rose woven potli you chose, with SATVA and Dil Se Pure in the olive green from your screenshot, set in fifteen different block designs. Click any one to see it full size (click again or press Esc to come back). Tell me the number you like. <a href="kit-potli-lilac-rose.html">The lilac &amp; rose potlis</a> &middot; <a href="index.html#kit">Back to the site</a></p>
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
