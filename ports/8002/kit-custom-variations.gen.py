#!/usr/bin/env python3
"""kit-custom-variations.html - 15 designs for the "Build your own kit" block
at the end of Our Range (16 Oct 2026, owner: "can you give me some variations
for this atleast 15"). Each is drawn at the block's size on the owner's screen
(about 600 x 400). Ivory potli: assets/kit-potli-ivory.png."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
P = "assets/kit-potli-ivory.png"
IT = ["u-turmeric", "u-chilli-powder", "u-garam-masala", "u-cumin-seeds", "u-coriander-seeds", "u-sambar-masala-8002",
      "u-himalayan-pink-salt", "u-chia-seeds", "u-methi-seeds", "u-mustard-seeds"]
KICK = "Healthy Grocery Kit &middot; made to order"
H = "Build your own kit"
D = "Pick only the masalas and staples your kitchen uses, in the size you need. Our Sahelis pack it fresh, just for you."
SIZES = '<div class="sz"><span>100 g</span><span>200 g</span><span>500 g</span></div>'
BTN = '<a class="btn">Customise your kit <i>&rarr;</i></a>'

def copy(extra="", btn=BTN, kick=KICK, h=H, d=D):
    return '<div class="cp"><p class="k">%s</p><h3>%s</h3><p class="d">%s</p>%s%s</div>' % (kick, h, d, extra, btn)

def pot(cls="", style=""):
    return '<img class="pot %s" src="%s" alt="" style="%s">' % (cls, P, style)

def circ(img, x, y, s, cls=""):
    return '<span class="ci %s" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx"><img src="assets/%s.jpg" alt=""></span>' % (cls, x, y, s, s, img)

V = []
V.append(("Now, tidied", "Today's layout, cleaned up: the potli on ivory, the size chips added under the line.",
  "lt", '<div class="half ivory">' + pot("c") + '<span class="note">Your kit,<br>your way</span></div>' + copy(SIZES)))
V.append(("Potli with ingredients", "Little spice circles tumbling round the potli - what you can put in.",
  "lt", '<div class="half ivory">' + pot("c sm") + "".join(circ(IT[i], x, y, 46) for i, (x, y) in enumerate([(18, 40), (200, 30), (14, 250), (210, 260), (110, 330)])) + '</div>' + copy(SIZES)))
V.append(("Deep green", "Brand green block, cream words, gold button - the potli glows on the left.",
  "dk", '<div class="half glow">' + pot("c") + '</div>' + copy(SIZES), "background:radial-gradient(90% 120% at 20% 50%,#2d5236,#15261a)"))
V.append(("Step by step", "Three numbered steps: pick masalas, choose size, send on WhatsApp.",
  "lt", '<div class="half ivory">' + pot("c") + '</div>' + copy('<ol class="steps"><li><b>1</b>Pick your masalas</li><li><b>2</b>Choose 100 / 200 / 500 g</li><li><b>3</b>Send the list on WhatsApp</li></ol>', d="")))
V.append(("Potli on the right", "Words first, potli on the right, a soft peach ground.",
  "lt", copy(SIZES) + '<div class="half ivory r">' + pot("c") + '</div>', "background:#fbeee7"))
V.append(("Arch window", "The potli standing in a tall ivory arch, like the site's other arches.",
  "lt", '<div class="half"><div class="arch">' + pot("c sm") + '</div></div>' + copy(SIZES)))
V.append(("Pick-list card", "A little order card with ticked items and sizes - shows what the result looks like.",
  "lt", '<div class="half ivory">' + pot("c sm2", "top:30px") + '<div class="slip"><p>My kit</p><ul><li>Turmeric <b>200 g</b></li><li>Garam Masala <b>100 g</b></li><li>Sambar Masala <b>100 g</b></li><li>Pink Salt <b>500 g</b></li></ul></div></div>' + copy(SIZES)))
V.append(("Kraft and twine", "Kraft-paper ground with a twine line - homemade, handmade.",
  "lt kraft", '<div class="half">' + pot("c") + '<span class="twine"></span></div>' + copy(SIZES), "background:#e9d3ad"))
V.append(("Big type", "A huge 'Your kit, your way' behind the words, the potli breaking out of the corner.",
  "lt", '<div class="bigt">Your kit,<br>your way</div>' + pot("corner") + copy(SIZES), "background:#fdf6ee"))
V.append(("Gold frame", "Ivory card with a fine gold frame - the premium one.",
  "lt", '<div class="gf"></div><div class="half">' + pot("c") + '</div>' + copy(SIZES), "background:linear-gradient(160deg,#fffaf0,#f3e5c8)"))
V.append(("Ingredient strip", "A row of ingredient photos along the foot, potli above.",
  "lt", '<div class="half ivory">' + pot("c sm", "top:20px") + '</div>' + copy(SIZES) + '<div class="strip">' + "".join('<span><img src="assets/%s.jpg" alt=""></span>' % i for i in IT[:8]) + '</div>'))
V.append(("Saheli touch", "The 'Packed by Satva Sahelis' sticker on the potli - it's their kit.",
  "lt", '<div class="half ivory">' + pot("c") + '<div class="stamp"><img src="assets/saheli-mark-bright.svg" alt=""><b>Packed by<br>Satva Sahelis</b></div></div>' + copy(SIZES), "background:#fbeee7"))
V.append(("Terracotta", "Warm terracotta block, cream words, potli on an ivory circle.",
  "dk", '<div class="half"><div class="disc">' + pot("c sm") + '</div></div>' + copy(SIZES), "background:linear-gradient(150deg,#c06a48,#9c4a2e)"))
V.append(("Centred", "Everything centred: potli on top, words and button below - calm and simple.",
  "lt ctr", pot("top") + copy(SIZES), "background:radial-gradient(80% 80% at 50% 30%,#fffaf0,#f6e6da)"))
V.append(("Price hint", "A gold badge 'from &#8377;__' on the potli, for when you set prices.",
  "lt", '<div class="half ivory">' + pot("c") + '<div class="price">from<b>&#8377;__</b></div></div>' + copy(SIZES)))

figs = []
for i, v in enumerate(V, 1):
    n, cap, cls, inner = v[:4]
    bg = v[4] if len(v) > 4 else "background:linear-gradient(135deg,#fdf1ea,#f6dccf)"
    figs.append('<figure><div class="blk %s" style="%s">%s</div><figcaption><b>%02d</b> <strong>%s</strong> &mdash; %s</figcaption></figure>' % (cls, bg, inner, i, n, cap))

CSS = r"""*{box-sizing:border-box;margin:0;padding:0}
body{background:#1e1f1b;color:#f4efe6;font-family:"Jost",system-ui,sans-serif;padding:0 16px 70px}
header{max-width:1400px;margin:0 auto;padding:36px 0 10px}
header .k0{letter-spacing:.28em;text-transform:uppercase;font-size:.78rem;color:#e9cf98}
header h1{font-family:"Fraunces",serif;font-weight:600;font-size:clamp(1.8rem,3.4vw,2.7rem);margin:8px 0}
header p{color:#c9bfb0;max-width:80ch;line-height:1.6} header a{color:#e9cf98}
.grid{max-width:1400px;margin:30px auto 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(600px,1fr));gap:36px 26px;justify-items:center}
figcaption{margin-top:10px;color:#d9cfbf;font-size:.95rem;line-height:1.45;width:600px}
figcaption b{color:#e9cf98;font-family:"Fraunces",serif;font-size:1.1rem;margin-right:6px}figcaption strong{color:#f4efe6}
.blk{position:relative;width:600px;height:400px;border-radius:22px;overflow:hidden;display:flex;align-items:stretch;border:1px solid rgba(160,90,70,.18)}
.half{position:relative;flex:0 0 44%}
.half.ivory{background:radial-gradient(70% 70% at 50% 55%,#fffaf0,#f1e4c8)}
.half.glow{background:radial-gradient(60% 60% at 50% 55%,rgba(255,226,170,.35),transparent 70%)}
.pot{position:absolute;filter:drop-shadow(0 14px 14px rgba(60,30,20,.3))}
.pot.c{left:8%;top:8%;width:84%}
.pot.c.sm{left:20%;top:16%;width:60%}
.pot.c.sm2{left:24%;width:52%}
.pot.corner{right:-30px;bottom:-40px;width:270px;z-index:1}
.pot.top{position:relative;display:block;width:150px;margin:18px auto 0}
.cp{flex:1;display:flex;flex-direction:column;justify-content:center;padding:28px 30px;position:relative;z-index:2}
.cp .k{font:500 10.5px/1.4 "Jost";letter-spacing:.22em;text-transform:uppercase;color:#a0442e}
.cp h3{font:600 32px/1.05 "Fraunces",serif;color:#1f3a26;margin:8px 0}
.cp .d{font:300 14px/1.5 "Jost";color:#4a3f38}
.btn{align-self:flex-start;display:inline-flex;gap:10px;align-items:center;margin-top:16px;padding:13px 22px;border-radius:999px;background:linear-gradient(160deg,#f7dc96,#e0a51a 45%,#a8760f);color:#1e2c16;font:600 14px/1 "Jost";box-shadow:0 12px 22px -14px rgba(120,80,10,.8)}
.btn i{font-style:normal}
.sz{display:flex;gap:6px;margin-top:12px}
.sz span{padding:5px 10px;border-radius:99px;border:1.2px solid #1f3a26;font:600 11.5px/1 "Jost";color:#1f3a26;background:#fffaf4}
.dk .cp .k{color:#e9cf98}.dk .cp h3{color:#f6f1e6}.dk .cp .d{color:#e4d9c5}.dk .sz span{border-color:#e9cf98;color:#f6f1e6;background:transparent}
.note{position:absolute;left:14px;bottom:14px;padding:8px 12px;border-radius:12px;background:#fffaf4;color:#8f3a4c;font:600 13px/1.2 "Fraunces",serif;transform:rotate(-4deg);box-shadow:0 10px 18px -12px rgba(0,0,0,.5)}
.ci{position:absolute;border-radius:50%;overflow:hidden;border:3px solid #fffaf4;box-shadow:0 8px 14px -8px rgba(60,30,20,.6);z-index:2}
.ci img{width:100%;height:100%;object-fit:cover}
.steps{list-style:none;margin-top:12px;display:flex;flex-direction:column;gap:8px}
.steps li{display:flex;align-items:center;gap:10px;font:500 13.5px/1.2 "Jost";color:#1f3a26}
.steps b{display:grid;place-items:center;width:24px;height:24px;border-radius:50%;background:#1f3a26;color:#f6f1e6;font:600 12px/1 "Fraunces",serif}
.half.r{order:2}
.arch{position:absolute;left:24px;right:24px;top:24px;bottom:0;border-radius:120px 120px 0 0;background:linear-gradient(180deg,#fffaf0,#f1e4c8);box-shadow:inset 0 0 0 1.5px #d9b45a}
.slip{position:absolute;left:24px;right:24px;bottom:22px;background:#fffdf8;border-radius:12px;padding:10px 12px;box-shadow:0 14px 24px -14px rgba(60,30,20,.5);border:1px dashed #c9a14a}
.slip p{font:600 12px/1 "Fraunces",serif;color:#1f3a26;margin-bottom:6px}
.slip ul{list-style:none;font:400 11px/1.6 "Jost";color:#3c3330}.slip li{display:flex;justify-content:space-between}.slip li::before{content:"\2713";color:#25a35a;margin-right:6px}
.slip li b{margin-left:auto;font-weight:600}
.twine{position:absolute;left:0;right:-40%;top:40px;height:2px;background:repeating-linear-gradient(90deg,#8a6a3a 0 6px,transparent 6px 9px);transform:rotate(-4deg)}
.kraft{background-image:radial-gradient(rgba(90,60,25,.12) .8px,transparent 1.2px)!important;background-size:5px 5px!important}
.blk:has(.bigt) .cp{flex:0 0 66%}
.bigt{position:absolute;right:-10px;top:10px;font:700 84px/.9 "Fraunces",serif;color:rgba(166,71,91,.09);text-align:right;z-index:0}
.gf{position:absolute;inset:10px;border:1px solid rgba(201,150,42,.6);border-radius:14px;pointer-events:none;z-index:3}
.strip{position:absolute;left:0;right:0;bottom:0;height:56px;display:flex;gap:6px;padding:6px 10px;background:rgba(255,250,244,.85);z-index:3}
.strip span{flex:1;border-radius:10px;overflow:hidden}.strip img{width:100%;height:100%;object-fit:cover}
.blk:has(.strip) .half,.blk:has(.strip) .cp{padding-bottom:62px}
.blk:has(.strip) .pot.c.sm{top:10px;width:64%;left:18%}
.stamp{position:absolute;right:10px;bottom:16px;width:96px;height:96px;border-radius:50%;background:#fffaf4;border:2px dashed #c98d84;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;transform:rotate(-10deg);box-shadow:0 10px 18px -10px rgba(0,0,0,.5)}
.stamp img{width:30px}.stamp b{font:600 9px/1.15 "Jost";letter-spacing:.04em;text-transform:uppercase;color:#8f3a4c;margin-top:3px}
.disc{position:absolute;left:24px;top:50%;transform:translateY(-50%);width:210px;height:210px;border-radius:50%;background:radial-gradient(circle,#fffaf0,#f1e4c8)}
.disc .pot.c.sm{left:16%;top:10%;width:68%}
.ctr{flex-direction:column;align-items:center}.ctr .cp{align-items:center;text-align:center;padding-top:6px}.ctr .btn{align-self:center}.ctr .cp h3{font-size:28px}.ctr .sz{justify-content:center}
.price{position:absolute;right:14px;top:18px;width:72px;height:72px;border-radius:50%;background:linear-gradient(160deg,#f7dc96,#d9a73a);color:#1e2c16;display:flex;flex-direction:column;align-items:center;justify-content:center;font:500 10px/1 "Jost";box-shadow:0 10px 18px -10px rgba(120,80,10,.7)}
.price b{font:700 18px/1 "Fraunces",serif;margin-top:3px}"""
page = """<!DOCTYPE html><html lang="en">
<!-- 16 Oct 2026. Owner: variations for the "Build your own kit" block, at least 15.
     Review page only, noindex. Generated by kit-custom-variations.gen.py. -->
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Build Your Kit Options</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>%s</style></head><body>
<header><p class="k0">DS Satva &middot; Our Range</p><h1>&ldquo;Build your own kit&rdquo; &mdash; 15 designs</h1>
<p>Each is the block at the size it shows on your screen, with the ivory potli. Tell me the number you like. <a href="index.html#range">Back to the site</a></p></header>
<div class="grid">%s</div></body></html>""" % (CSS, "".join(figs))
open(os.path.join(HERE, "kit-custom-variations.html"), "w").write(page)
print("ok")
