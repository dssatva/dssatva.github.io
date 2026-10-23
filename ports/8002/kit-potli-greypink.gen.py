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

OUT = os.path.expanduser("~/dssatva/ports/8002/kit-potli-greypink.html")
COCOA, TAUPE, BLUSH = "#3b312a", "#6c605a", "#f3e1de"
GRAD = "linear-gradient(90deg,#e9e8e7 0%,#ebe7e6 30%,#efe1df 52%,#f3d9d5 72%,#f6dcd8 100%)"

def copy(x, w, kick="Healthy Grocery Kit", title="SATVA", sub="K I T", line="One kit, straight from a Saheli.",
         d="Thirteen pure kitchen essentials in one hand-tied potli &mdash; three of them masalas blended at home by our Sahelis.", top="50%", cls=""):
    return ('<div class="mc %s" style="left:%dpx;top:%s;width:%dpx"><p class="k">%s</p>'
            '<div class="lock"><b>%s</b><span>%s</span><em>%s</em></div><p class="d">%s</p>'
            '<div class="ctas"><a class="gold">Buy the kit</a><a class="ghost">Call +91-9689888822</a></div></div>'
            % (cls, x, top, w, kick, title, sub, line, d))

V = []
V.append(("Grey to pink", "Soft dove grey melting into blush pink, charcoal words, the potli on the pink",
  "background:" + GRAD, copy(80, 470) + h.shadow(930, 50, 300) + h.potli("g1", 300, 780, 58)))
V.append(("Split with a rose seam", "A light grey panel and a pink panel side by side, a thin rose line between",
  "background:linear-gradient(90deg,#ebeae9 0 49%,#c98d97 49% 49.2%,#f5dcd8 49.2%)",
  copy(70, 460) + h.shadow(935, 50, 300) + h.potli("g2", 300, 785, 58)))
V.append(("Pink arch on grey", "All pale grey, with a tall pink arch window holding the potli and a Saheli stamp",
  "background:radial-gradient(90% 100% at 20% 40%,#f2f1f0,#e3e1df)",
  copy(80, 470) + '<div class="arch pk" style="left:700px;top:28px;width:430px;height:541px"></div>'
  + '<div class="stamp" style="left:660px;top:70px"><img src="assets/saheli-mark-bright.svg" alt=""><b>Packed by<br>Satva Sahelis</b></div>'
  + h.shadow(915, 26, 300) + h.potli("g3", 300, 765, 34)))
V.append(("Grey card on pink", "Blush pink all over, the words in a soft grey card on the left",
  "background:radial-gradient(90% 100% at 75% 40%,#fbeeec,#f1d6d2)",
  '<div class="card gp" style="left:44px;top:44px;width:560px;height:481px"></div>' + copy(90, 470) + h.shadow(930, 50, 300) + h.potli("g4", 300, 780, 58)))
ring = ""
for i, im in enumerate(h.ITEMS):
    a = -math.pi / 2 + i * 2 * math.pi / 13
    ring += '<span class="orb" style="--a:%.3frad"><span class="it"><img src="assets/%s.jpg" alt=""></span></span>' % (a, im)
V.append(("Orbit", "Grey into pink, with the thirteen ingredients circling the potli on a rose ring",
  "background:" + GRAD, copy(80, 440) + '<div class="ring" style="left:905px;top:300px">%s</div>' % ring + h.shadow(905, 70, 290) + h.potli("g5", 280, 765, 80, z=5)))
V.append(("Pink glow", "Pale grey, with a big soft pink glow behind the potli",
  "background:radial-gradient(42% 70% at 74% 55%,#f8d9d5 0%,#f1e1df 40%,#ebeae9 75%)",
  copy(80, 470) + h.shadow(920, 52, 300) + h.potli("g6", 300, 770, 60)))
V.append(("Grey top, pink floor", "Grey at the top melting down to a pink floor, the potli standing on the pink",
  "background:linear-gradient(180deg,#ecebea 0%,#ebe8e7 45%,#f1dcd9 72%,#f5d6d1 100%)",
  copy(80, 560, top="44px", cls="flat") + h.shadow(960, 34, 280) + h.potli("g7", 270, 825, 40)))
arc = ""
for i, im in enumerate(h.ITEMS[:9]):
    x = 690 + i * 60
    u_ = (x - 930) / 280.0
    arc += h.item(im, x, int(452 + 64 * math.sqrt(max(0, 1 - u_ * u_))), 62, "bowl")
V.append(("Bowls in front", "Grey into pink, with a gentle arc of spice bowls in front of the potli",
  "background:" + GRAD, copy(80, 440) + h.shadow(930, 120, 270) + h.potli("g8", 260, 800, 130) + arc))
V.append(("Giant KIT", "Grey into pink, a huge outlined KIT in rose behind the potli",
  "background:" + GRAD, '<div class="giant" style="left:640px;top:40px">KIT</div>' + copy(80, 470) + h.shadow(930, 50, 300) + h.potli("g9", 300, 780, 58)))
V.append(("Minimal frame", "Pale grey inside a thin rose frame: words, the potli on a pink arch panel, contents - quiet and premium",
  "background:#efeeed",
  '<div class="frame-gold rose"></div><div class="panel" style="left:470px;top:60px;width:330px;height:449px"></div>' +
  copy(80, 360, line="One kit, straight<br>from a Saheli.", d="Thirteen pure essentials, hand-tied.") + h.shadow(635, 74, 250) + h.potli("g10", 250, 510, 80, tag=False) +
  '<div class="inside" style="left:860px;top:110px"><p>Inside every potli</p><b>Spices</b><span>Turmeric, chilli, mustard, cumin, coriander</span>'
  '<b>Home-made masalas</b><span>Garam, sambar, chatpat</span><b>Essentials</b><span>Pink salt, coconut sugar, chia, methi, monk fruit</span></div>'))

figs = []
for i, (n, cap, bg, inner) in enumerate(V, 1):
    figs.append('<figure><div class="frame" tabindex="0" role="button" aria-label="Option %d, click for full size"><div class="st" style="%s">%s</div></div>'
                '<figcaption><b>%02d</b> <strong>%s</strong> &mdash; %s</figcaption></figure>' % (i, bg.replace('"', "'"), inner, i, n, cap))

CSS = h.CSS + r"""
/* words: charcoal and rose on light grey and pink */
.mc{position:absolute;transform:translateY(-50%);z-index:5;color:#3a3536}
.mc.flat{transform:none}
.mc .k{font:500 13px/1 "Jost";letter-spacing:.32em;text-transform:uppercase;color:#b0607a}
.mc .lock{margin:22px 0 0 0}
.mc .lock b{display:block;font:600 64px/1 "Fraunces",serif;color:#3a3536;letter-spacing:.01em}
.mc .lock span{display:block;font:500 20px/1 "Fraunces",serif;letter-spacing:.55em;color:#3a3536;margin-top:12px}
.mc .lock em{display:block;font:italic 500 22px/1.3 "Fraunces",serif;color:#b0607a;margin-top:14px}
.mc .d{font:300 17px/1.6 "Jost";color:#5a5355;margin-top:18px;max-width:42ch}
.mc .ctas{display:flex;flex-wrap:wrap;gap:14px;margin-top:26px;align-items:center}
.mc .gold,.mc .ghost{white-space:nowrap}
.mc .gold{padding:15px 30px;border-radius:999px;background:#3a3536;color:#fbefee;font:600 16px/1 "Jost";letter-spacing:.03em;box-shadow:0 14px 28px -14px rgba(58,53,54,.7)}
.mc .ghost{padding:14px 26px;border-radius:999px;border:1.5px solid #b0607a;color:#9a4a63;font:500 15px/1 "Jost";letter-spacing:.03em}
/* bits */
.arch.pk{background:linear-gradient(180deg,#f8e0dc,#eec3bd);box-shadow:inset 0 0 0 10px rgba(255,255,255,.4)}
.card.gp{background:linear-gradient(160deg,#f4f3f2,#e3e1df);box-shadow:0 30px 60px -30px rgba(60,50,52,.45)}
.frame-gold.rose{border-color:rgba(176,96,122,.45)}
.arch.blush{background:linear-gradient(180deg,#f6e6e2,#e9cdc6);box-shadow:inset 0 0 0 10px rgba(255,255,255,.3)}
.card{position:absolute;border-radius:26px;background:linear-gradient(160deg,#4a3f37,#2f2620);box-shadow:0 30px 60px -30px rgba(40,25,15,.8);z-index:1}
.ring.gold::before{border-color:rgba(226,194,126,.7)}
.giant.gold{-webkit-text-stroke:2px rgba(226,194,126,.55)}
.panel{position:absolute;border-radius:200px 200px 22px 22px;background:linear-gradient(180deg,#f8e2de,#efc8c2);z-index:1}
.frame-gold{border-color:rgba(226,194,126,.55)}
.inside.dark p{color:#e2c27e}.inside.dark b{color:#fff;border-top-color:rgba(226,194,126,.4)}.inside.dark span{color:#e6dcd4}
.stamp{z-index:7}
"""
html = """<!DOCTYPE html>
<html lang="en">
<!-- 14 Oct 2026. Owner, pointing at saheli-variations.html option 3 (cocoa
     melting into blush, gold accents, white words): "can you give some
     variations in this colour combination"; then "another 10 variations of
     light grey and pink" - this page. Review page only - not linked,
     noindex. The rose potli kit block in that palette, 12 compositions, at the
     owner's screen size (1245 x 569). Generated by kit-potli-mocha.gen.py. -->
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Kit Potli Grey Pink</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>%s</style>
</head>
<body>
<header>
  <p class="k0">DS Satva &middot; kit block review</p>
  <h1>The rose potli &mdash; light grey &amp; pink, 10 options</h1>
  <p>Light grey and pink: soft dove grey melting into blush, charcoal words with rose accents, and the rose potli. Click any one to see it full size (click again or press Esc to come back). Tell me the number you like. <a href="kit-potli-mocha.html">Cocoa &amp; blush</a> &middot; <a href="kit-potli-hero.html">The 15 hero blocks</a> &middot; <a href="index.html#kit">Back to the site</a></p>
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
