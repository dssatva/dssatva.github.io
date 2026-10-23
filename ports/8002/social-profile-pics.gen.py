#!/usr/bin/env python3
"""Generates social-profile-pics.html - 15 profile pictures for DS Satva's
social media accounts. 21 Oct 2026. Every one is 1080x1080 and keeps the logo
inside the centre circle, so Instagram/WhatsApp/Facebook round crops never cut it.
Open social-profile-pics.html?only=N to see picture N alone at full size;
render-profile-pics.sh screenshots each one to social-profile-pics/NN.png."""
import json, os, html as H
HERE = os.path.dirname(os.path.abspath(__file__))
CR = {p["file"]: p for p in json.load(open(os.path.join(HERE, "masala-hero-photos/picked.json")))}

# The DS mark, as a solid shape in any colour (uses the PNG as a mask).
def solid(color, w=560):
    return ('<i class="m" style="width:%dpx;background:%s;-webkit-mask-image:url(assets/mark-dark.png);'
            'mask-image:url(assets/mark-dark.png)"></i>' % (w, color))
def mark(f, w=560):
    return '<img class="mk" src="assets/%s" style="width:%dpx" alt="">' % (f, w)
def ring_text(txt, color, r=430, size=46):
    return ('<svg class="rt" viewBox="0 0 1080 1080"><defs><path id="rp%%s" d="M540,540 m-%d,0 a%d,%d 0 1,1 %d,0 a%d,%d 0 1,1 -%d,0"/></defs>'
            '<text fill="%s" style="font:600 %dpx Jost;letter-spacing:.2em"><textPath href="#rp%%s" textLength="%d" lengthAdjust="spacing">%s</textPath></text></svg>'
            % (r, r, r, 2*r, r, r, 2*r, color, size, int(6.2832*r) - 40, H.escape(txt)))
RT = "DIL SE PURE · DS SATVA · PURE FROM HOME · DS SATVA · "

PICS = [
 ("Cream classic", "background:#f4f3e7", mark("mark-dark.png") + '<b class="ring" style="border-color:#bf8a17"></b>', ""),
 ("Forest green", "background:radial-gradient(circle at 50% 42%,#3c5128,#1e2c16 75%)", mark("mark-cream.png"), ""),
 ("Gold leaf", "background:radial-gradient(circle at 35% 30%,#f1ddab,#dfb459 45%,#bf8a17)", solid("#1e2c16"), ""),
 ("Night & gold glow", "background:radial-gradient(circle at 50% 50%,#3a3a22 0,#141c0e 70%)", mark("mark-cream.png") + '<b class="ring" style="border-color:#dfb459;opacity:.7"></b>', ""),
 ("Chilli red", "background:radial-gradient(circle at 50% 40%,#d5482a,#9c2410 80%)", solid("#fdf3e6"), ""),
 ("Turmeric", "background:radial-gradient(circle at 50% 40%,#f2c255,#e39a2a 80%)", solid("#2c4220"), ""),
 ("Full logo on cream", "background:#fdf3e6", mark("logo-stack-dark.png", 720), ""),
 ("Full logo on green", "background:#2c4220", mark("logo-stack-cream.png", 720), ""),
 ("Seal - cream", "background:#f4f3e7", mark("mark-dark.png", 470) + ring_text(RT, "#3c5128") + '<b class="ring" style="inset:150px;border-color:#bf8a17;border-width:4px"></b>', ""),
 ("Seal - green", "background:#2c4220", mark("mark-cream.png", 470) + ring_text(RT, "#dfb459") + '<b class="ring" style="inset:150px;border-color:#dfb459;border-width:4px"></b>', ""),
 ("Spice dots", "background:#efe7d5 url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='90' height='90'%3E%3Ccircle cx='15' cy='15' r='6' fill='%23bf8a17' opacity='.35'/%3E%3Ccircle cx='60' cy='55' r='4' fill='%23c3341a' opacity='.3'/%3E%3Ccircle cx='75' cy='20' r='3' fill='%234e6848' opacity='.35'/%3E%3C/svg%3E\")",
  '<b class="disc" style="background:#fff"></b>' + mark("mark-dark.png", 430), ""),
 ("Gold & green split", "background:linear-gradient(135deg,#dfb459 0 50%,#2c4220 50%)", '<b class="disc" style="background:#fdf3e6"></b>' + mark("mark-dark.png", 430), ""),
 ("Whole spices photo", "background:#222 url(assets/mas-hero-09.jpg) 50% 50%/cover", '<b class="disc" style="background:rgba(253,243,230,.94)"></b>' + mark("mark-dark.png", 430), "mas-hero-09.jpg"),
 ("Chilli fields photo", "background:url(assets/mas-hero-14.jpg) 55% 60%/auto 100%", '<b class="veil"></b>' + mark("mark-cream.png", 540), "mas-hero-14.jpg"),
 ("Satva Saheli", "background:radial-gradient(circle at 50% 45%,#fff 0,#fdf4f2 50%,#f6dcd3)", '<img class="mk" src="assets/saheli-mark-grad.svg" style="width:560px" alt="">', ""),
]

tiles = []
for i, (name, bg, inner, photo) in enumerate(PICS, 1):
    cr = ""
    if photo:
        p = CR[photo]
        cr = '<small>Photo: %s, %s &mdash; put &ldquo;Photo: %s (%s)&rdquo; in the bio if you use this one.</small>' % (
            H.escape(p["artist"]), p["lic"], H.escape(p["artist"]), p["lic"])
    tiles.append('<figure data-n="%d"><div class="pp" style="%s">%s</div>'
                 '<figcaption><b>%02d</b> %s <a href="social-profile-pics/%02d.png" download>PNG</a>%s</figcaption></figure>'
                 % (i, H.escape(bg, quote=True), inner, i, name, i, cr))

CSS = """*{box-sizing:border-box;margin:0;padding:0}
body{background:#1e1f1b;color:#f4efe6;font-family:"Jost",system-ui,sans-serif;padding:0 16px 70px}
header{max-width:1200px;margin:0 auto;padding:36px 0 10px}
header .k0{letter-spacing:.28em;text-transform:uppercase;font-size:.78rem;color:#e9cf98}
header h1{font-family:"Fraunces",serif;font-weight:600;font-size:clamp(1.8rem,3.4vw,2.7rem);margin:8px 0}
header p{color:#c9bfb0;max-width:80ch;line-height:1.6}
label{display:inline-flex;gap:8px;align-items:center;margin-top:12px;color:#e9cf98;cursor:pointer}
main{max-width:1200px;margin:26px auto 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:30px 24px}
figure{min-width:0}
.box{width:100%;aspect-ratio:1;overflow:hidden;border-radius:14px;position:relative}
.round .box{border-radius:50%}
.pp{width:1080px;height:1080px;position:absolute;left:0;top:0;transform-origin:0 0;display:grid;place-items:center;overflow:hidden}
.pp>*{grid-area:1/1}
.mk{display:block;height:auto;position:relative}
.m{display:block;aspect-ratio:607/512;-webkit-mask-size:contain;mask-size:contain;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;position:relative}
.ring{position:absolute;inset:70px;border:10px solid;border-radius:50%}
.disc{position:absolute;inset:170px;border-radius:50%;box-shadow:0 30px 60px -20px rgba(0,0,0,.45)}
.veil{position:absolute;inset:0;background:radial-gradient(circle at 50% 50%,rgba(20,28,14,.78) 0 36%,rgba(20,28,14,.45) 75%)}
.rt{position:absolute;inset:0;width:100%;height:100%}
figcaption{margin-top:10px;color:#d9cfbf;font-size:.98rem}
figcaption b{color:#e9cf98;font-family:"Fraunces",serif;font-size:1.15rem;margin-right:6px}
figcaption a{color:#e9cf98;margin-left:6px;font-size:.85rem}
figcaption small{display:block;color:#9d9586;margin-top:3px;font-size:.8rem}
body.only{padding:0;background:none} body.only header,body.only figcaption{display:none}
body.only main{display:block;margin:0;max-width:none} body.only figure{display:none}
body.only figure.on{display:block} body.only .box{width:1080px;height:1080px;border-radius:0}"""

JS = """const q=new URLSearchParams(location.search).get('only');
const fit=()=>document.querySelectorAll('.box').forEach(b=>{b.firstElementChild.style.transform=q?'none':'scale('+b.clientWidth/1080+')'});
document.querySelectorAll('.pp').forEach(p=>{const b=document.createElement('div');b.className='box';p.before(b);b.append(p)});
if(q){document.body.classList.add('only');const f=document.querySelector('figure[data-n="'+q+'"]');f&&f.classList.add('on')}
document.getElementById('rd').onchange=e=>document.body.classList.toggle('round',e.target.checked);
fit();addEventListener('resize',fit);
document.querySelectorAll('svg.rt').forEach((s,i)=>{s.querySelector('path').id='rp'+i;s.querySelector('textPath').setAttribute('href','#rp'+i)});"""

page = f"""<!DOCTYPE html>
<html lang="en">
<!-- 21 Oct 2026. Owner: "can create me 15 stunning great quality good pics for
     social media profiles". Review page only - not linked, noindex.
     Generated by social-profile-pics.gen.py. -->
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Social Profile Pictures</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<header><p class="k0">DS Satva &middot; Social media</p><h1>15 profile pictures</h1>
<p>Each one is a 1080&times;1080 PNG, sharp on every platform. The logo stays inside the centre circle, so Instagram, Facebook, WhatsApp, YouTube and LinkedIn can crop it round without cutting anything. Tick the box to see them as round profile pictures. Click <b>PNG</b> to download one.</p>
<label><input type="checkbox" id="rd"> Show as round profile pictures</label></header>
<main>{''.join(tiles)}</main>
<script>{JS}</script></body></html>"""
open(os.path.join(HERE, "social-profile-pics.html"), "w").write(page); print("ok")
