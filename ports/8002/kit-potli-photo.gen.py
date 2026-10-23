#!/usr/bin/env python3
"""kit-potli-photo.html - the Grocery Kit slide (rotating orbit, as on the
site) with the rendered product-style potli (kit-potli-photo/render.py) in
12 colour combinations. 15 Oct 2026."""
import json, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
L = json.load(open(os.path.join(HERE, "kit-potli-photo", "list.json")))
ITEMS = ["u-turmeric","u-chilli-powder","u-mustard-seeds","u-cumin-seeds","u-coriander-seeds","u-garam-masala",
         "u-sambar-masala-8002","u-chatpat-masala","u-himalayan-pink-salt","u-coconut-sugar","u-chia-seeds","u-methi-seeds","j-monk-3-powder"]
ring = "".join('<span class="orb" style="--a:%.3frad"><span class="it"><img src="assets/%s.jpg" alt=""></span></span>' % (-math.pi/2 + i*2*math.pi/13, im) for i, im in enumerate(ITEMS))
figs = []
for i, c in enumerate(L, 1):
    figs.append(f'''<figure><div class="frame" tabindex="0" role="button"><div class="st" style="--ring:{c['ring']};--acc:{c['acc']};background:radial-gradient(80% 90% at 70% 50%,{c['bg'][0]},{c['bg'][1]})">
<div class="cp"><p class="k">New &middot; one box, whole kitchen</p><h2>Healthy Grocery Kit<em>Your Kitchen, Sorted</em></h2>
<p class="d">Thirteen everyday essentials in one box &mdash; the spices, home-made masalas, salt, sweeteners and seeds a kitchen goes through every week, all pure and packed by SATVA.</p>
<a class="pl">Order the kit on WhatsApp<i>&rarr;</i></a></div>
<div class="orbit"><div class="ring">{ring}</div><div class="sh"></div><img class="pt" src="kit-potli-photo/{c['file']}" alt="">
<div class="tg"><i></i><b>Healthy Grocery Kit</b></div>
<div class="stp"><img src="assets/saheli-mark-bright.svg" alt=""><b>Packed by<br>Satva Sahelis</b></div></div>
</div></div><figcaption><b>{i:02d}</b> <strong>{c['name']}</strong></figcaption></figure>''')
CSS = """*{box-sizing:border-box;margin:0;padding:0}
body{background:#1e1f1b;color:#f4efe6;font-family:"Jost",system-ui,sans-serif;padding:0 16px 70px}
header{max-width:1400px;margin:0 auto;padding:36px 0 10px}
header .k0{letter-spacing:.28em;text-transform:uppercase;font-size:.78rem;color:#e9cf98}
header h1{font-family:"Fraunces",serif;font-weight:600;font-size:clamp(1.8rem,3.4vw,2.7rem);margin:8px 0}
header p{color:#c9bfb0;max-width:80ch;line-height:1.6} header a{color:#e9cf98}
.grid{max-width:1400px;margin:30px auto 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,620px),1fr));gap:34px 26px}
figcaption{margin-top:10px;color:#d9cfbf;font-size:1rem}figcaption b{color:#e9cf98;font-family:"Fraunces",serif;font-size:1.15rem;margin-right:6px}figcaption strong{color:#f4efe6}
.frame{position:relative;aspect-ratio:1245/464;overflow:hidden;border-radius:12px;cursor:zoom-in;outline:none}
.frame.full{position:fixed;inset:0;z-index:50;border-radius:0;aspect-ratio:auto;background:rgba(14,12,10,.92);cursor:zoom-out}
.st{position:absolute;left:0;top:0;width:1245px;height:464px;transform-origin:0 0;transform:scale(var(--s,.5));overflow:hidden}
.frame.full .st{left:50%;top:50%;transform:translate(-50%,-50%) scale(var(--s))}
.cp{position:absolute;left:50px;top:50%;transform:translateY(-50%);width:470px;z-index:5}
.cp .k{font:500 13px/1.3 "Jost";letter-spacing:.32em;text-transform:uppercase;color:var(--acc)}
.cp h2{font:600 46px/1.04 "Fraunces",serif;margin:14px 0;color:#1f3a26}.cp h2 em{display:block;font-style:normal;color:var(--acc)}
.cp .d{font:300 16px/1.55 "Jost";color:#4a4040;max-width:46ch}
.cp .pl{display:inline-flex;align-items:center;gap:16px;margin-top:22px;padding:13px 14px 13px 26px;border-radius:999px;background:#1f3a26;color:#fbf1ec;font:500 13px/1 "Jost";letter-spacing:.14em;text-transform:uppercase}
.cp .pl i{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:#fbf1ec;color:#1f3a26;font-style:normal}
.orbit{position:absolute;right:52px;top:6px;width:452px;height:452px;container-type:inline-size}
.ring{position:absolute;left:50%;top:50%;width:0;height:0;animation:spin 70s linear infinite}
.ring::before{content:"";position:absolute;left:-40cqw;top:-40cqw;width:80cqw;height:80cqw;border-radius:50%;border:1.5px dashed var(--ring);opacity:.5}
.orb{position:absolute;left:0;top:0;transform:rotate(var(--a)) translate(40cqw) rotate(calc(-1 * var(--a)))}
.it{display:block;width:15cqw;height:15cqw;margin:-7.5cqw 0 0 -7.5cqw;border-radius:50%;overflow:hidden;border:.9cqw solid #fffaf4;box-shadow:0 2cqw 4cqw -2cqw rgba(60,30,20,.6);animation:spin 70s linear infinite reverse}
.it img{width:100%;height:100%;object-fit:cover;display:block}
@keyframes spin{to{transform:rotate(360deg)}}
.sh{position:absolute;left:27%;bottom:15%;width:46%;height:7cqw;border-radius:50%;background:radial-gradient(closest-side,rgba(60,30,20,.4),transparent)}
.pt{position:absolute;left:50%;top:50%;width:54cqw;transform:translate(-50%,-53%);filter:drop-shadow(0 3cqw 3cqw rgba(60,30,20,.28))}
.tg{position:absolute;left:66%;top:45%;width:14cqw;padding:3cqw 1cqw 2cqw;background:#e3c595;border-radius:4px 4px 10px 10px;text-align:center;transform:rotate(-8deg);box-shadow:0 2cqw 3cqw -1.5cqw rgba(0,0,0,.5);clip-path:polygon(18% 0,82% 0,100% 14%,100% 100%,0 100%,0 14%)}
.tg i{position:absolute;left:50%;top:6%;width:1.4cqw;height:1.4cqw;margin-left:-.7cqw;border-radius:50%;background:#6b4a14}
.tg b{display:block;font:600 2.7cqw/1.08 "Fraunces",serif;color:#3a2a14}
.stp{position:absolute;left:-15%;bottom:9%;width:22cqw;aspect-ratio:1;border-radius:50%;background:#fffaf4;border:2px dashed #c98d84;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;transform:rotate(-10deg);box-shadow:0 2.5cqw 5cqw -2.5cqw rgba(60,30,20,.6)}
.stp img{width:34%}.stp b{font:600 2.35cqw/1.15 "Jost";letter-spacing:.04em;text-transform:uppercase;color:#8f3a4c;margin-top:.8cqw;white-space:nowrap}"""
JS = """function fit(){document.querySelectorAll('.frame').forEach(function(f){var full=f.classList.contains('full');f.style.setProperty('--s',full?Math.min(innerWidth/1245,innerHeight/464)*.96:f.clientWidth/1245);});}
addEventListener('resize',fit);fit();document.querySelectorAll('.frame').forEach(function(f){f.addEventListener('click',function(){var on=!f.classList.contains('full');document.querySelectorAll('.frame.full').forEach(function(x){x.classList.remove('full')});if(on)f.classList.add('full');fit();});});
addEventListener('keydown',function(e){if(e.key==='Escape'){document.querySelectorAll('.frame.full').forEach(function(x){x.classList.remove('full')});fit();}});"""
page = f"""<!DOCTYPE html><html lang="en">
<!-- 15 Oct 2026. Owner: "i want the same rotating one. but the pic of the potli
     is not stunning. i just want colour variations in that and the potli to be
     professional and stunning". Review page only, noindex. Generated by
     kit-potli-photo.gen.py; potlis rendered by kit-potli-photo/render.py. -->
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Kit Potli Colours</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><header><p class="k0">DS Satva &middot; Grocery Kit slide</p><h1>The rotating kit &mdash; new potli, 12 colours</h1>
<p>The same rotating slide as on the site, with a new product-style potli (real cloth shading, gathered neck, twisted cord and tassels, the logo printed on the cloth) in twelve colour combinations. Click one for full size. Tell me the number. <a href="index.html">Back to the site</a></p></header>
<div class="grid">{''.join(figs)}</div><script>{JS}</script></body></html>"""
open(os.path.join(HERE, "kit-potli-photo.html"), "w").write(page); print("ok")
