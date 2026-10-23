#!/usr/bin/env python3
"""Generates ~/dssatva/ports/8002/kit-potli-variations.html - the potli the
owner liked (kit-bag-variations 07), redrawn with real cloth (gathered neck,
folds, linen weave, twisted cord, tassels, woven border) in 12 colour
combinations, each in the kit block."""
import os
OUT = os.path.expanduser("~/dssatva/ports/8002/kit-potli-variations.html")

def pattern_def(u, kind, pc, pc2):
    if kind == "gingham":
        return ('<pattern id="pt%s" width="26" height="26" patternUnits="userSpaceOnUse">'
                '<rect width="13" height="26" fill="%s" opacity=".38"/><rect width="26" height="13" fill="%s" opacity=".38"/></pattern>') % (u, pc, pc)
    if kind == "dots":
        return ('<pattern id="pt%s" width="24" height="24" patternUnits="userSpaceOnUse">'
                '<circle cx="6" cy="6" r="3.4" fill="%s"/><circle cx="18" cy="18" r="3.4" fill="%s"/></pattern>') % (u, pc, pc)
    if kind == "stripes":
        return ('<pattern id="pt%s" width="44" height="10" patternUnits="userSpaceOnUse">'
                '<rect x="0" width="14" height="10" fill="%s" opacity=".55"/><rect x="20" width="4" height="10" fill="%s" opacity=".8"/>'
                '<rect x="30" width="8" height="10" fill="%s" opacity=".4"/></pattern>') % (u, pc, pc2, pc)
    if kind == "floral":
        return ('<pattern id="pt%s" width="40" height="40" patternUnits="userSpaceOnUse">'
                '<g fill="%s"><path d="M20 9c4 3 4 8 0 10-4-2-4-7 0-10ZM20 31c4-3 4-8 0-10-4 2-4 7 0 10ZM9 20c3-4 8-4 10 0-2 4-7 4-10 0ZM31 20c-3 4-8 4-10 0 2-4 7-4 10 0Z"/></g>'
                '<circle cx="20" cy="20" r="2.2" fill="%s"/><circle cx="0" cy="0" r="2.4" fill="%s"/><circle cx="40" cy="40" r="2.4" fill="%s"/>'
                '<circle cx="40" cy="0" r="2.4" fill="%s"/><circle cx="0" cy="40" r="2.4" fill="%s"/></pattern>') % (u, pc, pc2, pc2, pc2, pc2, pc2)
    if kind == "chikan":
        return ('<pattern id="pt%s" width="46" height="46" patternUnits="userSpaceOnUse"><g fill="none" stroke="%s" stroke-width="1.3" stroke-opacity=".7">'
                '<path d="M23 12c3 3 3 7 0 9-3-2-3-6 0-9ZM23 34c3-3 3-7 0-9-3 2-3 6 0 9ZM12 23c3-3 7-3 9 0-2 3-6 3-9 0ZM34 23c-3 3-7 3-9 0 2-3 6-3 9 0Z"/>'
                '<circle cx="23" cy="23" r="1.6"/><path d="M0 0l5 5M46 46l-5-5M46 0l-5 5M0 46l5-5"/></g>'
                '<g fill="%s" fill-opacity=".6"><circle cx="0" cy="23" r="1.4"/><circle cx="46" cy="23" r="1.4"/><circle cx="23" cy="0" r="1.4"/><circle cx="23" cy="46" r="1.4"/></g></pattern>') % (u, pc, pc)
    if kind == "jute":
        return ('<pattern id="pt%s" width="8" height="8" patternUnits="userSpaceOnUse">'
                '<path d="M0 2h8M0 6h8" stroke="%s" stroke-width="1.8" stroke-opacity=".55"/><path d="M2 0v8M6 0v8" stroke="%s" stroke-width="1.2" stroke-opacity=".45"/></pattern>') % (u, pc, pc2)
    return ""

def potli(u, cloth, shade, cord, cord2, trim, trim2, tassel, pattern=None, pc=None, pc2=None):
    body = ("M150 174C94 198 54 252 54 324C54 404 110 450 200 450C290 450 346 404 346 324"
            "C346 252 306 198 250 174Z")
    ruff = ("M152 176C146 152 128 124 110 98C126 102 140 94 150 80C160 93 172 93 182 77"
            "C192 90 208 90 218 77C228 93 240 93 250 80C260 94 274 102 290 98C272 124 254 152 248 176Z")
    back = ("M128 104C142 96 152 86 158 74C168 86 178 86 188 70C196 82 204 82 212 70C222 86 232 86 242 74"
            "C248 86 258 96 272 104L262 118H138Z")
    folds_body = ["M172 182C150 234 120 276 102 336", "M188 184C180 244 168 304 158 372",
                  "M212 184C222 244 234 304 246 372", "M230 182C254 234 284 276 300 336",
                  "M160 180C128 214 96 246 76 296", "M242 180C276 214 306 246 326 296"]
    folds_ruff = ["M164 174L136 104", "M180 174L168 86", "M200 174V84", "M220 174L234 86", "M236 174L266 104"]
    def creases(paths, w):
        out = ""
        for p in paths:
            out += '<path d="%s" stroke="#000" stroke-opacity=".2" stroke-width="%s" fill="none" filter="url(#bl%s)"/>' % (p, w, u)
            out += '<path d="%s" stroke="#fff" stroke-opacity=".28" stroke-width="%s" fill="none" filter="url(#bl%s)" transform="translate(5 0)"/>' % (p, w * .7, u)
        return out
    trim_band = ""
    if trim:
        trim_band = ('<g clip-path="url(#cb%s)"><path d="M40 392Q200 448 360 392" stroke="%s" stroke-width="20" fill="none"/>'
                     '<path d="M40 392Q200 448 360 392" stroke="%s" stroke-width="3" fill="none" stroke-dasharray="7 7"/>'
                     '<path d="M40 380Q200 436 360 380" stroke="%s" stroke-width="2.5" fill="none"/>'
                     '<path d="M40 404Q200 460 360 404" stroke="%s" stroke-width="2.5" fill="none"/></g>') % (u, trim, trim2, trim, trim)
    patch = ""
    if pattern and pattern not in ("dots", "chikan", "jute", "gingham"):
        # a plain stitched panel so the logo reads on a busy print
        patch = ('<rect x="110" y="200" width="180" height="158" rx="20" fill="%s"/>'
                 '<rect x="110" y="200" width="180" height="158" rx="20" fill="url(#vol%s)" opacity=".5"/>'
                 '<rect x="117" y="207" width="166" height="144" rx="15" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="6 5" opacity=".8"/>') % (cloth, u, pc)
    svg = f'''<svg viewBox="0 0 400 470"><defs>
<filter id="bl{u}" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3.2"/></filter>
<filter id="ln{u}" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9 .045" numOctaves="2" seed="3" result="a"/>
<feTurbulence type="fractalNoise" baseFrequency=".045 .9" numOctaves="2" seed="7" result="b"/><feBlend in="a" in2="b" mode="multiply"/>
<feColorMatrix values="0 0 0 0 .25  0 0 0 0 .18  0 0 0 0 .1  0 0 0 .34 0"/></filter>
<radialGradient id="vol{u}" cx=".36" cy=".3" r=".85"><stop offset="0" stop-color="#fff" stop-opacity=".34"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/>
<stop offset=".8" stop-color="#000" stop-opacity=".16"/><stop offset="1" stop-color="#000" stop-opacity=".34"/></radialGradient>
<linearGradient id="rv{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset="1" stop-color="#000" stop-opacity=".22"/></linearGradient>
<linearGradient id="rim{u}" x1="0" x2="1"><stop offset=".78" stop-color="#fff" stop-opacity="0"/><stop offset=".93" stop-color="#fff" stop-opacity=".18"/><stop offset="1" stop-color="#000" stop-opacity=".1"/></linearGradient>
<clipPath id="cb{u}"><path d="{body}"/></clipPath><clipPath id="cr{u}"><path d="{ruff}"/></clipPath>{pattern_def(u, pattern, pc, pc2) if pattern else ""}
</defs>
<path d="{back}" fill="{shade}"/><path d="{back}" fill="#000" opacity=".25"/>
<path d="{ruff}" fill="{cloth}"/>{(chr(60)+"path d=\""+ruff+"\" fill=\"url(#pt"+u+")\"/"+chr(62)) if pattern else ""}<path d="{ruff}" fill="url(#rv{u})"/>
<g clip-path="url(#cr{u})"><rect width="400" height="470" filter="url(#ln{u})"/>{creases(folds_ruff, 4)}</g>
<path d="{body}" fill="{cloth}"/>{(chr(60)+"path d=\""+body+"\" fill=\"url(#pt"+u+")\"/"+chr(62)) if pattern else ""}
<g clip-path="url(#cb{u})"><rect width="400" height="470" filter="url(#ln{u})"/>{creases(folds_body, 6)}
<rect width="400" height="470" fill="url(#vol{u})"/><rect width="400" height="470" fill="url(#rim{u})"/>
<ellipse cx="200" cy="180" rx="70" ry="18" fill="#000" opacity=".22" filter="url(#bl{u})"/></g>
{trim_band}{patch}
<path d="M144 178Q200 200 256 178" stroke="{cord}" stroke-width="11" fill="none" stroke-linecap="round"/>
<path d="M144 178Q200 200 256 178" stroke="{cord2}" stroke-width="11" fill="none" stroke-dasharray="3 5" opacity=".75"/>
<path d="M144 175Q200 196 256 175" stroke="#fff" stroke-opacity=".3" stroke-width="2" fill="none"/>
<circle cx="252" cy="182" r="10" fill="{cord}"/><circle cx="252" cy="182" r="10" fill="none" stroke="{cord2}" stroke-width="3" stroke-dasharray="3 3"/>
<path d="M250 188C262 214 260 238 268 262" stroke="{cord}" stroke-width="6" fill="none" stroke-linecap="round"/>
<path d="M256 188C280 208 290 232 292 254" stroke="{cord}" stroke-width="6" fill="none" stroke-linecap="round"/>
<g fill="{tassel}"><rect x="261" y="258" width="14" height="10" rx="4"/><rect x="285" y="250" width="14" height="10" rx="4"/></g>
<g stroke="{tassel}" stroke-width="2.4" stroke-linecap="round"><path d="M263 268v26M266 268v28M269 268v29M272 268v28M275 268v26"/>
<path d="M287 260v26M290 260v28M293 260v29M296 260v28M299 260v26"/></g>
</svg>'''
    return svg

def lockup(tone):
    mark = "mark-dark.png" if tone == "print" else "mark-cream.png"
    return ('<div class="lk %s"><img class="lk-m" src="assets/%s" alt=""><b class="lk-s">SATVA</b>'
            '<span class="lk-d"><img src="assets/kit-sprig-l.png" alt=""><i>Dil Se Pure</i><img src="assets/kit-sprig-r.png" alt=""></span></div>') % (tone, mark)

#  name, caption, block{bg, kick, h, em, d, btn, btnfg, tel}, scene{wall1, wall2, table1, table2}, potli{...}, tone, bowls
P = [
 ("Kumkum & ivory", "Deep maroon block; ivory potli with a kumkum-red border and gold cord - festive, like a wedding gift",
  dict(bg="radial-gradient(120% 140% at 85% 20%,#7a2630,#4a1219 60%,#350c12)", kick="#f0c987", h="#fbf1e4", em="#f0c987", d="#ead6c8", btn="linear-gradient(160deg,#f7dc96,#e0a51a 42%,#a8760f)", btnfg="#3a0f14", tel="#f0c987"),
  dict(w1="#fff8ef", w2="#f3e3d3", t1="#ecdcc8", t2="#dcc7ae"),
  dict(cloth="#f4ecdc", shade="#e2d5bd", cord="#c9962a", cord2="#8a6510", trim="#b8232f", trim2="#f0c987", tassel="#b8232f"), "print", ("u-chilli-powder", "u-turmeric")),
 ("Indigo & saffron", "Indigo block; an indigo-dyed potli with the logo in cream, saffron cord and tassels",
  dict(bg="radial-gradient(120% 140% at 85% 20%,#2f3f6e,#1c2647 60%,#141b33)", kick="#f2b04a", h="#f5f1e8", em="#f2b04a", d="#d5d9e6", btn="linear-gradient(160deg,#ffcf7a,#e8901f)", btnfg="#1c2647", tel="#f2b04a"),
  dict(w1="#f7f4ee", w2="#e6e1d6", t1="#e3dccd", t2="#d2c8b4"),
  dict(cloth="#34497e", shade="#26365f", cord="#e8901f", cord2="#a85f0a", trim="#f2b04a", trim2="#34497e", tassel="#e8901f"), "cream", ("u-turmeric", "u-coriander-seeds")),
 ("Terracotta & cream", "Terracotta block; a natural cream potli with a terracotta border and dark brown cord - earthy, village-made",
  dict(bg="radial-gradient(120% 140% at 85% 20%,#c06a48,#9c4a2e 60%,#7d3820)", kick="#fbe3c4", h="#fff6ea", em="#fbe3c4", d="#f6dccb", btn="#2e1c12", btnfg="#fbe3c4", tel="#fff1dc"),
  dict(w1="#fdf6ec", w2="#f1e1cc", t1="#e6d3b9", t2="#d4bc9c"),
  dict(cloth="#f1e6d0", shade="#dccdb0", cord="#5a3a22", cord2="#2e1c12", trim="#b5583a", trim2="#f1e6d0", tassel="#5a3a22"), "print", ("u-cumin-seeds", "u-chilli-powder")),
 ("Mustard & charcoal", "Charcoal block; a haldi-mustard potli with a cream border and black cord - bold and modern",
  dict(bg="radial-gradient(120% 140% at 85% 20%,#3b3935,#252421 60%,#1a1917)", kick="#e8b93a", h="#f6f1e6", em="#e8b93a", d="#d6d1c6", btn="linear-gradient(160deg,#f6d36a,#d9a521)", btnfg="#1a1917", tel="#e8b93a"),
  dict(w1="#f6f3ec", w2="#e4dfd4", t1="#d9d2c4", t2="#c4bba9"),
  dict(cloth="#dca82a", shade="#b98a18", cord="#26241f", cord2="#000", trim="#f6ecd4", trim2="#26241f", tassel="#26241f"), "print", ("u-garam-masala", "u-methi-seeds")),
 ("Peach & forest", "A light peach block (dark words); a forest-green potli with the logo in cream and a gold cord",
  dict(bg="radial-gradient(120% 140% at 85% 20%,#fdf1ea,#f6dccf 60%,#efcbbb)", kick="#a0442e", h="#1f3a26", em="#a0442e", d="#4a3a30", btn="#1f3a26", btnfg="#f4efe6", tel="#7f3a2a", dark=True),
  dict(w1="#fffaf6", w2="#f6e6dc", t1="#efdccf", t2="#e2c9b8"),
  dict(cloth="#2f5238", shade="#223d29", cord="#d4a63c", cord2="#8a6510", trim="#d4a63c", trim2="#2f5238", tassel="#d4a63c"), "cream", ("u-himalayan-pink-salt", "u-coriander-seeds")),
 ("Plum & gold", "Plum block; a blush potli with a plum border and gold cord - soft and premium",
  dict(bg="radial-gradient(120% 140% at 85% 20%,#5c2d4d,#3d1f33 60%,#2b1524)", kick="#e6c27a", h="#fbf0f4", em="#e6c27a", d="#e6d2dc", btn="linear-gradient(160deg,#f7dc96,#d9a73a)", btnfg="#2b1524", tel="#e6c27a"),
  dict(w1="#fff7f8", w2="#f3e2e6", t1="#ecd8dc", t2="#dcc0c7"),
  dict(cloth="#f5e1e1", shade="#e3c9ca", cord="#c9a14a", cord2="#8a6510", trim="#6a3157", trim2="#e6c27a", tassel="#c9a14a"), "print", ("u-coconut-sugar", "u-chilli-powder")),
 ("Teal & coral", "Deep teal block; an ivory potli with a coral border and coral cord - fresh and lively",
  dict(bg="radial-gradient(120% 140% at 85% 20%,#1d6363,#0f4c4c 60%,#0a3838)", kick="#f4a582", h="#f2f7f4", em="#f4a582", d="#cfe1dc", btn="linear-gradient(160deg,#f9b99a,#e07a5f)", btnfg="#0a3838", tel="#f4a582"),
  dict(w1="#f6faf8", w2="#e2ece8", t1="#dde5df", t2="#c8d3cb"),
  dict(cloth="#f5efe3", shade="#e2d8c6", cord="#e07a5f", cord2="#a8492f", trim="#e07a5f", trim2="#f5efe3", tassel="#e07a5f"), "print", ("u-turmeric", "u-mustard-seeds")),
 ("Cocoa & gold", "Cocoa block; an oatmeal linen potli with a brown border and gold cord - warm, like a sweet-shop box",
  dict(bg="radial-gradient(120% 140% at 85% 20%,#5a3b26,#3b2618 60%,#2a1a10)", kick="#e7bf6a", h="#fbf3e6", em="#e7bf6a", d="#e3d3c0", btn="linear-gradient(160deg,#f7dc96,#d9a73a)", btnfg="#2a1a10", tel="#e7bf6a"),
  dict(w1="#fbf5ec", w2="#ecdcc6", t1="#a8743d", t2="#8f5e2e", wood=True),
  dict(cloth="#e6d6b8", shade="#cfbd99", cord="#c9962a", cord2="#7a5418", trim="#6b4423", trim2="#e7bf6a", tassel="#c9962a"), "print", ("u-garam-masala", "u-cumin-seeds")),
 ("Saffron & green", "A bright saffron block (dark words); an ivory potli with a green border and green cord - the flag of the kitchen",
  dict(bg="radial-gradient(120% 140% at 85% 20%,#f7b955,#ec9a2b 60%,#d9821a)", kick="#1f3a26", h="#1f2a14", em="#7a1f12", d="#3a2a10", btn="#1f3a26", btnfg="#fdf3e0", tel="#1f3a26", dark=True),
  dict(w1="#fffaf0", w2="#f6e8cf", t1="#efdcbb", t2="#e0c89e"),
  dict(cloth="#f6efdf", shade="#e2d8c2", cord="#2f5238", cord2="#1a2e1f", trim="#2f5238", trim2="#f6efdf", tassel="#2f5238"), "print", ("u-chilli-powder", "u-coriander-seeds")),
 ("Sage & terracotta", "A soft sage block (dark words); a terracotta potli with the logo in cream and a cream cord",
  dict(bg="radial-gradient(120% 140% at 85% 20%,#cdd8bf,#b3c2a2 60%,#9fb08c)", kick="#7a3a22", h="#1f2a17", em="#9c4a2e", d="#34402a", btn="#9c4a2e", btnfg="#fff4e6", tel="#7a3a22", dark=True),
  dict(w1="#fbfaf4", w2="#e9ecdf", t1="#e2e2d2", t2="#cfd0bb"),
  dict(cloth="#b8603e", shade="#954a2c", cord="#f4e8d2", cord2="#c9b590", trim="#f4e8d2", trim2="#b8603e", tassel="#f4e8d2"), "cream", ("u-methi-seeds", "u-turmeric")),
 ("Black & gold", "Black block, black table; a black potli with the logo in cream and gold, gold cord - the luxury one",
  dict(bg="radial-gradient(120% 140% at 85% 20%,#2a2a28,#161615 60%,#0d0d0c)", kick="#d9b45a", h="#f6f0e2", em="#d9b45a", d="#cfc8b8", btn="linear-gradient(160deg,#f7dc96,#c9962a)", btnfg="#0d0d0c", tel="#d9b45a"),
  dict(w1="#3a3a35", w2="#1d1d1a", t1="#2a2722", t2="#1a1815", darkscene=True),
  dict(cloth="#262624", shade="#161615", cord="#d9b45a", cord2="#8a6510", trim="#d9b45a", trim2="#262624", tassel="#d9b45a"), "cream", ("u-garam-masala", "u-turmeric")),
 ("Cream & jute, minimal", "A quiet cream block (dark words); an unbleached potli with a jute cord and no border - simple and honest",
  dict(bg="radial-gradient(120% 140% at 85% 20%,#fbf6ec,#f1e7d4 60%,#e8dbc2)", kick="#94660a", h="#1f3a26", em="#94660a", d="#4a4636", btn="#1f3a26", btnfg="#f4efe6", tel="#7f5a0f", dark=True),
  dict(w1="#ffffff", w2="#f2ece0", t1="#e9e1d1", t2="#d9cdb6"),
  dict(cloth="#ece2cc", shade="#d6c9ac", cord="#b08a50", cord2="#7a5c2e", trim=None, trim2=None, tassel="#b08a50"), "print", ("u-coriander-seeds", "u-chia-seeds")),
]


def L(bg1, bg2, kick, h, em, d, btn, btnfg, tel):
    return dict(bg="radial-gradient(120%% 140%% at 85%% 20%%,%s,%s)" % (bg1, bg2), kick=kick, h=h, em=em, d=d, btn=btn, btnfg=btnfg, tel=tel)
def SC(w1, w2, t1, t2): return dict(w1=w1, w2=w2, t1=t1, t2=t2)
P_LIGHT = [
 ("Blush & ivory", "Soft blush block; an ivory potli with a rose border and gold cord",
  L("#fdf3ef", "#f5dcd2", "#a0442e", "#1f3a26", "#b0566a", "#4f4038", "#1f3a26", "#fbf1ec", "#a0442e"),
  SC("#ffffff", "#f8ebe6", "#f1e0d8", "#e4cdc3"),
  dict(cloth="#f7f0e4", shade="#e6dccb", cord="#c9962a", cord2="#8a6510", trim="#d98a8a", trim2="#fff4f0", tassel="#d98a8a"), "print", ("u-himalayan-pink-salt", "u-turmeric")),
 ("Mint & cream", "Fresh mint block; a cream potli with a sage-green border and green cord",
  L("#f3faf4", "#d9ebdc", "#3d6b4a", "#1f3a26", "#3d6b4a", "#3e4a3f", "#2f5238", "#f1f7f1", "#2f5238"),
  SC("#ffffff", "#eef5ef", "#e3ebe2", "#d1dccf"),
  dict(cloth="#f6f1e4", shade="#e3dccb", cord="#4f7a55", cord2="#2f5238", trim="#8fb08f", trim2="#f6f1e4", tassel="#4f7a55"), "print", ("u-coriander-seeds", "u-methi-seeds")),
 ("Butter & sage", "Buttery yellow block; a pale sage potli with a gold cord",
  L("#fffbe8", "#f7ebb8", "#8a6510", "#1f3a26", "#8a6510", "#4a4430", "#1f3a26", "#fffbe8", "#7a5a0a"),
  SC("#ffffff", "#fbf6e2", "#f2e9cc", "#e5d8b0"),
  dict(cloth="#dfe8d2", shade="#c8d4b8", cord="#c9962a", cord2="#8a6510", trim="#f2d57a", trim2="#8a6510", tassel="#c9962a"), "print", ("u-turmeric", "u-cumin-seeds")),
 ("Lavender & gold", "Pale lavender block; an ivory potli with a lavender border and gold cord",
  L("#f8f5fb", "#e4dcef", "#6b5a9a", "#2a2440", "#6b5a9a", "#45405a", "#4a3f75", "#f8f5fb", "#4a3f75"),
  SC("#ffffff", "#f3f0f7", "#e9e4ef", "#d9d1e4"),
  dict(cloth="#f7f2e8", shade="#e5ddcf", cord="#c9a14a", cord2="#8a6510", trim="#a693cc", trim2="#f7f2e8", tassel="#a693cc"), "print", ("u-chia-seeds", "u-coconut-sugar")),
 ("Sky & sand", "Light sky-blue block; a sand potli with a dusty-blue border and tan cord",
  L("#f3f8fc", "#d8e7f2", "#4a6f94", "#1d2f45", "#4a6f94", "#3c4856", "#2f4f72", "#f3f8fc", "#2f4f72"),
  SC("#ffffff", "#eef4f8", "#e6ebee", "#d3dbe0"),
  dict(cloth="#efe5cf", shade="#dccfb4", cord="#b08a50", cord2="#7a5c2e", trim="#7f9dbd", trim2="#efe5cf", tassel="#7f9dbd"), "print", ("u-coriander-seeds", "u-himalayan-pink-salt")),
 ("Apricot & terracotta", "Warm apricot block; a cream potli with a terracotta border and brown cord",
  L("#fff6ee", "#fbdcc6", "#a4492f", "#2e1c12", "#a4492f", "#4f3c30", "#9c4a2e", "#fff6ee", "#8a3d22"),
  SC("#ffffff", "#fdf1e8", "#f3e2d4", "#e6cdb8"),
  dict(cloth="#f6eedd", shade="#e3d7c0", cord="#6b4423", cord2="#3d2614", trim="#c4653f", trim2="#f6eedd", tassel="#6b4423"), "print", ("u-chilli-powder", "u-garam-masala")),
 ("Pistachio & rose", "Pistachio block; a blush potli with a pistachio border and rose cord",
  L("#f7faef", "#dfeac8", "#5d7a33", "#24301a", "#b0566a", "#43493a", "#4a6a2a", "#f7faef", "#4a6a2a"),
  SC("#ffffff", "#f4f7ec", "#e8eddc", "#d7dfc5"),
  dict(cloth="#f8e6e4", shade="#e8d0cd", cord="#c97a86", cord2="#8f4552", trim="#a9c27e", trim2="#f8e6e4", tassel="#c97a86"), "print", ("u-methi-seeds", "u-coconut-sugar")),
 ("Ivory & turmeric", "Ivory block; a soft turmeric potli with a green border and green cord",
  L("#fffcf4", "#f6ead0", "#94660a", "#1f3a26", "#94660a", "#4a4636", "#1f3a26", "#fffcf4", "#7f5a0f"),
  SC("#ffffff", "#fbf6ea", "#f1e8d4", "#e2d5b9"),
  dict(cloth="#f3d98c", shade="#e0c06a", cord="#3f6b47", cord2="#24412c", trim="#3f6b47", trim2="#f3d98c", tassel="#3f6b47"), "print", ("u-turmeric", "u-chilli-powder")),
 ("Rose & sage", "Powder-pink block; a pale sage potli with a rose border and gold cord",
  L("#fff5f6", "#f8dde2", "#a6475b", "#2a1f22", "#a6475b", "#4f4044", "#8f3a4c", "#fff5f6", "#8f3a4c"),
  SC("#ffffff", "#fcf1f2", "#f2e3e5", "#e5ced2"),
  dict(cloth="#e3ead9", shade="#cdd7c1", cord="#c9a14a", cord2="#8a6510", trim="#e3a7b2", trim2="#e3ead9", tassel="#e3a7b2"), "print", ("u-himalayan-pink-salt", "u-coriander-seeds")),
 ("Stone & olive", "Warm stone-grey block; an oatmeal potli with an olive border and olive cord",
  L("#f8f6f1", "#e6e2d7", "#6b7240", "#25281a", "#6b7240", "#46473d", "#4f5530", "#f8f6f1", "#4f5530"),
  SC("#ffffff", "#f3f1ec", "#e8e4da", "#d6d0c2"),
  dict(cloth="#eae0cb", shade="#d7cbb1", cord="#7a8450", cord2="#4f5530", trim="#8f9a5e", trim2="#eae0cb", tassel="#7a8450"), "print", ("u-cumin-seeds", "u-mustard-seeds")),
 ("Aqua & coral", "Pale aqua block; an ivory potli with a coral border and coral cord",
  L("#f2fbf9", "#d6efea", "#2f7d74", "#173a36", "#d0664a", "#3c4a48", "#2a6d65", "#f2fbf9", "#2a6d65"),
  SC("#ffffff", "#eff8f6", "#e4eeec", "#d0dfdb"),
  dict(cloth="#f8f2e6", shade="#e6dccb", cord="#e07a5f", cord2="#a8492f", trim="#e9937b", trim2="#f8f2e6", tassel="#e07a5f"), "print", ("u-turmeric", "u-coriander-seeds")),
 ("Cream & gold", "Classic cream block; a white linen potli with a gold border and gold cord - clean and premium",
  L("#fffdf8", "#f2e8d4", "#94660a", "#1f3a26", "#94660a", "#4a4636", "#1f3a26", "#fffdf8", "#7f5a0f"),
  SC("#ffffff", "#f7f2e8", "#efe7d6", "#dfd3bb"),
  dict(cloth="#fbf8f1", shade="#ebe4d6", cord="#c9962a", cord2="#8a6510", trim="#d9b45a", trim2="#fbf8f1", tassel="#c9962a"), "print", ("u-garam-masala", "u-turmeric")),
]
if os.environ.get("LIGHT"):
    P = P_LIGHT
    OUT = OUT.replace("kit-potli-variations.html", "kit-potli-light.html")

def C(cloth, shade, cord, cord2, trim, trim2, tassel, pattern=None, pc=None, pc2=None):
    return dict(cloth=cloth, shade=shade, cord=cord, cord2=cord2, trim=trim, trim2=trim2, tassel=tassel, pattern=pattern, pc=pc, pc2=pc2)
G, BR = "#1f3a26", "#2e1c12"
P_DIFF = [
 ("Marigold on white", "Open white scene, no card - a marigold-orange potli with a cream cord and border, the colour all in the bag",
  L("#ffffff", "#fbf5ea", "#c27a12", G, "#c27a12", "#4a4636", G, "#fffdf8", "#9a5f0a"), SC("#ffffff", "#fbf5ea", "#f6ecdb", "#ecdcc2"),
  C("#f3b456", "#dc962e", "#fffaf0", "#e0c9a0", "#fffaf0", "#f3b456", "#fffaf0"), "print", ("u-turmeric", "u-chilli-powder"), dict(layout="bleed")),
 ("Green gingham", "Soft sage block; a cream potli in a green gingham check, green cord - picnic-fresh",
  L("#f8faf3", "#e7ecdb", "#4f7a55", G, "#4f7a55", "#43493a", "#2f5238", "#f8faf3", "#2f5238"), SC("#ffffff", "#f4f6ee", "#ebeee2", "#dce1cf"),
  C("#f7f3e8", "#e5dfcf", "#4f7a55", "#2f5238", "#4f7a55", "#f7f3e8", "#4f7a55", "gingham", "#6f9a6a"), "print", ("u-coriander-seeds", "u-methi-seeds")),
 ("Block-print floral", "Open warm-white scene - an ivory potli hand block-printed in terracotta and green flowers",
  L("#fffcf6", "#f6ebda", "#a4492f", G, "#a4492f", "#4a4036", "#9c4a2e", "#fffcf6", "#8a3d22"), SC("#fffcf6", "#f6ebda", "#efe1cb", "#e2cfb1"),
  C("#f8f1e3", "#e7dcc7", "#b5583a", "#7a3a22", "#b5583a", "#f8f1e3", "#b5583a", "floral", "#c76a4c", "#3f6b47"), "print", ("u-cumin-seeds", "u-garam-masala"), dict(layout="bleed")),
 ("Pastel stripes", "Warm cream block; a potli woven in peach and sage stripes, sage cord",
  L("#fffaf5", "#f6ebe0", "#b0603e", G, "#b0603e", "#4a4036", "#3f6b47", "#fffaf5", "#3f6b47"), SC("#ffffff", "#fbf4ec", "#f2e6d8", "#e5d4c0"),
  C("#f8f1e4", "#e6dccb", "#6f9a6a", "#3f6b47", "#e8a68c", "#f8f1e4", "#6f9a6a", "stripes", "#ecb39c", "#8fb08f"), "print", ("u-himalayan-pink-salt", "u-coriander-seeds")),
 ("Mint polka", "Floating on mint, no table - a mint potli with white polka dots and a gold cord",
  L("#f7fcf9", "#e3f1e9", "#3d7a5a", G, "#3d7a5a", "#3e4a42", "#2f6a4a", "#f7fcf9", "#2f6a4a"), SC("#f7fcf9", "#e3f1e9", "#e3f1e9", "#e3f1e9"),
  C("#cfe6d8", "#b5d4c2", "#c9962a", "#8a6510", "#fffaf0", "#cfe6d8", "#c9962a", "dots", "#fffaf0"), "print", ("u-chia-seeds", "u-coriander-seeds"), dict(layout="float")),
 ("Lilac & pearl", "Open pearl-white scene - a lilac potli with a cream border and cream cord, soft and calm",
  L("#fdfcff", "#efebf6", "#6b5a9a", "#2a2440", "#6b5a9a", "#45405a", "#4a3f75", "#fdfcff", "#4a3f75"), SC("#fdfcff", "#efebf6", "#e8e3f0", "#dbd3e7"),
  C("#dccfee", "#c4b4de", "#fffaf0", "#d9cbb0", "#fffaf0", "#dccfee", "#fffaf0"), "print", ("u-coconut-sugar", "u-chia-seeds"), dict(layout="bleed")),
 ("Sky polka", "Airy white-blue block; a sky-blue potli with white dots and a navy cord",
  L("#fbfdff", "#e9f1f8", "#3a6a96", "#1d2f45", "#3a6a96", "#3c4856", "#2f4f72", "#fbfdff", "#2f4f72"), SC("#ffffff", "#f1f6fa", "#e8eef3", "#d7e0e7"),
  C("#cfe0f0", "#b5cbe2", "#2f4f72", "#1d2f45", "#fffaf0", "#cfe0f0", "#2f4f72", "dots", "#fffaf0"), "print", ("u-turmeric", "u-himalayan-pink-salt")),
 ("White chikankari", "Open pale-sage scene - a white potli with fine white-on-white chikankari flowers, sage cord",
  L("#f8faf5", "#e8eee1", "#5d7a4a", G, "#5d7a4a", "#43493a", "#3f6b47", "#f8faf5", "#3f6b47"), SC("#f8faf5", "#e8eee1", "#e2e8da", "#d3dcc8"),
  C("#fcfbf7", "#ece9df", "#8fa880", "#5d7a4a", None, None, "#8fa880", "chikan", "#a9b99b"), "print", ("u-methi-seeds", "u-turmeric"), dict(layout="bleed")),
 ("Dusty rose", "Floating on sand-pink, no table - a dusty-rose potli with a cream border and cream cord",
  L("#fdf8f6", "#f3e5df", "#a6475b", "#2a1f22", "#a6475b", "#4f4044", "#8f3a4c", "#fdf8f6", "#8f3a4c"), SC("#fdf8f6", "#f3e5df", "#f3e5df", "#f3e5df"),
  C("#e7bdb5", "#d3a198", "#fffaf0", "#d9c3b0", "#fffaf0", "#e7bdb5", "#fffaf0"), "print", ("u-himalayan-pink-salt", "u-coconut-sugar"), dict(layout="float")),
 ("Natural jute", "Open linen-white scene - a light jute potli with a cream border and cream cord, honest and earthy",
  L("#fffdf9", "#f3ede3", "#8a6a3a", BR, "#8a6a3a", "#4a4232", "#5a4428", "#fffdf9", "#5a4428"), SC("#fffdf9", "#f3ede3", "#ece4d6", "#ddd2be"),
  C("#ddc59c", "#c7ad80", "#fffaf0", "#d9c9a8", "#f6efe0", "#b08a50", "#fffaf0", "jute", "#b08a50", "#9a7640"), "print", ("u-cumin-seeds", "u-coriander-seeds"), dict(layout="bleed")),
 ("Peach madras", "Soft peach block; an ivory potli in coral and gold madras stripes, coral cord",
  L("#fff8f2", "#fde6d6", "#c0563e", BR, "#c0563e", "#4f3c30", "#b5583a", "#fff8f2", "#9c4a2e"), SC("#ffffff", "#fdf3ea", "#f5e3d4", "#e9cfba"),
  C("#f9f2e5", "#e8dcc8", "#e07a5f", "#a8492f", "#e07a5f", "#f9f2e5", "#e07a5f", "stripes", "#f0a27a", "#e3c35a"), "print", ("u-chilli-powder", "u-turmeric")),
 ("Turquoise block print", "Floating on pale aqua, no table - a white potli block-printed in turquoise and gold, teal cord",
  L("#f8fcfc", "#e4f2f2", "#2f7d7d", "#173a3a", "#2f7d7d", "#3c4a4a", "#2a6d6d", "#f8fcfc", "#2a6d6d"), SC("#f8fcfc", "#e4f2f2", "#e4f2f2", "#e4f2f2"),
  C("#fbf8f1", "#e9e3d6", "#3f8f8f", "#235a5a", "#4aa3a3", "#fbf8f1", "#3f8f8f", "floral", "#4aa3a3", "#e0a51a"), "print", ("u-turmeric", "u-mustard-seeds"), dict(layout="float")),
]
if os.environ.get("DIFF"):
    P = P_DIFF
    OUT = OUT.replace("kit-potli-variations.html", "kit-potli-light-2.html")

LIL_B = L("#fdfcff", "#efebf6", "#6b5a9a", "#2a2440", "#6b5a9a", "#45405a", "#4a3f75", "#fdfcff", "#4a3f75")
LIL_S = SC("#fdfcff", "#efebf6", "#e8e3f0", "#dbd3e7")
ROS_B = L("#fdf8f6", "#f3e5df", "#a6475b", "#2a1f22", "#a6475b", "#4f4044", "#8f3a4c", "#fdf8f6", "#8f3a4c")
ROS_S = SC("#fdf8f6", "#f3e5df", "#f3e5df", "#f3e5df")
BLU_B = L("#fff8f8", "#f6e4e6", "#a6475b", "#2a1f22", "#7a5a9a", "#4f4044", "#8f3a4c", "#fff8f8", "#8f3a4c")
BLU_S = SC("#fff8f8", "#f6e4e6", "#efdcde", "#e3cbce")
MIX_B = L("#fdf9fc", "#efe3ee", "#7d4f7a", "#2a1f28", "#7d4f7a", "#4a3f48", "#6a3f66", "#fdf9fc", "#6a3f66")
MIX_S = SC("#fdf9fc", "#efe3ee", "#efe3ee", "#efe3ee")
LILAC, LILAC_D, LILAC_P = "#dccfee", "#c4b4de", "#b7a4d6"
ROSE, ROSE_D, ROSE_P = "#e7bdb5", "#d3a198", "#c98d84"
P_MIX = [
 ("Lilac weave, cream cord", "Lilac in the small woven check, cream cord and border - the 06 colour in the 10 cloth, open pearl scene",
  LIL_B, LIL_S, C(LILAC, LILAC_D, "#fffaf0", "#d9cbb0", "#fffaf0", LILAC, "#fffaf0", "jute", LILAC_P, LILAC_D), "print", ("u-coconut-sugar", "u-chia-seeds"), dict(layout="bleed")),
 ("Rose weave, cream cord", "Dusty rose in the small woven check, cream cord and border - the 09 colour in the 10 cloth, floating on sand-pink",
  ROS_B, ROS_S, C(ROSE, ROSE_D, "#fffaf0", "#d9c3b0", "#fffaf0", ROSE, "#fffaf0", "jute", ROSE_P, ROSE_D), "print", ("u-himalayan-pink-salt", "u-coconut-sugar"), dict(layout="float")),
 ("Lilac weave on blush", "The lilac woven potli on a soft blush block, with a rose cord - the two colours together",
  BLU_B, BLU_S, C(LILAC, LILAC_D, "#d58f8a", "#a8605a", "#fffaf0", LILAC, "#d58f8a", "jute", LILAC_P, LILAC_D), "print", ("u-himalayan-pink-salt", "u-chia-seeds"), dict(layout="bleed")),
 ("Rose weave on lilac", "The rose woven potli on the pale lilac block, with a lilac cord",
  LIL_B, SC("#fdfcff", "#efebf6", "#efebf6", "#efebf6"), C(ROSE, ROSE_D, "#a693cc", "#6b5a9a", "#fffaf0", ROSE, "#a693cc", "jute", ROSE_P, ROSE_D), "print", ("u-coconut-sugar", "u-himalayan-pink-salt"), dict(layout="float")),
 ("Lilac weave, gold & rose", "Lilac woven potli with a gold cord and a dusty-rose border - a little richer",
  LIL_B, LIL_S, C(LILAC, LILAC_D, "#c9a14a", "#8a6510", ROSE, "#fffaf0", "#c9a14a", "jute", LILAC_P, LILAC_D), "print", ("u-turmeric", "u-chia-seeds"), dict(layout="bleed")),
 ("Rose weave, gold & lilac", "Rose woven potli with a gold cord and a lilac border",
  ROS_B, ROS_S, C(ROSE, ROSE_D, "#c9a14a", "#8a6510", LILAC, "#fffaf0", "#c9a14a", "jute", ROSE_P, ROSE_D), "print", ("u-turmeric", "u-himalayan-pink-salt"), dict(layout="float")),
 ("Pale lilac, plum cord", "A paler lilac weave with a deep plum cord and border - soft cloth, crisp tie",
  LIL_B, LIL_S, C("#e8e0f4", "#d4c8e8", "#5c3d7a", "#3a2450", "#7a5a9a", "#e8e0f4", "#5c3d7a", "jute", "#c9bce2", "#b7a4d6"), "print", ("u-chia-seeds", "u-coriander-seeds"), dict(layout="bleed")),
 ("Pale rose, mauve border", "A paler rose weave with a cream cord and a mauve border",
  BLU_B, BLU_S, C("#f1d3cd", "#e2bbb3", "#fffaf0", "#d9c3b0", "#b07a96", "#f1d3cd", "#fffaf0", "jute", "#e0b2aa", "#d3a198"), "print", ("u-coconut-sugar", "u-himalayan-pink-salt"), dict(layout="bleed")),
 ("Mauve weave", "Halfway between the two: a mauve woven potli, cream cord and border, floating on a lilac-rose blush",
  MIX_B, MIX_S, C("#e1c3d6", "#cba8bf", "#fffaf0", "#d9c3c8", "#fffaf0", "#e1c3d6", "#fffaf0", "jute", "#cfa9c1", "#bf95b0"), "print", ("u-himalayan-pink-salt", "u-chia-seeds"), dict(layout="float")),
 ("Lilac weave, minimal", "Lilac woven potli, white cord, no border - the plainest, calmest one",
  LIL_B, SC("#fdfcff", "#efebf6", "#efebf6", "#efebf6"), C(LILAC, LILAC_D, "#ffffff", "#e3dcef", None, None, "#ffffff", "jute", LILAC_P, LILAC_D), "print", ("u-coconut-sugar", "u-chia-seeds"), dict(layout="float")),
]
if os.environ.get("MIX"):
    P = P_MIX
    OUT = OUT.replace("kit-potli-variations.html", "kit-potli-lilac-rose.html")

LIL1 = C(LILAC, LILAC_D, "#fffaf0", "#d9cbb0", "#fffaf0", LILAC, "#fffaf0", "jute", LILAC_P, LILAC_D)
P_ONE = [
 ("Rose as in potli 2", "Lilac potli as in 1; the DS mark in the site's own gold and green; SATVA and Dil Se Pure in the rose of potli 2 itself",
  LIL_B, LIL_S, LIL1, "print", ("u-coconut-sugar", "u-chia-seeds"), dict(layout="bleed", letters="#d3a198")),
 ("Deeper rose", "The same, with the letters a few shades deeper in the same rose, so they read more clearly on the lilac",
  LIL_B, LIL_S, LIL1, "print", ("u-coconut-sugar", "u-chia-seeds"), dict(layout="bleed", letters="#b56f78")),
 ("Deepest rose", "The same, with the letters in the deepest dusty rose - the clearest of the three",
  LIL_B, LIL_S, LIL1, "print", ("u-coconut-sugar", "u-chia-seeds"), dict(layout="bleed", letters="#94495a")),
]
if os.environ.get("ONE"):
    P = P_ONE
    OUT = OUT.replace("kit-potli-variations.html", "kit-potli-lilac-final.html")

COPY = ('<div class="cp"><p class="k">Healthy Grocery Kit &middot; sold only by our Sahelis</p>'
        '<h2>One kit, <em>straight from a Saheli</em></h2>'
        '<p class="d">Our Sahelis don&rsquo;t sell loose packets. Every Saheli brings the same Healthy Grocery Kit to your door &mdash; thirteen pure kitchen essentials, three of them masalas blended at home by the Sahelis themselves.</p>'
        '<a class="bt">Buy the kit</a><span class="tl">or call +91-9689888822</span></div>')

figs = []
for i, row in enumerate(P, 1):
    name, cap, b, s, p, tone, bw = row[:7]
    ex = row[7] if len(row) > 7 else {}
    u = "p%d" % i
    st = ("--bg:%s;--kick:%s;--h:%s;--em:%s;--d:%s;--btn:%s;--btnfg:%s;--tel:%s;--w1:%s;--w2:%s;--t1:%s;--t2:%s"
          % (b["bg"], b["kick"], b["h"], b["em"], b["d"], b["btn"], b["btnfg"], b["tel"], s["w1"], s["w2"], s["t1"], s["t2"]))
    cls = " wood" if s.get("wood") else ""
    cls += " darkscene" if s.get("darkscene") else ""
    tag_dark = ' style="--tg:#d9b45a;--tgi:#1a1815"' if s.get("darkscene") else ""
    scene = ('<div class="scene%s"><div class="table"></div>'
             '<div class="bowl" style="left:5%%;bottom:6%%"><img src="assets/%s.jpg" alt=""></div>'
             '<div class="bowl sm" style="right:6%%;bottom:5%%"><img src="assets/%s.jpg" alt=""></div>'
             '<div class="shadow"></div>'
             '<div class="potli">%s%s<div class="htag"%s><i></i><b>Healthy Grocery Kit</b><span>13 items</span></div></div></div>'
             % (cls, bw[0], bw[1], potli(u, **p), (lockup(tone).replace('class="lk print"', 'class="lk orig" style="--lc:%s"' % ex['letters']) if ex.get('letters') else lockup(tone)), tag_dark))
    figs.append('<figure><div class="frame" tabindex="0" role="button" aria-label="Option %d, click for full size"><div class="st%s" style="%s">%s%s</div></div>'
                '<figcaption><b>%02d</b> <strong>%s</strong> &mdash; %s</figcaption></figure>' % (i, " " + ex.get("layout", ""), st.replace('"', "'"), COPY, scene, i, name, cap))

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
figcaption strong{color:#f4efe6;font-weight:600}
.frame{position:relative;aspect-ratio:1245/569;overflow:hidden;border-radius:12px;cursor:zoom-in;outline:none}
.frame.full{position:fixed;inset:0;z-index:50;border-radius:0;aspect-ratio:auto;background:rgba(14,12,10,.92);cursor:zoom-out}
.st{position:absolute;left:0;top:0;width:1245px;height:569px;transform-origin:0 0;transform:scale(var(--s,.5));overflow:hidden;background:var(--bg)}
.frame.full .st{left:50%;top:50%;transform:translate(-50%,-50%) scale(var(--s))}
.cp{position:absolute;left:56px;top:50%;transform:translateY(-50%);width:470px}
.cp .k{font:500 12px/1.3 "Jost";letter-spacing:.26em;text-transform:uppercase;color:var(--kick)}
.cp h2{font:600 44px/1.06 "Fraunces",serif;margin:12px 0 14px;color:var(--h)}.cp h2 em{display:block;color:var(--em)}
.cp .d{font:300 16px/1.55 "Jost";color:var(--d);max-width:44ch}
.cp .bt{display:inline-block;margin-top:24px;padding:14px 28px;border-radius:999px;background:var(--btn);color:var(--btnfg);font:600 15px/1 "Jost";letter-spacing:.04em;box-shadow:0 12px 24px -14px rgba(0,0,0,.6)}
.cp .tl{margin-left:18px;font:500 15px/1 "Jost";color:var(--tel)}
.scene{position:absolute;left:600px;top:34px;width:600px;height:501px;border-radius:22px;overflow:hidden;
  background:radial-gradient(90% 85% at 32% 18%,var(--w1),var(--w2));box-shadow:0 34px 60px -30px rgba(0,0,0,.75)}
.scene::before{content:"";position:absolute;left:-10%;top:-30%;width:70%;height:90%;background:radial-gradient(closest-side,rgba(255,255,255,.55),transparent);pointer-events:none}
.darkscene::before{background:radial-gradient(closest-side,rgba(255,240,210,.12),transparent)}
.scene .table{position:absolute;left:0;right:0;bottom:0;height:29%;background:linear-gradient(180deg,var(--t1),var(--t2));
  box-shadow:inset 0 12px 18px -12px rgba(60,40,20,.45)}
.scene .table::before{content:"";position:absolute;inset:0;background-image:repeating-linear-gradient(0deg,rgba(90,70,40,.06) 0 2px,transparent 2px 4px),repeating-linear-gradient(90deg,rgba(90,70,40,.05) 0 2px,transparent 2px 5px)}
.wood .table::before{background-image:repeating-linear-gradient(0deg,rgba(50,25,5,.2) 0 1px,transparent 1px 9px)}
.darkscene .table::before{background-image:repeating-linear-gradient(0deg,rgba(255,255,255,.04) 0 1px,transparent 1px 8px)}
.shadow{position:absolute;left:50%;bottom:6.5%;width:330px;height:40px;margin-left:-165px;border-radius:50%;background:radial-gradient(closest-side,rgba(30,18,8,.5),transparent)}
.darkscene .shadow{background:radial-gradient(closest-side,rgba(0,0,0,.85),transparent)}
.bowl{position:absolute;width:96px;height:96px;border-radius:50%;overflow:hidden;border:6px solid #fffaf2;box-shadow:0 14px 20px -12px rgba(40,25,5,.7);z-index:1}
.bowl.sm{width:74px;height:74px}.bowl img{width:100%;height:100%;object-fit:cover}
.darkscene .bowl{border-color:#3d3a33}
.potli{position:absolute;left:50%;bottom:6%;width:356px;height:418px;margin-left:-178px;container-type:inline-size;z-index:2;filter:drop-shadow(0 18px 18px rgba(30,18,8,.28))}
.potli svg{width:100%;height:100%;display:block;overflow:visible}
.lk{position:absolute;left:50%;top:44%;width:38%;transform:translateX(-50%);text-align:center;container-type:inline-size;pointer-events:none}
.lk.print{mix-blend-mode:multiply}
.lk-m{display:block;width:60%;margin:0 auto}
.lk-s{display:block;font:400 22cqw/1 "Jost",sans-serif;letter-spacing:.2em;margin:5cqw 0 0 .2em;color:#4f6e47}
.lk-d{display:flex;align-items:center;justify-content:center;gap:3cqw;margin-top:3cqw}
.lk-d img{height:6.5cqw;width:auto}
.lk-d i{font:400 10cqw/1 "Jost",sans-serif;font-style:normal;color:#4f6e47}
.lk.cream .lk-s,.lk.cream .lk-d i{color:#f4ecd8}
/* true site colours for the mark (no print blend), letters in a chosen colour */
.lk.orig{mix-blend-mode:normal}.lk.orig .lk-s,.lk.orig .lk-d i{color:var(--lc)}.lk.orig .lk-s{font-weight:500}

/* open scene: no card, the potli stands in the block itself */
.st.bleed .scene{left:520px;top:0;width:725px;height:569px;border-radius:0;box-shadow:none;background:transparent}
.st.bleed .scene::before{display:none}
.st.bleed .scene .table{height:24%;-webkit-mask-image:linear-gradient(90deg,transparent,#000 22%);mask-image:linear-gradient(90deg,transparent,#000 22%)}
.st.bleed .potli{width:380px;height:446px;margin-left:-190px;bottom:7%}
/* floating: no card, no table - the potli and its shadow on the colour */
.st.float .scene{left:520px;top:0;width:725px;height:569px;border-radius:0;box-shadow:none;background:transparent}
.st.float .scene::before,.st.float .scene .table{display:none}
.st.float .potli{width:380px;height:446px;margin-left:-190px;bottom:9%}
.st.float .shadow{bottom:8%}
.htag{position:absolute;left:78%;top:43%;width:22%;padding:8% 2% 5%;background:var(--tg,#e3c595);border-radius:4px 4px 10px 10px;text-align:center;transform:rotate(-8deg);
  box-shadow:0 10px 14px -8px rgba(0,0,0,.5);clip-path:polygon(18% 0,82% 0,100% 14%,100% 100%,0 100%,0 14%)}
.htag::after{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(90,60,20,.06) 0 1px,transparent 1px 4px)}
.htag i{position:absolute;left:50%;top:5%;width:10%;aspect-ratio:1;margin-left:-5%;border-radius:50%;background:#6b4a14;box-shadow:inset 0 1px 2px rgba(0,0,0,.6)}
.htag b{display:block;font:600 4.2cqw/1.08 "Fraunces",serif;color:var(--tgi,#3a2a14)}
.htag span{display:block;font:500 3.2cqw/1.2 "Jost";letter-spacing:.1em;text-transform:uppercase;color:var(--tgi,#7a5418);margin-top:4%;opacity:.85}
"""
JS = """
function fit(){document.querySelectorAll('.frame').forEach(function(f){var full=f.classList.contains('full');
  f.style.setProperty('--s', full?Math.min(innerWidth/1245,innerHeight/569)*.96:f.clientWidth/1245);});}
addEventListener('resize',fit); fit();
document.querySelectorAll('.frame').forEach(function(f){
  function t(){var on=!f.classList.contains('full'); document.querySelectorAll('.frame.full').forEach(function(x){x.classList.remove('full')}); if(on)f.classList.add('full'); fit();}
  f.addEventListener('click',t); f.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();t();}});
});
addEventListener('keydown',function(e){if(e.key==='Escape'){document.querySelectorAll('.frame.full').forEach(function(x){x.classList.remove('full')});fit();}});
"""
html = """<!DOCTYPE html>
<html lang="en">
<!-- 14 Oct 2026. Owner, on kit-bag-variations.html: "i dont like any of the
     designs ... but this looks better [07, the cotton potli]. give me some
     better colour combinations. even if its not green, its ok, also the bag
     quality should be changed". Review page only - not linked, noindex. The
     potli redrawn with real cloth (gathered neck, folds, linen weave, twisted
     cord, tassels, woven border) in 12 colour combinations of block + potli +
     scene, at the owner's screen size (1245 x 569). Generated by
     kit-potli-variations.gen.py beside this file. -->
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..600&display=swap" rel="stylesheet">
<style>%s</style>
</head>
<body>
<header>
  <p class="k0">DS Satva &middot; kit potli review</p>
  <h1>%s</h1>
  <p>The potli you liked, redrawn so it looks like real cloth (gathered neck, soft folds, linen weave, twisted cord with tassels, woven border), in twelve colour combinations of the block, the potli and the table it stands on. Click any option to see it full size (click again or press Esc to come back). Tell me the number you like. <a href="kit-bag-variations.html">The earlier bags</a> &middot; <a href="index.html#kit">Back to the site</a></p>
</header>
<div class="grid">
%s
</div>
<script>%s</script>
</body>
</html>
""" % (("Kit Potli Lilac Final" if os.environ.get("ONE") else "Kit Potli Lilac Rose" if os.environ.get("MIX") else "Kit Potli Light 2" if os.environ.get("DIFF") else "Kit Potli Light" if os.environ.get("LIGHT") else "Kit Potli Colours"), CSS, ("The lilac potli &mdash; site-colour mark, rose letters" if os.environ.get("ONE") else "The kit potli &mdash; small woven check in lilac &amp; rose, 10 options" if os.environ.get("MIX") else "The kit potli &mdash; 12 new light looks" if os.environ.get("DIFF") else "The kit potli &mdash; 12 light colour combinations" if os.environ.get("LIGHT") else "The kit potli &mdash; 12 colour combinations"), "\n".join(figs), JS)
open(OUT, "w").write(html)
print("wrote", OUT, len(html) // 1024, "KB")
