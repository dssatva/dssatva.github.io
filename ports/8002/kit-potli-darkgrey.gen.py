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

OUT = os.path.expanduser("~/dssatva/ports/8002/kit-potli-darkgrey.html")
COCOA, TAUPE, BLUSH = "#353538", "#67656a", "#f6d8d8"
GRAD = "linear-gradient(90deg,#353538 0%,#434346 26%,#67656a 44%,#a99ea2 60%,#e2c9cc 74%,#f6d8d8 86%,#f8dfdf 100%)"

def copy(x, w, kick="Healthy Grocery Kit", title="SATVA", sub="K I T", line="One kit, straight from a Saheli.",
         d="Thirteen pure kitchen essentials in one hand-tied potli &mdash; three of them masalas blended at home by our Sahelis.", top="50%", cls=""):
    return ('<div class="mc %s" style="left:%dpx;top:%s;width:%dpx"><p class="k">%s</p>'
            '<div class="lock"><b>%s</b><span>%s</span><em>%s</em></div><p class="d">%s</p>'
            '<div class="ctas"><a class="gold">Buy the kit</a><a class="ghost">Call +91-9689888822</a></div></div>'
            % (cls, x, top, w, kick, title, sub, line, d))

V = []
V.append(("Grey into pink", "Dark charcoal grey melting into pink, white words with pink accents, the potli on the pink",
  "background:" + GRAD, copy(80, 470) + h.shadow(930, 50, 300) + h.potli("m1", 300, 780, 58)))
V.append(("Split with a pink seam", "A charcoal panel and a pink panel side by side, a thin pink line between",
  "background:linear-gradient(90deg,#353538 0 49%,#f2b6c1 49% 49.2%,#f6d8d8 49.2%)",
  copy(70, 460) + h.shadow(935, 50, 300) + h.potli("m3", 300, 785, 58)))
V.append(("Pink arch on charcoal", "All charcoal, with a tall pink arch window holding the potli and a Saheli stamp",
  "background:radial-gradient(90% 100% at 20% 40%,#454548,#2a2a2d)",
  copy(80, 470) + '<div class="arch blush" style="left:700px;top:28px;width:430px;height:541px"></div>'
  + '<div class="stamp" style="left:660px;top:70px"><img src="assets/saheli-mark-bright.svg" alt=""><b>Packed by<br>Satva Sahelis</b></div>'
  + h.shadow(915, 26, 300) + h.potli("m4", 300, 765, 34)))
V.append(("Charcoal card on pink", "Pink all over, the words in a charcoal card on the left - lighter overall",
  "background:radial-gradient(90% 100% at 75% 40%,#fbeeee,#f2d2d2)",
  '<div class="card" style="left:44px;top:44px;width:560px;height:481px"></div>' + copy(90, 470) + h.shadow(930, 50, 300) + h.potli("m5", 300, 780, 58)))
ring = ""
for i, im in enumerate(h.ITEMS):
    a = -math.pi / 2 + i * 2 * math.pi / 13
    ring += '<span class="orb" style="--a:%.3frad"><span class="it"><img src="assets/%s.jpg" alt=""></span></span>' % (a, im)
V.append(("Orbit", "Charcoal into pink, the thirteen ingredients circling the potli on a pink ring",
  "background:" + GRAD, copy(80, 440) + '<div class="ring gold" style="left:905px;top:300px">%s</div>' % ring + h.shadow(905, 70, 290) + h.potli("m6", 280, 765, 80, z=5)))
V.append(("Pink glow", "Deep charcoal with a big soft pink glow behind the potli - the most dramatic",
  "background:radial-gradient(42% 70% at 74% 55%,#f6d8d8 0%,#e8c0c2 30%,#67656a 62%,#353538 85%)",
  copy(80, 470) + h.shadow(920, 52, 300) + h.potli("m8", 300, 770, 60)))
V.append(("Charcoal top, pink floor", "Charcoal at the top melting down to a pink floor, the potli standing on the pink",
  "background:linear-gradient(180deg,#353538 0%,#47474a 40%,#a99ea2 66%,#f0d6d6 80%,#f6d8d8 100%)",
  copy(80, 520, top="44px", cls="flat") + h.shadow(960, 34, 280) + h.potli("m9", 270, 825, 40)))
arc = ""
for i, im in enumerate(h.ITEMS[:9]):
    x = 690 + i * 60
    u_ = (x - 930) / 280.0
    arc += h.item(im, x, int(452 + 64 * math.sqrt(max(0, 1 - u_ * u_))), 62, "bowl")
V.append(("Bowls in front", "Charcoal into pink, an arc of spice bowls in front of the potli",
  "background:" + GRAD, copy(80, 440) + h.shadow(930, 120, 270) + h.potli("m10", 260, 800, 130) + arc))
V.append(("Giant KIT", "Charcoal into pink, a huge outlined KIT in pink behind the potli",
  "background:" + GRAD, '<div class="giant gold" style="left:640px;top:40px">KIT</div>' + copy(80, 470) + h.shadow(930, 50, 300) + h.potli("m11", 300, 780, 58)))
V.append(("Minimal frame", "Charcoal inside a thin pink frame: words, the potli on a pink arch panel, contents - quiet and premium",
  "background:#353538",
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
.mc .k{font:500 13px/1 "Jost";letter-spacing:.32em;text-transform:uppercase;color:#f2b6c1}
.mc .lock{margin:22px 0 0 0}
.mc .lock b{display:block;font:600 64px/1 "Fraunces",serif;color:#fff;letter-spacing:.01em}
.mc .lock span{display:block;font:500 20px/1 "Fraunces",serif;letter-spacing:.55em;color:#fff;margin-top:12px}
.mc .lock em{display:block;font:italic 500 22px/1.3 "Fraunces",serif;color:#f4bcc6;margin-top:14px}
.mc .d{font:300 17px/1.6 "Jost";color:#efe6df;margin-top:18px;max-width:42ch}
.mc .ctas{display:flex;flex-wrap:wrap;gap:14px;margin-top:26px;align-items:center}
.mc .gold,.mc .ghost{white-space:nowrap}
.mc .gold{padding:15px 30px;border-radius:999px;background:linear-gradient(160deg,#f7c9d1,#e996a6 55%,#d97a8e);color:#2a2a2d;font:600 16px/1 "Jost";letter-spacing:.03em;box-shadow:0 14px 28px -14px rgba(200,90,110,.7)}
.mc .ghost{padding:14px 26px;border-radius:999px;border:1.5px solid rgba(255,250,240,.75);color:#fff;font:500 15px/1 "Jost";letter-spacing:.03em}
/* bits */
.arch.blush{background:linear-gradient(180deg,#f8e1e0,#efc6c6);box-shadow:inset 0 0 0 10px rgba(255,255,255,.3)}
.card{position:absolute;border-radius:26px;background:linear-gradient(160deg,#454548,#2a2a2d);box-shadow:0 30px 60px -30px rgba(40,25,15,.8);z-index:1}
.ring.gold::before{border-color:rgba(242,182,193,.75)}
.giant.gold{-webkit-text-stroke:2px rgba(242,182,193,.6)}
.panel{position:absolute;border-radius:200px 200px 22px 22px;background:linear-gradient(180deg,#f8e1e0,#eec4c4);z-index:1}
.frame-gold{border-color:rgba(242,182,193,.6)}
.inside.dark p{color:#f2b6c1}.inside.dark b{color:#fff;border-top-color:rgba(242,182,193,.45)}.inside.dark span{color:#e6dcd4}
.stamp{z-index:7}
.arch-line{border-color:#f2b6c1}
.mc .ghost{border-color:rgba(255,240,242,.75)}
"""
html = """<!DOCTYPE html>
<html lang="en">
<!-- 14 Oct 2026. Owner, pointing at saheli-variations.html option 3 (cocoa
     melting into blush, gold accents, white words): "can you give some
     variations in this colour combination"; later "this grey is too light.
     dark grey with pink" - this page. Review page only - not linked,
     noindex. The rose potli kit block in that palette, 12 compositions, at the
     owner's screen size (1245 x 569). Generated by kit-potli-mocha.gen.py. -->
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Kit Potli Dark Grey Pink</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>%s</style>
</head>
<body>
<header>
  <p class="k0">DS Satva &middot; kit block review</p>
  <h1>The rose potli &mdash; dark grey &amp; pink, 10 options</h1>
  <p>Dark charcoal grey melting into pink, white words with pink accents, and the rose potli. Click any one to see it full size (click again or press Esc to come back). Tell me the number you like. <a href="kit-potli-greypink.html">Light grey &amp; pink</a> &middot; <a href="kit-potli-mocha.html">Cocoa &amp; blush</a> &middot; <a href="kit-potli-hero.html">The 15 hero blocks</a> &middot; <a href="index.html#kit">Back to the site</a></p>
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
