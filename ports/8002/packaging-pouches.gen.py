#!/usr/bin/env python3
"""packaging-pouches.html - design 2 (revised, as packaging-chilli-02.html) for
each product. 15 Oct 2026. Owner: "prepare the similar cover pouches for Haldi
Powder, Coriander, Jeera, Mustard, Coriander Powder, Pink Salt".
Each pouch gets its own accent colour (name, Hindi, Net Wt.) and the colour of
the product showing through the clear back; everything else is identical."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "packaging-chilli-02.html")).read()
a = src.index('<div class="solo">'); b = src.index('</figure>', a) + 9
FIG = src[a + len('<div class="solo">'):b]
# name, small line, Hindi, accent, back colour, coarse?, ingredients, claim
P = [
 ("Red Chilli", "Powder", "लाल मिर्च पाउडर", "#b8342a", "#b8342a", False, "100% red chilli", "No added colour &middot; No preservatives"),
 ("Haldi", "Turmeric Powder", "हल्दी पाउडर", "#b8800a", "#e0a419", False, "100% turmeric", "No added colour &middot; No preservatives"),
 ("Coriander", "Powder", "धनिया पाउडर", "#5f6f22", "#a8935a", False, "100% coriander seed", "No added colour &middot; No preservatives"),
 ("Coriander", "Seeds", "साबुत धनिया", "#5f6f22", "#b9a26a", True, "100% coriander seeds", "Whole &middot; Hand-sorted &middot; Unpolished"),
 ("Jeera", "Cumin Seeds", "जीरा", "#7a4f22", "#8f7046", True, "100% cumin seeds", "Whole &middot; Hand-sorted &middot; Unpolished"),
 ("Mustard", "Seeds", "राई", "#8a5a0f", "#4a3020", True, "100% mustard seeds", "Whole &middot; Hand-sorted &middot; Unpolished"),
 ("Pink Salt", "Himalayan", "गुलाबी सेंधा नमक", "#b0566a", "#e6b0b4", True, "100% Himalayan rock salt", "Unrefined &middot; No additives"),
]
figs = []
for name, small, hi, acc, back, coarse, ing, claim in P:
    f = FIG
    f = f.replace('<span class="pnum">2</span>', '')
    f = f.replace('--acc:#b8342a', '--acc:%s' % acc)
    f = f.replace('<h3>Red Chilli<small>Powder</small></h3>', '<h3>%s<small>%s</small></h3>' % (name, small))
    f = f.replace('<p class="dv">लाल मिर्च पाउडर</p>', '<p class="dv">%s</p>' % hi)
    f = f.replace('<p class="pr">No added colour &middot; No preservatives</p>', '<p class="pr">%s</p>' % claim)
    f = f.replace('<b>Ingredients:</b> 100% red chilli', '<b>Ingredients:</b> %s' % ing)
    f = f.replace('<div class="clearside" style="--c:#b8342a"><div class="fill">', '<div class="clearside" style="--c:%s"><div class="fill%s">' % (back, " coarse" if coarse else ""))
    f = re.sub(r'<figcaption>.*?</figcaption>', '<figcaption><b>%s %s</b></figcaption>' % (name, small), f)
    figs.append('<div class="solo">' + f + '</div>')
head = src[:src.index('<body>') + 6]
head = head.replace('<title>Red Chilli Pouch</title>', '<title>SATVA Pouches</title>')
css = '''<style>.solo{margin:30px auto 0}.solo figure{break-inside:avoid}
@media print{.solo{break-after:page}}</style>'''
page = (head.replace('</head>', css + '</head>') +
        '<header class="top"><p class="k">DS Satva &middot; packaging</p><h1>Design 2 &mdash; all products</h1>'
        '<p>Red Chilli Powder as approved, and the same pouch for Haldi, Coriander Powder, Coriander Seeds, Jeera, Mustard and Pink Salt. '
        'Each has its own accent colour and its product colour through the clear back; the details block is the same on all.</p></header>'
        + "".join(figs) + '</body></html>')
open(os.path.join(HERE, "packaging-pouches.html"), "w").write(page)
print(len(figs))
