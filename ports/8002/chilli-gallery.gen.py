#!/usr/bin/env python3
"""Generates chilli-gallery.html - the chilli, chilli powder and dish photos
laid out as the site's "Something for every shelf" cards (photo, name on the
photo, arrow, description below, gold line). 20 Oct 2026. Photos: Unsplash
(free licence), assets/cg-*.jpg; credits in chilli-gallery-credits.json."""
import json, os, html as H
HERE = os.path.dirname(os.path.abspath(__file__))
CR = {m["file"]: m for m in json.load(open(os.path.join(HERE, "chilli-gallery-credits.json")))}
SECTIONS = [
 ("The chillies &amp; the powder", "From the sack to the spoon", [
  ("chilli-1.jpg", "Dried red chillies", "Sun-dried whole chillies, the start of every chilli powder we grind.", "Whole &middot; sun dried"),
  ("chilli-2.jpg", "Long, thin and hot", "Teja and Guntur chillies have this slim shape and sharp, strong heat.", "Teja &middot; 341"),
  ("chilli-4.jpg", "Wrinkled and deep red", "Wrinkled skin and a maroon colour, the look of a colour chilli like Byadgi.", "Byadgi &middot; Kashmiri"),
  ("powder-1.jpg", "Red chilli powder", "Ground with nothing added: no colour, no salt, no starch.", "Lal mirch"),
  ("powder-2.jpg", "Bright and even", "A clean, bright red that stays true when it hits hot oil.", "Pure &middot; single origin"),
  ("powder-4.jpg", "Deep red, gentle heat", "The deep red that Byadgi and Kashmiri bring to a gravy.", "Colour chilli")]),
 ("Hot chilli dishes", "Teja and 341: for food that should be spicy", [
  ("hot-1.jpg", "Andhra chicken curry", "Sharp Guntur heat, fried in oil with onion and ginger-garlic before the chicken goes in.", "Best with Teja"),
  ("hot-2.png", "Everyday chicken curry", "Half 341, half Byadgi: a red gravy that is hot, but not too hot for the family.", "Best with 341 + Byadgi"),
  ("hot-3.jpg", "Fish &amp; mutton curry", "A spoon of Teja lifts the heat; Byadgi keeps the gravy red.", "Best with Teja + Byadgi")]),
 ("Byadgi dishes", "Colour without burning the mouth", [
  ("byadgi-1.jpg", "Idli &amp; sambar", "Byadgi gives sambar its red-orange colour and mild warmth.", "Best with Byadgi"),
  ("byadgi-2.jpg", "Masala dosa", "The red chutney inside a Mysore masala dosa, and the colour of idli podi.", "Best with Byadgi"),
  ("byadgi-3.jpg", "Fish fry &amp; ghee roast", "A thick Byadgi paste gives the deep red coat on Mangalorean fish fry.", "Best with Byadgi")]),
 ("Kashmiri dishes", "The brightest red, almost no heat", [
  ("kash-1.jpg", "Butter chicken", "An orange-red gravy with no bite, so children enjoy it too.", "Best with Kashmiri"),
  ("kash-2.jpg", "Tandoori chicken", "Mixed into the curd marinade for the famous red, with no food dye.", "Best with Kashmiri"),
  ("kash-3.jpg", "Rogan josh", "A large spoon gives the deep red oil, the &ldquo;rogan&rdquo;, on top.", "Best with Kashmiri")]),
 ("Maharashtrian favourites", "What our neighbours cook every week", [
  ("maha-1.jpg", "Misal pav", "The red &ldquo;kat&rdquo; on top is chilli powder fried in oil: hot and bright.", "Best with 341 + Byadgi"),
  ("maha-2.jpg", "Vada pav", "The dry garlic chutney is garlic, coconut and a hot chilli powder.", "Best with Teja"),
  ("maha-3.jpg", "Pav bhaji", "Kashmiri or Byadgi gives the bright red bhaji everyone expects.", "Best with Kashmiri / Byadgi")]),
]
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13M12 5l7 7-7 7"/></svg>'
secs = []
for title, kick, cards in SECTIONS:
    cs = ""
    for f, name, blurb, meta in cards:
        m = CR[f]
        cs += (f'<article class="catcard"><div class="cshot"><img src="assets/cg-{f}" alt="{H.escape(m.get("desc") or m.get("alt") or "")}">'
               f'<span class="cscrim"></span><span class="cname">{name}</span><span class="carrow">{ARROW}</span></div>'
               f'<div class="cmeta"><p class="cblurb">{blurb}</p><p class="ccount">{meta}</p>'
               f'<p class="ccred">Photo: <a href="{m["page"]}" target="_blank" rel="noopener">{H.escape(m.get("u") or "")}</a> / Unsplash</p></div></article>')
    secs.append(f'<section class="cats"><div class="wrap"><div class="chead"><p class="kick">{kick}</p><h2 class="dsp">{title}</h2></div><div class="catgrid">{cs}</div></div></section>')
CSS = """:root{--ivory:#f4f3e7;--cream:#e8dcc6;--line:#e8ddc6;--ink:#1e2c16;--band:#3c5128;--sage:#4e6848;--gold-lt:#dfb459;--gold-dk:#7f5a0f;--ease:cubic-bezier(.22,1,.36,1)}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--cream);color:var(--ink);font-family:"Jost",system-ui,sans-serif}
.top{max-width:1240px;margin:0 auto;padding:34px 20px 0}
.top p{color:var(--sage);max-width:80ch;line-height:1.6;font-size:.95rem}.top a{color:var(--gold-dk)}
.cats{padding:46px 0 26px}.cats:nth-child(odd of section){background:var(--ivory)}
.wrap{max-width:1240px;margin:0 auto;padding:0 20px}
.chead{text-align:center;margin:0 auto 30px}
.kick{letter-spacing:.32em;text-transform:uppercase;font-size:.8rem;font-weight:600;color:var(--gold-dk)}
.dsp{font-family:"Fraunces",Georgia,serif;font-weight:600;font-size:clamp(1.6rem,2.6vw,2.2rem);margin-top:8px}
.catgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.catcard{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:20px;overflow:hidden;
 box-shadow:0 18px 38px -24px rgba(60,81,40,.45);transition:transform .55s var(--ease),box-shadow .55s var(--ease),border-color .55s var(--ease)}
.cshot{position:relative;height:clamp(260px,46vh,440px);overflow:hidden}
.cshot img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:saturate(1.12) contrast(1.03);transition:transform .8s var(--ease)}
.cscrim{position:absolute;left:0;right:0;bottom:0;height:46%;background:linear-gradient(to top,rgba(20,28,15,.92) 0%,rgba(20,28,15,.58) 45%,rgba(20,28,15,0) 100%)}
.cname{position:absolute;left:22px;right:70px;bottom:20px;font-family:"Fraunces",Georgia,serif;font-size:1.42rem;font-weight:600;color:#fff;line-height:1.15;text-shadow:0 1px 12px rgba(12,18,8,.55)}
.carrow{position:absolute;right:18px;bottom:16px;width:40px;height:40px;border-radius:50%;display:grid;place-items:center;background:rgba(255,255,255,.94);color:var(--band);transition:transform .45s var(--ease)}
.carrow svg{width:52%;height:52%}
.catcard:hover{transform:translateY(-7px);box-shadow:0 30px 52px -26px rgba(60,81,40,.55);border-color:var(--gold-lt)}
.catcard:hover .cshot img{transform:scale(1.055)}.catcard:hover .carrow{transform:translateX(3px)}
.cmeta{display:flex;flex-direction:column;gap:6px;flex:1;padding:15px 18px 16px}
.cblurb{font-size:.95rem;line-height:1.55;color:var(--sage)}
.ccount{margin-top:auto;padding-top:7px;font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-dk);font-weight:600}
.ccred{font-size:.7rem;color:#8a8a7a}.ccred a{color:inherit}
@media (max-width:900px){.catgrid{grid-template-columns:repeat(2,1fr)}}
@media (max-width:560px){.catgrid{grid-template-columns:1fr}.cshot{height:300px}}"""
page = f"""<!DOCTYPE html>
<html lang="en">
<!-- 20 Oct 2026. Owner: "i need a set of stunning pictures of the chilli and the
     powder and some description on what all we can use it for, the dishes" -
     then, pointing at the Something for every shelf cards: "i want the content
     to be in this order and some description below". Review page only - not
     linked, noindex. Generated by chilli-gallery.gen.py. -->
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Chilli Gallery</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500..700&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="top"><p class="kick">DS Satva &middot; chilli review</p><p>The chillies, the powder and the dishes each one is best for, in the same cards as the &ldquo;Something for every shelf&rdquo; section. All photos are from Unsplash, free to use, credited under each. <a href="index.html">Back to the site</a></p></div>
{''.join(secs)}</body></html>"""
open(os.path.join(HERE, "chilli-gallery.html"), "w").write(page); print("ok")
