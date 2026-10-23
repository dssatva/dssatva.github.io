#!/usr/bin/env python3
"""Generates ~/dssatva/ports/8002/kit-hero-stunning.html - 15 bolder designs
for the Grocery Kit hero slide (1245 x 464 at the owner's window). The potli:
rose weave, no white band, tag "Healthy Grocery Kit", stamp "Packed by Satva
Sahelis". The slide's own words."""
import os, math
HERE = os.path.dirname(os.path.abspath(__file__))
_P = os.path.join(HERE, "genpotli.py") if os.path.exists(os.path.join(HERE, "genpotli.py")) else os.path.join(HERE, "kit-potli-variations.gen.py")
_src = open(_P).read().replace('open(OUT, "w").write(html)', 'pass')
for k in ("LIGHT", "DIFF", "MIX", "ONE"):
    os.environ.pop(k, None)
G = {"__file__": os.path.join(HERE, "genpotli.py")}
exec(compile(_src, "genpotli", "exec"), G)
ROSE = dict(G["P_MIX"][1][4]); ROSE["trim"] = None; ROSE["trim2"] = None
CREAM = dict(ROSE, cloth="#f4ead6", shade="#e2d5bd", pc="#dccdb0", pc2="#cfbe9c")
GREEN = dict(ROSE, cloth="#2f5238", shade="#223d29", pc="#3c6346", pc2="#284a31", cord="#d9b45a", cord2="#8a6510", tassel="#d9b45a")
OUT = os.path.expanduser("~/dssatva/ports/8002/kit-hero-stunning.html")
W, H = 1245, 464
ITEMS = ["u-turmeric", "u-chilli-powder", "u-mustard-seeds", "u-cumin-seeds", "u-coriander-seeds", "u-garam-masala",
         "u-sambar-masala-8002", "u-chatpat-masala", "u-himalayan-pink-salt", "u-coconut-sugar", "u-chia-seeds",
         "u-methi-seeds", "j-monk-3-powder"]
_n = [0]

def potli(w, left, bottom, cloth=None, tag=True, stamp=None, letters="#3d4529", glow=False, z=4, cream_lk=False):
    _n[0] += 1
    u = "s%d" % _n[0]
    svg = G["potli"](u, **(cloth or ROSE))
    h = w * 470 / 400
    mark = "mark-cream.png" if cream_lk else "mark-dark.png"
    lk = ('<div class="lk%s" style="--lc:%s"><img class="lk-m" src="assets/%s" alt=""><b>SATVA</b>'
          '<span><img src="assets/kit-sprig-l.png" alt=""><i>Dil Se Pure</i><img src="assets/kit-sprig-r.png" alt=""></span></div>'
          % (" cr" if cream_lk else "", letters, mark))
    tg = '<div class="tg"><i></i><b>Healthy Grocery Kit</b></div>' if tag else ''
    st = ''
    if stamp:
        st = ('<div class="stp" style="%s"><img src="assets/saheli-mark-bright.svg" alt=""><b>Packed by<br>Satva Sahelis</b></div>' % stamp)
    gl = '<div class="glow"></div>' if glow else ''
    return ('<div class="pt" style="left:%dpx;bottom:%dpx;width:%dpx;height:%dpx;z-index:%d">%s%s%s%s%s</div>'
            % (left, bottom, w, h, z, gl, svg.replace("\n", ""), lk, tg, st))

def sh(cx, bottom, w, dark=False):
    return '<div class="sh%s" style="left:%dpx;bottom:%dpx;width:%dpx"></div>' % (" dk" if dark else "", cx - w // 2, bottom, w)

def it(img, x, y, s, cls=""):
    return '<span class="it %s" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx"><img src="assets/%s.jpg" alt=""></span>' % (cls, x - s // 2, y - s // 2, s, s, img)

def copy(theme, x=50, w=470, kick="New &middot; one box, whole kitchen", h1="Healthy Grocery Kit", h2="Your Kitchen, <span>Sorted</span>",
         d="Thirteen everyday essentials in one box &mdash; the spices, home-made masalas, salt, sweeteners and seeds a kitchen goes through every week, all pure and packed by SATVA.",
         btn="Order the kit on WhatsApp", extra=""):
    return ('<div class="cp %s" style="left:%dpx;width:%dpx"><p class="k">%s</p><h2>%s<em>%s</em></h2><p class="d">%s</p>%s'
            '<a class="pl">%s<i>&rarr;</i></a></div>' % (theme, x, w, kick, h1, h2, d, extra, btn))

def bgimg(f, pos="center", filt="", extra_style=""):
    return '<img class="bgi" src="assets/%s" alt="" style="object-position:%s;%s%s">' % (f, pos, ("filter:%s;" % filt) if filt else "", extra_style)

V = []
# 01 dabba
V.append(("Masala dabba", "The real masala dabba photograph full-bleed on the right, the potli glowing in front of it; words on deep green",
  "background:#16261b",
  bgimg("cat-blend.jpg", "center 40%", "saturate(1.1)", "left:auto;right:0;width:62%;") +
  '<div class="fade" style="background:linear-gradient(90deg,#16261b 0%,#16261b 38%,rgba(22,38,27,.85) 46%,rgba(22,38,27,0) 70%)"></div>' +
  copy("dk") + sh(905, 34, 300, True) + potli(310, 750, 40, glow=True, stamp="left:-30%;bottom:6%")))
# 02 spotlight
V.append(("Spotlight", "Pitch dark velvet with a single warm spotlight falling on the potli, gold dust floating in the beam",
  "background:radial-gradient(60% 90% at 72% 10%,#3a2f22 0%,#17130f 55%,#0c0a08 100%)",
  '<div class="beam" style="left:740px"></div>' + "".join('<i class="dust" style="left:%dpx;top:%dpx;animation-delay:%.1fs"></i>' % (780 + (i * 53) % 260, 40 + (i * 71) % 300, i * .37) for i in range(16)) +
  copy("dk gold") + sh(905, 30, 320, True) + potli(320, 745, 36, stamp="left:-28%;bottom:8%")))
# 03 spice spread
V.append(("Spice market spread", "The bright spice-bowl photograph across the whole slide, a soft cream veil on the left for the words, potli standing among the bowls",
  "background:#fbf6ee",
  bgimg("hero-2.jpg", "center 60%", "saturate(1.08)") +
  '<div class="fade" style="background:linear-gradient(90deg,rgba(251,246,238,.97) 0%,rgba(251,246,238,.93) 36%,rgba(251,246,238,.35) 56%,rgba(251,246,238,0) 70%)"></div>' +
  copy("lt") + sh(930, 24, 300) + potli(300, 780, 30, stamp="left:auto;right:-26%;bottom:62%")))
# 04 giant title behind
V.append(("Magazine cover", "A giant 'KIT' in rose behind the potli, the potli breaking in front of it - bold editorial type",
  "background:linear-gradient(180deg,#fdf3ee,#f3dcd3)",
  '<div class="giant">KIT</div>' + copy("lt", h2="Your Kitchen, <span>Sorted</span>") + sh(915, 22, 320) + potli(330, 750, 26, stamp="left:-30%;bottom:4%")))
# 05 gold sunburst on maroon
V.append(("Festive sunburst", "Deep maroon with gold rays bursting from behind the potli - festive, like a Diwali gift",
  "background:radial-gradient(70% 100% at 74% 55%,#7a2630,#3d0f16 75%)",
  '<div class="rays" style="left:470px;top:-330px"></div>' + copy("dk gold") + sh(910, 30, 310, True) + potli(310, 755, 36, cloth=CREAM, stamp="left:-28%;bottom:8%")))
# 06 half orbit cropped
ring = ""
for i, im in enumerate(ITEMS):
    a = math.radians(-90 + i * 360 / 13)
    ring += it(im, int(930 + 290 * math.cos(a)), int(240 + 290 * math.sin(a)), 84, "big")
V.append(("Giant orbit", "A huge ring of ingredient photographs around the potli, cropped by the top and bottom of the slide - big and bold",
  "background:radial-gradient(80% 100% at 85% 50%,#fff7f2,#f4ddd4 70%)",
  '<div class="arcline"></div>' + ring + copy("lt", w=440) + sh(930, 28, 300) + potli(280, 790, 70, stamp="left:auto;right:-20%;bottom:-6%")))
# 07 dark wood whole spices
V.append(("Dark wood, whole spices", "Whole spices scattered on dark wood fill the slide, the potli lit warmly in front - rich and moody",
  "background:#1a120c",
  bgimg("cat-whole.jpg", "center", "brightness(.62) saturate(1.1)") +
  '<div class="fade" style="background:linear-gradient(90deg,rgba(18,12,8,.92) 0%,rgba(18,12,8,.8) 38%,rgba(18,12,8,.2) 62%,rgba(18,12,8,0) 80%)"></div>' +
  copy("dk gold") + sh(905, 32, 320, True) + potli(320, 745, 36, cloth=CREAM, glow=True, stamp="left:-28%;bottom:8%")))
# 08 arch window photo
V.append(("Arch window", "A tall arch filled with the masala-dabba photograph, the potli standing in its doorway, a gold line tracing it",
  "background:linear-gradient(180deg,#fbf3ea,#f1e1cf)",
  '<div class="archw" style="left:720px"><img src="assets/cat-blend.jpg" alt=""></div><div class="archline" style="left:706px"></div>' +
  copy("lt") + sh(905, 18, 280) + potli(270, 770, 22, stamp="left:auto;right:-36%;bottom:56%")))
# 09 turmeric gold
V.append(("Turmeric gold", "Turmeric bowls on dark wood melting into warm gold, the green potli standing out against it",
  "background:#2a1a08",
  bgimg("cat-ground.jpg", "center", "brightness(.8) saturate(1.15)", "left:auto;right:0;width:65%;") +
  '<div class="fade" style="background:linear-gradient(90deg,#2a1a08 0%,#2a1a08 36%,rgba(42,26,8,.75) 46%,rgba(42,26,8,0) 66%)"></div>' +
  copy("dk gold") + sh(905, 32, 300, True) + potli(310, 750, 38, cloth=GREEN, cream_lk=True, letters="#f4ecd8", stamp="left:-30%;bottom:8%")))
# 10 kitchen shelf with jars
jars = "".join(it(im, 590 + i * 58, 128 if i % 2 else 112, 50, "jar") for i, im in enumerate(ITEMS[:11]))
V.append(("Kitchen shelf", "A wooden kitchen shelf of spice jars above, the potli on the counter below - a real kitchen feel",
  "background:linear-gradient(180deg,#f7ecdc 0 62%,#d9b98f 62% 63.5%,#ecd9bf 63.5%)",
  '<div class="plank" style="top:150px"></div>' + jars + copy("lt") + sh(930, 34, 280) + potli(270, 795, 40, stamp="left:-34%;bottom:6%")))
# 11 glass card over blur
V.append(("Frosted glass", "The spice photograph blurred behind, the words on a frosted glass card, the potli breaking out of the card",
  "background:#3a2414",
  bgimg("hero-2.jpg", "center", "blur(6px) brightness(.75) saturate(1.2)", "transform:scale(1.08);") +
  '<div class="glass" style="left:40px;top:40px;width:600px;height:384px"></div>' +
  copy("dk", x=80, w=500) + sh(930, 30, 300, True) + potli(320, 770, 34, stamp="left:auto;right:-30%;bottom:64%")))
# 12 chilli field
V.append(("Sun-ripe chillies", "The chilli field photograph behind, darkened, the potli standing in the field - farm to kitchen",
  "background:#0f160c",
  bgimg("hero-spices-chilli-field.jpg", "center 60%", "brightness(.6) saturate(1.15)") +
  '<div class="fade" style="background:linear-gradient(90deg,rgba(10,14,8,.9) 0%,rgba(10,14,8,.75) 38%,rgba(10,14,8,.15) 62%,rgba(10,14,8,0) 80%)"></div>' +
  copy("dk") + sh(905, 30, 300, True) + potli(310, 750, 36, cloth=CREAM, stamp="left:-30%;bottom:8%")))
# 13 spilling bowls
bowls = "".join(it(im, 640 + i * 66, int(400 - 30 * math.sin(math.pi * i / 8)), 64, "bowl") for i, im in enumerate(ITEMS[:9]))
V.append(("Spilling out", "Warm cocoa with a line of spice bowls spilling from the potli across the counter",
  "background:radial-gradient(80% 100% at 75% 30%,#5a3b26,#2a1a10 80%)",
  copy("dk gold") + sh(905, 100, 280, True) + potli(290, 760, 106, cloth=CREAM, stamp="left:-30%;bottom:18%") + bowls))
# 14 split photo panels
V.append(("Triptych", "Three tall photograph panels (turmeric, dabba, whole spices) behind, the potli in front of the middle one",
  "background:#f6eee3",
  '<div class="tri" style="left:620px"><img src="assets/cat-ground.jpg" alt=""><img src="assets/cat-blend.jpg" alt=""><img src="assets/cat-whole.jpg" alt=""></div>' +
  copy("lt", w=500) + sh(905, 14, 280) + potli(280, 765, 18, stamp="left:auto;right:-38%;bottom:4%")))
# 15 minimal luxe gold frame
V.append(("Black & gold", "Black with a fine gold frame and a soft gold glow, the cream potli centre stage - the luxury one",
  "background:radial-gradient(50% 80% at 72% 55%,#2c2416,#0d0c0a 70%)",
  '<div class="gframe"></div>' + copy("dk gold") + sh(905, 34, 300, True) + potli(300, 755, 40, cloth=CREAM, glow=True, stamp="left:-30%;bottom:8%")))

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
figcaption strong{color:#f4efe6}
.frame{position:relative;aspect-ratio:1245/464;overflow:hidden;border-radius:12px;cursor:zoom-in;outline:none}
.frame.full{position:fixed;inset:0;z-index:50;border-radius:0;aspect-ratio:auto;background:rgba(14,12,10,.92);cursor:zoom-out}
.st{position:absolute;left:0;top:0;width:1245px;height:464px;transform-origin:0 0;transform:scale(var(--s,.5));overflow:hidden}
.frame.full .st{left:50%;top:50%;transform:translate(-50%,-50%) scale(var(--s))}
.bgi{position:absolute;left:0;top:0;width:100%;height:100%;object-fit:cover}
.fade{position:absolute;inset:0;z-index:1}
/* words, as the site's slide */
.cp{position:absolute;top:50%;transform:translateY(-50%);z-index:6}
.cp .k{font:500 13px/1.3 "Jost";letter-spacing:.32em;text-transform:uppercase}
.cp h2{font:600 46px/1.04 "Fraunces",serif;margin:14px 0 14px}
.cp h2 em{display:block;font-style:normal}
.cp .d{font:300 16px/1.55 "Jost";max-width:46ch}
.cp .pl{display:inline-flex;align-items:center;gap:16px;margin-top:22px;padding:13px 14px 13px 26px;border-radius:999px;font:500 13px/1 "Jost";letter-spacing:.14em;text-transform:uppercase}
.cp .pl i{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;font-style:normal;font-size:16px}
.cp.lt .k{color:#a6475b}.cp.lt h2{color:#1f3a26}.cp.lt h2 em,.cp.lt h2 em span{color:#a6475b}.cp.lt .d{color:#4f4044}
.cp.lt .pl{background:#1f3a26;color:#fbf1ec}.cp.lt .pl i{background:#fbf1ec;color:#1f3a26}
.cp.dk .k{color:#f1ddab}.cp.dk h2{color:#f6f1e6}.cp.dk h2 em{color:#f6f1e6}.cp.dk h2 em span{color:#f1ddab}.cp.dk .d{color:#e2d8c6}
.cp.dk .pl{border:1.5px solid #e8dcc6;color:#f4f3e7}.cp.dk .pl i{background:#e8dcc6;color:#16200f}
.cp.dk.gold .pl{border:0;background:linear-gradient(160deg,#f7dc96,#e0a51a 45%,#a8760f);color:#1e2c16}.cp.dk.gold .pl i{background:#1e2c16;color:#f7dc96}
/* potli */
.pt{position:absolute;container-type:inline-size;filter:drop-shadow(0 18px 18px rgba(30,15,8,.35))}
.pt svg{position:relative;width:100%;height:100%;display:block;overflow:visible;z-index:1}
.glow{position:absolute;left:-40%;top:-30%;width:180%;height:160%;border-radius:50%;background:radial-gradient(closest-side,rgba(255,214,150,.45),transparent 70%);z-index:0}
.lk{position:absolute;left:50%;top:47%;width:40%;transform:translateX(-50%);text-align:center;container-type:inline-size;z-index:2}
.lk .lk-m,.lk span img{mix-blend-mode:multiply}.lk.cr .lk-m,.lk.cr span img{mix-blend-mode:normal}
.lk-m{display:block;width:60%;margin:0 auto}
.lk b{display:block;font:400 22cqw/1 "Jost";letter-spacing:.2em;margin:5cqw 0 0 .2em;color:var(--lc)}
.lk span{display:flex;align-items:center;justify-content:center;gap:3cqw;margin-top:3cqw}
.lk span img{height:6.5cqw;width:auto}
.lk i{font:400 10cqw/1 "Jost";font-style:normal;color:var(--lc)}
.tg{position:absolute;left:79%;top:40%;width:24%;padding:9% 2% 6%;background:#e3c595;border-radius:4px 4px 10px 10px;text-align:center;z-index:3;
  transform:rotate(-8deg);box-shadow:0 8px 12px -6px rgba(0,0,0,.55);clip-path:polygon(18% 0,82% 0,100% 14%,100% 100%,0 100%,0 14%)}
.tg i{position:absolute;left:50%;top:6%;width:10%;aspect-ratio:1;margin-left:-5%;border-radius:50%;background:#6b4a14}
.tg b{display:block;font:600 4.6cqw/1.08 "Fraunces",serif;color:#3a2a14}
.stp{position:absolute;width:40%;aspect-ratio:1;border-radius:50%;background:#fffaf4;border:2px dashed #c98d84;display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;transform:rotate(-10deg);box-shadow:0 10px 20px -10px rgba(0,0,0,.6);z-index:5}
.stp img{width:34%}.stp b{font:600 4.3cqw/1.15 "Jost";letter-spacing:.04em;text-transform:uppercase;color:#8f3a4c;margin-top:1.5cqw;white-space:nowrap}
.sh{position:absolute;height:34px;border-radius:50%;background:radial-gradient(closest-side,rgba(80,40,25,.38),transparent);z-index:2}
.sh.dk{background:radial-gradient(closest-side,rgba(0,0,0,.75),transparent)}
.it{position:absolute;border-radius:50%;overflow:hidden;border:4px solid #fffaf4;box-shadow:0 10px 18px -10px rgba(40,20,10,.7);z-index:3;display:block}
.it img{width:100%;height:100%;object-fit:cover;display:block}
/* pieces */
.beam{position:absolute;top:-40px;width:330px;height:560px;z-index:1;background:linear-gradient(180deg,rgba(255,226,170,.38),rgba(255,226,170,.05));
  clip-path:polygon(38% 0,62% 0,100% 100%,0 100%);filter:blur(6px)}
.dust{position:absolute;width:4px;height:4px;border-radius:50%;background:#f7dc96;z-index:2;animation:dust 4s ease-in-out infinite}
@keyframes dust{0%,100%{opacity:.15;transform:translateY(0)}50%{opacity:.9;transform:translateY(-14px)}}
.giant{position:absolute;left:560px;top:-30px;font:700 470px/1 "Fraunces",serif;color:rgba(166,71,91,.12);letter-spacing:-.03em;z-index:0}
.rays{position:absolute;width:1100px;height:1100px;border-radius:50%;z-index:0;
  background:repeating-conic-gradient(from 0deg,rgba(240,201,135,.22) 0 6deg,rgba(240,201,135,0) 6deg 14deg);
  -webkit-mask-image:radial-gradient(closest-side,#000 25%,transparent 70%);mask-image:radial-gradient(closest-side,#000 25%,transparent 70%)}
.arcline{position:absolute;left:640px;top:-50px;width:580px;height:580px;border-radius:50%;border:1.5px dashed rgba(166,71,91,.45);z-index:2}
.it.big{border-width:5px}
.archw{position:absolute;top:24px;width:370px;height:440px;border-radius:185px 185px 0 0;overflow:hidden;z-index:1;box-shadow:0 30px 50px -30px rgba(60,30,10,.6)}
.archw img{width:100%;height:100%;object-fit:cover;filter:brightness(.85) saturate(1.1)}
.archline{position:absolute;top:10px;width:398px;height:454px;border:1.5px solid #c9962a;border-bottom:0;border-radius:199px 199px 0 0;z-index:1}
.plank{position:absolute;left:560px;right:0;height:14px;background:linear-gradient(180deg,#b9824a,#7d5228);box-shadow:0 10px 14px -8px rgba(60,30,0,.5);z-index:2}
.it.jar{border-radius:10px 10px 12px 12px;border-top:8px solid #8a5a2b;height:62px !important}
.glass{position:absolute;z-index:2;border-radius:26px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.3);backdrop-filter:blur(14px) saturate(1.2);-webkit-backdrop-filter:blur(14px) saturate(1.2);box-shadow:0 30px 60px -30px rgba(0,0,0,.6)}
.it.bowl{border-width:5px;z-index:5}
.tri{position:absolute;top:30px;display:flex;gap:14px;z-index:1}
.tri img{width:180px;height:404px;object-fit:cover;border-radius:18px;box-shadow:0 20px 40px -24px rgba(60,30,10,.6)}
.tri img:nth-child(2){height:434px;margin-top:-15px}
.gframe{position:absolute;inset:20px;border:1px solid rgba(217,180,90,.6);border-radius:6px;z-index:1}
"""
JS = """function fit(){document.querySelectorAll('.frame').forEach(function(f){var full=f.classList.contains('full');f.style.setProperty('--s',full?Math.min(innerWidth/1245,innerHeight/464)*.96:f.clientWidth/1245);});}
addEventListener('resize',fit);fit();
document.querySelectorAll('.frame').forEach(function(f){function t(){var on=!f.classList.contains('full');document.querySelectorAll('.frame.full').forEach(function(x){x.classList.remove('full')});if(on)f.classList.add('full');fit();}
f.addEventListener('click',t);f.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();t();}});});
addEventListener('keydown',function(e){if(e.key==='Escape'){document.querySelectorAll('.frame.full').forEach(function(x){x.classList.remove('full')});fit();}});"""
html = """<!DOCTYPE html>
<html lang="en">
<!-- 15 Oct 2026. Owner, on the Grocery Kit hero slide (blush orbit): "it looks
     good but doesnt look stunning. give me some 15 variations where this
     section looks stunning". Review page only - not linked, noindex. Each is
     the slide at the owner's window (1245 x 464). Potli: rose weave, no white
     band, tag "Healthy Grocery Kit", stamp "Packed by Satva Sahelis".
     Photographs are the site's own. Generated by kit-hero-stunning.gen.py. -->
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Kit Slide Options</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>%s</style></head><body>
<header><p class="k0">DS Satva &middot; Grocery Kit slide review</p><h1>Grocery Kit slide &mdash; 15 bolder designs</h1>
<p>The same potli and the same words, set in fifteen more dramatic scenes: real spice photography, spotlight, festive gold, giant type, glass and more. Each is the slide at your screen size. Click one to see it full size (click again or press Esc). Tell me the number you like. <a href="index.html">Back to the site</a></p></header>
<div class="grid">%s</div><script>%s</script></body></html>""" % (CSS, "\n".join(figs), JS)
open(OUT, "w").write(html)
print("wrote", OUT, len(html) // 1024, "KB")
