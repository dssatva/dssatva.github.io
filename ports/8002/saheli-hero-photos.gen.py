#!/usr/bin/env python3
"""Generates ~/dssatva/ports/8002/saheli-hero-photos.html - 15 Commons photographs
for the Satva Saheli hero slide, each shown in the slide with its words."""
import json, os, html as H
HERE = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(HERE, "saheli-hero-photos", "picked.json")))
OUT = os.path.expanduser("~/dssatva/ports/8002/saheli-hero-photos.html")
NAMES = ["Cooking on the chulha", "Winnowing rice", "Breakfast in the village", "Chillies drying, from above",
         "Planting rice together", "Pride in the field", "A food mela", "Cooking side by side", "At the fire",
         "Two cooks, one hearth", "Sorting red chillies", "Smiles and determination", "Sorting the turmeric harvest",
         "The veiled cook", "Women at work in the field"]
POS = ["center 40%", "center 30%", "65% center", "center", "center 35%", "60% 30%", "center", "60% center", "70% center",
       "65% center", "center", "60% 35%", "center 40%", "60% center", "center 40%"]
figs = []
for i, p in enumerate(P):
    lic = H.escape(p["lic"]); art = H.escape(p["artist"] or "unknown")
    figs.append(f'''<figure><div class="frame" tabindex="0" role="button" aria-label="Option {i+1}, click for full size"><div class="st">
<img class="ph" src="assets/{p['file']}" alt="" style="object-position:{POS[i]}"><div class="scrim"></div>
<div class="cp"><div class="sl"><img src="assets/saheli-mark-bright.svg" alt=""><span><b>SATVA</b><i>SAHELI</i></span></div>
<h2>Empowering Women<em>Enriching <span>Kitchens</span></em></h2>
<p>Select masalas are roasted and blended at home by women using their own family recipes. Purity begins at home &mdash; the work and the wage stay with them.</p>
<div class="bt"><a class="pill">Meet Satva Saheli <span>&rarr;</span></a><a class="gold">Become a Saheli</a></div></div>
</div></div><figcaption><b>{i+1:02d}</b> <strong>{NAMES[i]}</strong> &mdash; {H.escape(p['desc'][:120])} <small>Photo: {art}, {lic}, <a href="{p['page']}" target="_blank" rel="noopener">Wikimedia Commons</a></small></figcaption></figure>''')
CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#1e1f1b;color:#f4efe6;font-family:"Jost",system-ui,sans-serif;padding:0 16px 70px}
header{max-width:1400px;margin:0 auto;padding:36px 0 10px}
header .k0{letter-spacing:.28em;text-transform:uppercase;font-size:.78rem;color:#e9cf98}
header h1{font-family:"Fraunces",serif;font-weight:600;font-size:clamp(1.8rem,3.4vw,2.7rem);margin:8px 0}
header p{color:#c9bfb0;max-width:80ch;line-height:1.6} header a,figcaption a{color:#e9cf98}
.grid{max-width:1400px;margin:30px auto 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,620px),1fr));gap:34px 26px}
figcaption{margin-top:10px;color:#d9cfbf;font-size:.95rem;line-height:1.45}
figcaption b{color:#e9cf98;font-family:"Fraunces",serif;font-size:1.15rem;margin-right:6px}
figcaption strong{color:#f4efe6}
figcaption small{display:block;color:#9d9586;margin-top:3px;font-size:.8rem}
.frame{position:relative;aspect-ratio:1245/464;overflow:hidden;border-radius:12px;cursor:zoom-in;outline:none}
.frame.full{position:fixed;inset:0;z-index:50;border-radius:0;aspect-ratio:auto;background:rgba(14,12,10,.92);cursor:zoom-out}
.st{position:absolute;left:0;top:0;width:1245px;height:464px;transform-origin:0 0;transform:scale(var(--s,.5));overflow:hidden;background:#0e120d}
.frame.full .st{left:50%;top:50%;transform:translate(-50%,-50%) scale(var(--s))}
.ph{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:saturate(1.08)}
.scrim{position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,13,9,.82) 0%,rgba(10,13,9,.72) 34%,rgba(10,13,9,.36) 58%,rgba(10,13,9,.08) 78%,rgba(10,13,9,0) 90%)}
.cp{position:absolute;left:50px;top:50%;transform:translateY(-50%);width:560px}
.sl{display:flex;align-items:center;gap:12px}.sl img{width:52px}
.sl span b{display:block;font:700 22px/1 "Fraunces",serif;color:#f4f3e7;letter-spacing:.06em}
.sl span i{display:block;font:500 12px/1 "Jost";letter-spacing:.5em;color:#f1ddab;font-style:normal;margin-top:5px}
h2{font:600 50px/1.04 "Fraunces",serif;color:#f4f3e7;margin:18px 0 14px}
h2 em{display:block;font-style:normal}h2 em span{color:#f1ddab}
.cp p{font:300 16.5px/1.55 "Jost";color:#e8dcc6;max-width:46ch}
.bt{display:flex;gap:14px;margin-top:22px;align-items:center}
.pill{padding:13px 22px;border-radius:999px;border:1.5px solid #e8dcc6;color:#f4f3e7;font:500 13px/1 "Jost";letter-spacing:.12em;text-transform:uppercase}
.pill span{display:inline-grid;place-items:center;width:30px;height:30px;margin:-8px -10px -8px 10px;border-radius:50%;background:#e8dcc6;color:#16200f}
.gold{padding:14px 24px;border-radius:999px;background:linear-gradient(160deg,#f7dc96,#e0a51a 42%,#a8760f);color:#1e2c16;font:600 15px/1 "Jost"}
"""
JS = """function fit(){document.querySelectorAll('.frame').forEach(function(f){var full=f.classList.contains('full');f.style.setProperty('--s',full?Math.min(innerWidth/1245,innerHeight/464)*.96:f.clientWidth/1245);});}
addEventListener('resize',fit);fit();
document.querySelectorAll('.frame').forEach(function(f){function t(){var on=!f.classList.contains('full');document.querySelectorAll('.frame.full').forEach(function(x){x.classList.remove('full')});if(on)f.classList.add('full');fit();}
f.addEventListener('click',t);f.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();t();}});});
addEventListener('keydown',function(e){if(e.key==='Escape'){document.querySelectorAll('.frame.full').forEach(function(x){x.classList.remove('full')});fit();}});"""
page = f"""<!DOCTYPE html>
<html lang="en">
<!-- 15 Oct 2026. Owner: "change this pic based on the content. give me some 15
     stunning pictures related to the content of empowering women, enriching
     kitchens to put it in the hero section". Review page only - not linked,
     noindex. Fifteen Wikimedia Commons photographs (free licences, credited
     under each), saved as assets/sah-hero-01..15.jpg, each shown in the
     Satva Saheli hero slide at the owner's screen size (1245 x 464).
     Generated by saheli-hero-photos.gen.py beside this file. -->
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Saheli Hero Photos</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>{CSS}</style></head>
<body><header><p class="k0">DS Satva &middot; hero review</p><h1>Satva Saheli slide &mdash; 15 photographs</h1>
<p>Real photographs of women cooking, winnowing, sorting spices and working together, each shown in the Satva Saheli slide with its words, at your screen size. All are free to use with credit (shown under each). Click one to see it full size (click again or press Esc). Tell me the number you like. <a href="index.html">Back to the site</a></p></header>
<div class="grid">{''.join(figs)}</div><script>{JS}</script></body></html>"""
open(OUT, "w").write(page); print("wrote", OUT)
