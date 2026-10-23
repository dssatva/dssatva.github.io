#!/usr/bin/env python3
"""Generates ~/dssatva/ports/8002/why-bg-variations.html - 15 backgrounds
for the Why SATVA hero slide, arches (option 2) unchanged."""
import os, urllib.parse
SP = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.expanduser("~/dssatva/ports/8002/why-bg-variations.html")
AR = open(os.path.join(SP, "why-bg-variations.arches.html") if os.path.exists(os.path.join(SP, "why-bg-variations.arches.html")) else os.path.join(SP, "arches.html")).read()

def svg_uri(svg):
    return "url(\"data:image/svg+xml," + urllib.parse.quote(svg) + "\")"

NOISE = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" width="220" height="220"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 .35  0 0 0 0 .25  0 0 0 0 .1  0 0 0 .22 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>')
FIBRE = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".012 .6" numOctaves="2"/><feColorMatrix values="0 0 0 0 .4  0 0 0 0 .27  0 0 0 0 .1  0 0 0 .28 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>')
LEAVES = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" fill="none" stroke="#b5832a" stroke-opacity=".22" stroke-width="1.4" stroke-linecap="round"><path d="M30 88V46M30 76c10-1 18-8 20-18-10 1-18 8-20 18ZM30 66c-10-1-18-8-20-18 10 1 18 8 20 18ZM30 46c-3-4-3-9 0-12 3 3 3 8 0 12Z"/><circle cx="90" cy="30" r="4"/><circle cx="98" cy="40" r="3"/><circle cx="84" cy="42" r="3.5"/><path d="M80 96c6-10 18-10 24 0"/></svg>')
BLOCK = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" width="90" height="90" fill="none" stroke="#a8760f" stroke-opacity=".2" stroke-width="1.3"><path d="M45 15c10 8 10 22 0 30-10-8-10-22 0-30ZM45 75c10-8 10-22 0-30-10 8-10 22 0 30ZM15 45c8-10 22-10 30 0-8 10-22 10-30 0ZM75 45c-8 10-22 10-30 0 8-10 22-10 30 0Z"/><circle cx="45" cy="45" r="4"/><circle cx="0" cy="0" r="6"/><circle cx="90" cy="0" r="6"/><circle cx="0" cy="90" r="6"/><circle cx="90" cy="90" r="6"/></svg>')
JUTE = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12"><rect width="12" height="12" fill="#e6d3b1"/><path d="M0 3h12M0 9h12" stroke="#cdb48a" stroke-width="2.2"/><path d="M3 0v12M9 0v12" stroke="#d8c29c" stroke-width="1.6"/></svg>')
COLONNADE = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" width="1245" height="465" viewBox="0 0 1245 465"><g fill="#e9dfc6">' +
    "".join('<path d="M%d 465V170a75 75 0 0 1 150 0V465Z"/>' % (x) for x in range(-40, 1245, 190)) + '</g></svg>')
MANDALA = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" width="700" height="700" viewBox="-350 -350 700 700" fill="none" stroke="#c99a3a" stroke-opacity=".28" stroke-width="1.5">' +
    "".join('<circle r="%d"/>' % r for r in (60, 120, 200, 290)) +
    "".join('<ellipse rx="40" ry="150" transform="rotate(%d)"/>' % a for a in range(0, 180, 15)) + '</svg>')

# (key, caption, css for .st, extra html behind, light heading?)
V = [
 ("v0", "<b>Now</b> The current plain cream, for comparison", "background:#f3efe2", "", False),
 ("v1", "Warm paper: the cream with a fine paper grain, so it feels printed rather than flat",
  "background:%s,linear-gradient(180deg,#f6f0e2,#ece2cc)" % NOISE, "", False),
 ("v2", "Gold glow: a soft sunlit halo behind the heading, fading to cream at the edges",
  "background:radial-gradient(60% 75% at 50% 18%,#fbe7b4 0%,#f6ecd6 45%,#efe5cf 100%)", "", False),
 ("v3", "Forest green: deep brand green, heading in cream - the photo arches glow against it",
  "background:radial-gradient(120% 140% at 50% 0%,#2d5236,#15261a)", "", True),
 ("v4", "Blurred spices: the spice photograph softly out of focus under a cream wash",
  "background:#f3efe2", '<img class="bgp" src="assets/hero-2.jpg" alt="" style="filter:blur(14px) saturate(1.1);opacity:.4;transform:scale(1.1)">', False),
 ("v5", "Kraft paper: brown-paper fibres, like the kit bag",
  "background:%s,linear-gradient(170deg,#e4cfa8,#d6bb8c)" % FIBRE, "", False),
 ("v6", "Terracotta wall: warm clay, like a sun-baked village wall",
  "background:%s,linear-gradient(170deg,#e9b996,#d79a74)" % NOISE, "", False),
 ("v7", "Stage: cream above, a deep green band behind the foot of the arches",
  "background:linear-gradient(180deg,#f3efe2 0 58%,#1f3a26 58% 100%)", "", False),
 ("v8", "Line-drawn spices: a faint repeat of leaves and seeds in gold on cream",
  "background:%s,#f4eee0" % LEAVES, "", False),
 ("v9", "Jute weave: the texture of a jute sack, kept very soft",
  "background:%s" % JUTE, '<div class="wash" style="background:rgba(246,239,224,.55)"></div>', False),
 ("v10", "Dark slate: the dark stone photograph, heading in cream - most dramatic",
  "background:#121612", '<img class="bgp" src="assets/hero-dark-slate.jpg" alt="" style="filter:brightness(.42) saturate(.9)">', True),
 ("v11", "Sunrise: blush at the top melting into turmeric gold at the bottom",
  "background:linear-gradient(180deg,#fbe9e1 0%,#f8dcb4 55%,#f1c779 100%)", "", False),
 ("v12", "Block print: a quiet Indian block-print motif in gold, like a printed cloth",
  "background:%s,#f5eedf" % BLOCK, "", False),
 ("v13", "Colonnade: tall arch shapes in a shade darker, echoing the four arches",
  "background:%s center bottom/cover no-repeat,#f3ecdb" % COLONNADE, "", False),
 ("v14", "Turmeric field: the field photograph faded under cream, heading still dark",
  "background:#f3efe2", '<img class="bgp" src="assets/hero-spices-turmeric-field.jpg" alt="" style="opacity:.28;filter:saturate(.8)">', False),
 ("v15", "Mandala: a large faint gold mandala centred behind the arches",
  "background:%s center 60%%/760px no-repeat,radial-gradient(70%% 90%% at 50%% 50%%,#fbf5e6,#efe4cc)" % MANDALA, "", False),
]

figs = []
for key, cap, css, extra, light in V:
    num = cap.split("</b>")[0].replace("<b>", "") if cap.startswith("<b>") else "%02d" % int(key[1:])
    text = cap.split("</b> ")[1] if cap.startswith("<b>") else cap
    figs.append('<figure><div class="frame" tabindex="0" role="button" aria-label="Option %s, click for full size">'
                '<div class="st%s" style="%s">%s<div class="hd"><h2>Why choose SATVA</h2></div>%s</div></div>'
                '<figcaption><b>%s</b> %s</figcaption></figure>'
                % (num, " light" if light else "", css.replace('"', "'"), extra, AR, num, text))

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#22261e;color:#f4efe6;font-family:"Jost",system-ui,sans-serif;padding:0 16px 70px}
header{max-width:1400px;margin:0 auto;padding:36px 0 10px}
header .k0{letter-spacing:.28em;text-transform:uppercase;font-size:.78rem;color:#e9cf98}
header h1{font-family:"Fraunces",serif;font-weight:600;font-size:clamp(1.8rem,3.4vw,2.7rem);margin:8px 0}
header p{color:#c9bfb0;max-width:76ch;line-height:1.6} header a{color:#e9cf98}
.grid{max-width:1400px;margin:30px auto 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,620px),1fr));gap:34px 26px}
figcaption{margin-top:10px;color:#d9cfbf;font-size:.98rem;line-height:1.45}
figcaption b{color:#e9cf98;font-family:"Fraunces",serif;font-size:1.15rem;margin-right:6px}
.frame{position:relative;aspect-ratio:1245/465;overflow:hidden;border-radius:12px;cursor:zoom-in;outline:none}
.frame.full{position:fixed;inset:0;z-index:50;border-radius:0;aspect-ratio:auto;background:rgba(14,12,10,.92);cursor:zoom-out}
.st{position:absolute;left:0;top:0;width:1245px;height:465px;transform-origin:0 0;transform:scale(var(--s,.5));overflow:hidden;color:#1f3a26}
.frame.full .st{left:50%;top:50%;transform:translate(-50%,-50%) scale(var(--s))}
.st .bgp{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.st .wash{position:absolute;inset:0}
.st h2{font:600 40px/1.05 "Fraunces",serif;color:#1f3a26}
.st.light h2{color:#f4efe6}
.st .hd{position:absolute;left:0;right:0;top:34px;text-align:center;z-index:3}
/* the arches: option 2, exactly as on the site */
.st .ar{position:absolute;left:50px;right:50px;bottom:40px;height:310px;display:grid;grid-template-columns:repeat(4,1fr);gap:26px;z-index:3}
.st .a{position:relative;overflow:hidden;background:var(--c);color:var(--k);border-radius:50% 50% 20px 20px/44% 44% 20px 20px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;text-align:center;padding:30px 18px 30px;box-shadow:0 20px 34px -24px rgba(0,0,0,.6)}
.st .a img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.st .a::before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,color-mix(in srgb,var(--k) 25%,transparent),color-mix(in srgb,var(--k) 88%,black) 92%);z-index:1}
.st .ic{display:block;width:64px;height:64px;margin-bottom:12px;position:relative;z-index:2;color:#fff}
.st .ic svg{width:100%;height:100%}
.st h3{font:600 19px/1.18 "Fraunces",serif;color:#fff;max-width:14ch;position:relative;z-index:2}
"""
JS = """
function fit(){document.querySelectorAll('.frame').forEach(function(f){var full=f.classList.contains('full');
  f.style.setProperty('--s', full?Math.min(innerWidth/1245,innerHeight/465)*.96:f.clientWidth/1245);});}
addEventListener('resize',fit); fit();
document.querySelectorAll('.frame').forEach(function(f){
  function t(){var on=!f.classList.contains('full'); document.querySelectorAll('.frame.full').forEach(function(x){x.classList.remove('full')}); if(on)f.classList.add('full'); fit();}
  f.addEventListener('click',t); f.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();t();}});
});
addEventListener('keydown',function(e){if(e.key==='Escape'){document.querySelectorAll('.frame.full').forEach(function(x){x.classList.remove('full')});fit();}});
"""
html = """<!DOCTYPE html>
<html lang="en">
<!-- 14 Oct 2026. Owner, on the Why SATVA hero slide (photo arches, option 2):
     "can you show some background variations for this slider alone 15".
     Review page only - not linked, noindex. Arches and heading exactly as on
     the site; only the ground behind them changes. Each preview is the hero
     slide's real size at the owner's window (1245 x 465). Photographs are the
     site's own. Generated by why-bg-variations.gen.py beside this file. -->
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Why SATVA Backgrounds</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>%s</style>
</head>
<body>
<header>
  <p class="k0">DS Satva &middot; hero review</p>
  <h1>Why SATVA slide &mdash; 15 backgrounds</h1>
  <p>The four photo arches and the heading are exactly as they are on the site; only the background behind them changes. The first one is today&rsquo;s plain cream, for comparison. Click any slide to see it full size (click again or press Esc to come back). Tell me the number you like. <a href="index.html">Back to the site</a></p>
</header>
<div class="grid">
%s
</div>
<script>%s</script>
</body>
</html>
""" % (CSS, "\n".join(figs), JS)
open(OUT, "w").write(html)
print("wrote", OUT, len(html)//1024, "KB")
