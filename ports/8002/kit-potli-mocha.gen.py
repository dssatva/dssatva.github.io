#!/usr/bin/env python3
"""Generates ~/dssatva/ports/8002/kit-potli-mocha.html - the rose potli kit
block in the colours of saheli-variations.html option 3 (cocoa melting into
blush, gold accents, white words), 12 compositions."""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
for k in ("LIGHT", "DIFF", "MIX", "ONE"):
    os.environ.pop(k, None)
import genhero as h   # potli(), shadow(), item(), base CSS (also rewrites its own page, unchanged)

OUT = os.path.expanduser("~/dssatva/ports/8002/kit-potli-mocha.html")
COCOA, TAUPE, BLUSH = "#3b312a", "#6c605a", "#f3e1de"
GRAD = "linear-gradient(90deg,#3b312a 0%,#4d423b 26%,#6c605a 44%,#a8968f 60%,#dcc8c3 74%,#f3e1de 86%,#f5e6e3 100%)"

def copy(x, w, kick="Healthy Grocery Kit", title="SATVA", sub="K I T", line="One kit, straight from a Saheli.",
         d="Thirteen pure kitchen essentials in one hand-tied potli &mdash; three of them masalas blended at home by our Sahelis.", top="50%", cls=""):
    return ('<div class="mc %s" style="left:%dpx;top:%s;width:%dpx"><p class="k">%s</p>'
            '<div class="lock"><b>%s</b><span>%s</span><em>%s</em></div><p class="d">%s</p>'
            '<div class="ctas"><a class="gold">Buy the kit</a><a class="ghost">Call +91-9689888822</a></div></div>'
            % (cls, x, top, w, kick, title, sub, line, d))

V = []
V.append(("Melt", "Exactly the reference: cocoa melting into blush, words on the dark side, the potli on the blush",
  "background:" + GRAD, copy(80, 470) + h.shadow(930, 50, 300) + h.potli("m1", 300, 780, 58)))
V.append(("Melt + podium", "The same melt, the potli raised on a blush podium under a soft light",
  "background:" + GRAD, copy(80, 470) + '<div class="spot" style="left:730px;top:-80px"></div><div class="podium" style="left:765px;bottom:30px;width:330px"></div>'
  + h.shadow(930, 120, 260) + h.potli("m2", 250, 805, 128)))
V.append(("Hard split", "A clean cocoa panel and a blush panel side by side, a thin gold seam between",
  "background:linear-gradient(90deg,#3b312a 0 49%,#c9a14a 49% 49.2%,#f3e1de 49.2%)",
  copy(70, 460) + h.shadow(935, 50, 300) + h.potli("m3", 300, 785, 58)))
V.append(("Blush arch", "All cocoa, with a tall blush arch window holding the potli",
  "background:radial-gradient(90% 100% at 20% 40%,#4a3f37,#2f2620)",
  copy(80, 470) + '<div class="arch blush" style="left:700px;top:28px;width:430px;height:541px"></div>'
  + '<div class="stamp" style="left:660px;top:70px"><img src="assets/saheli-mark-bright.svg" alt=""><b>Packed by<br>Satva Sahelis</b></div>'
  + h.shadow(915, 26, 300) + h.potli("m4", 300, 765, 34)))
V.append(("Cocoa card on blush", "Blush all over, the words in a cocoa card on the left - softer, lighter overall",
  "background:radial-gradient(90% 100% at 75% 40%,#fbf1ef,#efd9d4)",
  '<div class="card" style="left:44px;top:44px;width:560px;height:481px"></div>' + copy(90, 470) + h.shadow(930, 50, 300) + h.potli("m5", 300, 780, 58)))
ring = ""
for i, im in enumerate(h.ITEMS):
    a = -math.pi / 2 + i * 2 * math.pi / 13
    ring += '<span class="orb" style="--a:%.3frad"><span class="it"><img src="assets/%s.jpg" alt=""></span></span>' % (a, im)
V.append(("Melt + orbit", "The melt, with the thirteen ingredients circling the potli on a gold ring",
  "background:" + GRAD, copy(80, 440) + '<div class="ring gold" style="left:905px;top:300px">%s</div>' % ring + h.shadow(905, 70, 290) + h.potli("m6", 280, 765, 80, z=5)))
V.append(("Gold arch line", "The melt, a fine gold arch drawn round the potli and a Saheli stamp",
  "background:" + GRAD, copy(80, 470) + '<div class="arch-line" style="left:760px;top:40px;width:340px;height:490px"></div>'
  + '<div class="stamp" style="left:1060px;top:80px"><img src="assets/saheli-mark-bright.svg" alt=""><b>Packed by<br>Satva Sahelis</b></div>'
  + h.shadow(930, 52, 290) + h.potli("m7", 285, 787, 60)))
V.append(("Blush glow", "Deep cocoa, with a big soft blush glow behind the potli - dramatic and warm",
  "background:radial-gradient(42% 70% at 74% 55%,#f3e1de 0%,#d9bfb8 30%,#6c605a 62%,#3b312a 85%)",
  copy(80, 470) + h.shadow(920, 52, 300) + h.potli("m8", 300, 770, 60)))
V.append(("Top to floor", "Cocoa at the top melting down to a blush floor, the words above and the potli standing on the blush",
  "background:linear-gradient(180deg,#3b312a 0%,#55493f 40%,#a8968f 66%,#ecd8d4 80%,#f3e1de 100%)",
  copy(80, 520, top="44px", cls="flat") + h.shadow(960, 34, 280) + h.potli("m9", 270, 825, 40)))
arc = ""
for i, im in enumerate(h.ITEMS[:9]):
    x = 690 + i * 60
    u_ = (x - 930) / 280.0
    arc += h.item(im, x, int(452 + 64 * math.sqrt(max(0, 1 - u_ * u_))), 62, "bowl")
V.append(("Melt + bowls", "The melt, with a gentle arc of spice bowls in front of the potli",
  "background:" + GRAD, copy(80, 440) + h.shadow(930, 120, 270) + h.potli("m10", 260, 800, 130) + arc))
V.append(("Giant KIT", "The melt, a huge outlined KIT in gold behind the potli",
  "background:" + GRAD, '<div class="giant gold" style="left:640px;top:40px">KIT</div>' + copy(80, 470) + h.shadow(930, 50, 300) + h.potli("m11", 300, 780, 58)))
V.append(("Minimal frame", "Cocoa inside a thin gold frame: words left, potli on a blush panel, contents right - the quiet, premium one",
  "background:#3b312a",
  '<div class="frame-gold"></div><div class="panel" style="left:470px;top:60px;width:330px;height:449px"></div>' +
  copy(80, 360, line="One kit, straight<br>from a Saheli.", d="Thirteen pure essentials, hand-tied.") + h.shadow(635, 74, 250) + h.potli("m12", 250, 510, 80, tag=False) +
  '<div class="inside dark" style="left:860px;top:110px"><p>Inside every potli</p><b>Spices</b><span>Turmeric, chilli, mustard, cumin, coriander</span>'
  '<b>Home-made masalas</b><span>Garam, sambar, chatpat</span><b>Essentials</b><span>Pink salt, coconut sugar, chia, methi, monk fruit</span></div>'))

figs = []
for i, (n, cap, bg, inner) in enumerate(V, 1):
    figs.append('<figure><div class="frame" tabindex="0" role="button" aria-label="Option %d, click for full size"><div class="st" style="%s">%s</div></div>'
                '<figcaption><b>%02d</b> <strong>%s</strong> &mdash; %s</figcaption></figure>' % (i, bg.replace('"', "'"), inner, i, n, cap))

CSS = h.CSS + r"""
/* words in the reference style: gold kicker, big white serif, spaced sub, gold italic */
.mc{position:absolute;transform:translateY(-50%);z-index:5;color:#fff}
.mc.flat{transform:none}
.mc .k{font:500 13px/1 "Jost";letter-spacing:.32em;text-transform:uppercase;color:#e2c27e}
.mc .lock{margin:22px 0 0 0}
.mc .lock b{display:block;font:600 64px/1 "Fraunces",serif;color:#fff;letter-spacing:.01em}
.mc .lock span{display:block;font:500 20px/1 "Fraunces",serif;letter-spacing:.55em;color:#fff;margin-top:12px}
.mc .lock em{display:block;font:italic 500 22px/1.3 "Fraunces",serif;color:#e8cc8c;margin-top:14px}
.mc .d{font:300 17px/1.6 "Jost";color:#efe6df;margin-top:18px;max-width:42ch}
.mc .ctas{display:flex;flex-wrap:wrap;gap:14px;margin-top:26px;align-items:center}
.mc .gold,.mc .ghost{white-space:nowrap}
.mc .gold{padding:15px 30px;border-radius:999px;background:linear-gradient(160deg,#f2d27a,#d9a73a 55%,#b8872a);color:#fffaf0;font:600 16px/1 "Jost";letter-spacing:.03em;box-shadow:0 14px 28px -14px rgba(180,130,30,.8)}
.mc .ghost{padding:14px 26px;border-radius:999px;border:1.5px solid rgba(255,250,240,.75);color:#fff;font:500 15px/1 "Jost";letter-spacing:.03em}
/* bits */
.arch.blush{background:linear-gradient(180deg,#f6e6e2,#e9cdc6);box-shadow:inset 0 0 0 10px rgba(255,255,255,.3)}
.card{position:absolute;border-radius:26px;background:linear-gradient(160deg,#4a3f37,#2f2620);box-shadow:0 30px 60px -30px rgba(40,25,15,.8);z-index:1}
.ring.gold::before{border-color:rgba(226,194,126,.7)}
.giant.gold{-webkit-text-stroke:2px rgba(226,194,126,.55)}
.panel{position:absolute;border-radius:200px 200px 22px 22px;background:linear-gradient(180deg,#f6e6e2,#e6c8c1);z-index:1}
.frame-gold{border-color:rgba(226,194,126,.55)}
.inside.dark p{color:#e2c27e}.inside.dark b{color:#fff;border-top-color:rgba(226,194,126,.4)}.inside.dark span{color:#e6dcd4}
.stamp{z-index:7}
"""
html = """<!DOCTYPE html>
<html lang="en">
<!-- 14 Oct 2026. Owner, pointing at saheli-variations.html option 3 (cocoa
     melting into blush, gold accents, white words): "can you give some
     variations in this colour combination". Review page only - not linked,
     noindex. The rose potli kit block in that palette, 12 compositions, at the
     owner's screen size (1245 x 569). Generated by kit-potli-mocha.gen.py. -->
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Kit Potli Cocoa Blush</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>%s</style>
</head>
<body>
<header>
  <p class="k0">DS Satva &middot; kit block review</p>
  <h1>The rose potli &mdash; cocoa &amp; blush, 12 options</h1>
  <p>The colours of the Saheli option you showed me &mdash; dark cocoa melting into blush, gold accents, white words &mdash; on the kit block with the rose potli. Click any one to see it full size (click again or press Esc to come back). Tell me the number you like. <a href="kit-potli-hero.html">The 15 hero blocks</a> &middot; <a href="index.html#kit">Back to the site</a></p>
</header>
<div class="grid">
%s
</div>
<script>%s</script>
</body>
</html>
""" % (CSS, "\n".join(figs), h.JS)
open(OUT, "w").write(html)
print("wrote", OUT, len(html) // 1024, "KB")
