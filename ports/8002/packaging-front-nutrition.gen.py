#!/usr/bin/env python3
"""packaging-front-nutrition.html - 15 ways to fit the nutrition chart on the
PRINTED FRONT of the design-2 pouch (Garam Masala). 15 Oct 2026. Owner: "any
possibility of having the nutritional value chart on this side itself ... 15
variations". Draft values (typical garam masala) until lab-tested."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "packaging-chilli-02.html")).read()
STYLE = src[src.index("<style>") + 7:src.index("</style>")]
ACC = "#7d5630"
ROWS = [("Energy", "300 kcal", "0.3%", "", 0), ("Protein", "12 g", "&ndash;", "", 0), ("Carbohydrate", "40 g", "&ndash;", "", 0),
        ("Total Sugars", "3 g", "&ndash;", "", 1), ("Added Sugars", "0 g", "0%", "", 1),
        ("Total Fat", "10 g", "0.3%", "", 0), ("Saturated Fat", "2 g", "0.2%", "", 1), ("Trans Fat", "0 g", "0%", "", 1),
        ("Sodium", "70 mg", "0.1%", "", 0)]
KEY = [("Energy", "300", "kcal"), ("Protein", "12", "g"), ("Carbs", "40", "g"), ("Sugars", "3", "g"), ("Fat", "10", "g"), ("Sodium", "70", "mg")]

def table(cls="", cols=4, rows=ROWS):
    hd = "<tr><th>Nutrition</th><th>Per 100 g</th>" + ("<th>%RDA*</th>" if cols == 4 else "") + "</tr>"
    body = "".join("<tr class='%s'><td>%s</td><td>%s</td>%s</tr>" % ("sub" if r[4] else "", r[0], r[1], ("<td>%s</td>" % r[2]) if cols == 4 else "") for r in rows)
    foot = "<p class='nf'>*per 2 g serve, 2000 kcal diet</p>" if cols == 4 else "<p class='nf'>Serve 2 g (1 tsp)</p>"
    return "<div class='nt %s'><table>%s%s</table>%s</div>" % (cls, hd, body, foot)

def table2col():
    half = (len(ROWS) + 1) // 2
    def t(rr): return "<table>" + "".join("<tr class='%s'><td>%s</td><td>%s</td></tr>" % ("sub" if r[4] else "", r[0], r[1]) for r in rr) + "</table>"
    return ("<div class='nt two'><p class='nh'>Nutrition per 100 g</p><div class='cols'>%s%s</div>"
            "<p class='nf'>Serve 2 g (1 tsp)</p></div>" % (t(ROWS[:half]), t(ROWS[half:])))

BARS = ("<div class='bars'><p class='ch-h'>Nutrition per 100 g</p><div class='bx'>"
        "<div class='big'><b>300</b><i>kcal</i><em>Energy</em></div><div class='bl'>"
        + "".join("<div class='br'><span>%s</span><div class='trk'><i style='width:%d%%'></i></div><b>%s g</b></div>" % (n, w, v)
                  for n, w, v in (("Carbs", 80, "40"), ("Protein", 24, "12"), ("Fat", 20, "10"), ("Sugars", 6, "3")))
        + "</div><div class='big'><b>70</b><i>mg</i><em>Sodium</em></div></div>"
        "<p class='nf'>Sat. fat 2 g &middot; Trans fat 0 g &middot; Added sugars 0 g &middot; Per 2 g serve: 6 kcal, 0.3% RDA*</p></div>")

def chips(cls=""):
    return ("<div class='chips %s'><p class='ch-h'>Per 100 g</p><div class='row'>%s</div></div>"
            % (cls, "".join("<span><b>%s<i>%s</i></b><em>%s</em></span>" % (v, u, n) for n, v, u in KEY)))

DS = '<img class="dsbig" style="height:%dpx" src="assets/logo-stack-dark.png" alt="DS SATVA">'
NAME = '<div class="nm sm"><h3>Garam Masala</h3><p class="dv">गरम मसाला</p></div>'
NAME_S = '<div class="nm sm xs"><h3>Garam Masala</h3><p class="dv">गरम मसाला</p></div>'
SAH = '<div class="sbig"><img src="assets/saheli-mark-grad.svg" alt=""><b>Satva <span>Saheli</span></b></div>'
SAH_ROW = '<div class="sahrow"><img src="assets/saheli-mark-grad.svg" alt=""><div><b>Satva <span>Saheli</span></b></div></div>'
WEB = '<p class="sweb s"><b>www.dssatva.com</b></p>'
WEB_S = '<p class="sweb s"><b>www.dssatva.com</b></p>'
CLAIM = ''
WT = '<p class="wt c">Net Wt. <b>100 g</b></p>'
CW = '<p class="wt c cwl">Net Wt. <b>100 g</b></p>'
LEG = ('<div class="legal l2"><p><b>Ingredients:</b> Cumin, black pepper, cinnamon, clove, cardamom, bay leaf, mace</p>'
       '<p><b>MRP</b> &#8377;_____ (incl. of all taxes)</p>'
       '<p><b>FSSAI</b> Lic. No. 21526044005691</p>'  # 21 Oct 2026: veg mark moved off this line to the top-left of the front
       '<p>Packed &amp; Marketed by <b>DS Satva Foods Pvt Ltd,</b> 31W, MIDC Chikalthana, Chhatrapati Sambhajinagar</p>'
       '<p>dssatva@gmail.com</p></div>')
BAT = '<div class="legal r2"><p><b>Batch</b> <span class="fill2"></span></p><p><b>Packed</b> <span class="fill2"></span></p><p><b>Best before</b> <span class="fill2"></span></p></div>'
BATROW = '<div class="batrow"><span><b>Batch</b></span><span><b>Packed</b></span><span><b>Best before</b></span></div>'
FT = '<div class="ft ft2">' + LEG + BAT + '</div>'

def pouch(inner, cls=""):
    return '<div class="pk pouch %s" style="--bg:#f6efe2;--ink:#1e2c16;--acc:%s"><span class="vegmark" title="Vegetarian"><i></i></span>%s</div>' % (cls, ACC, inner)

V = [
 ("Chart in the middle, Saheli as a row", "The full chart takes the centre; the Satva Saheli logo moves to a slim row under the name.",
  pouch(DS % 40 + NAME_S + SAH_ROW + table("c4") + CW + FT)),
 ("Chart beside the details", "The bottom band splits: details on the left, a compact chart on the right; Batch, Packed and Best before become a strip along the foot.",
  pouch(DS % 36 + NAME_S + SAH + WEB_S + CW + '<div class="ft ft3">' + LEG + table("mini", 2) + '</div>' + BATROW)),
 ("Key-figure chips", "Five round chips (energy, protein, carbs, fat, sodium per 100 g) above the net weight - the quickest read.",
  pouch(DS % 42 + NAME_S + SAH + WEB_S + chips() + CW + FT)),
 ("Chips + Saheli row", "Chips in the centre, Saheli as a row - more air around everything.",
  pouch(DS % 44 + NAME + SAH_ROW + WEB_S + chips("big") + CW + FT)),
 ("Chart left, Saheli right", "The middle splits in two: the full chart on the left, the Saheli logo stacked on the right.",
  pouch(DS % 40 + NAME_S + '<div class="split">' + table("c2l", 2) + '<div class="sp-r">' + SAH + WEB_S + '</div></div>' + CW + FT)),
 ("Saheli left, chart right", "The mirror image: Saheli on the left, chart on the right.",
  pouch(DS % 40 + NAME_S + '<div class="split">' + '<div class="sp-r">' + SAH + WEB_S + '</div>' + table("c2l", 2) + '</div>' + CW + FT)),
 ("Compact chart under Saheli", "A five-line chart (energy, protein, carbs, fat, sodium) between the Saheli line and the claim.",
  pouch(DS % 38 + NAME_S + SAH + WEB_S + table("c5", 4, [r for r in ROWS if r[0] in ("Energy", "Protein", "Carbohydrate", "Total Fat", "Sodium")]) + CW + FT)),
 ("Chart in a framed card", "The full chart in a rounded card with a brown header bar.",
  pouch(DS % 32 + NAME_S + SAH_ROW + table("card") + CW + FT)),
 ("Chart on a brown band", "The chart sits on a full-width brown band across the pouch - bold and easy to find.",
  pouch(DS % 38 + NAME_S + SAH_ROW + table("band", 2) + CW + FT)),
 ("Bar chart", "A small visual chart: bars for carbs, protein, fat and sugars per 100 g, with energy and sodium as figures, and the %RDA line underneath.",
  pouch(DS % 40 + NAME + SAH_ROW + WEB_S + BARS + CW + FT)),
 ("Energy badge + chips", "A round '6 kcal per serve' badge by the logo, with the chips below.",
  pouch('<div class="toprow">' + DS % 44 + '<div class="ebadge"><b>6</b><i>kcal</i><em>per 2 g serve</em></div></div>' + NAME_S + SAH + WEB_S + chips() + CW + FT)),
 ("Net weight up top, chart below", "Net weight moves to a badge at the top, freeing room for the full chart under Saheli.",
  pouch('<div class="toprow">' + DS % 40 + '<div class="wbadge">Net Wt.<b>100 g</b></div></div>' + NAME_S + SAH_ROW + table("c4") + CLAIM + FT)),
 ("Two-column chart", "The chart split into two side-by-side columns so it stays short.",
  pouch(DS % 34 + NAME_S + SAH + WEB_S + table2col() + CW + FT)),
 ("Chart across the foot", "The chart runs full width just above a one-line details block; Batch boxes in a strip.",
  pouch(DS % 34 + NAME_S + SAH_ROW + WEB_S + CW + table("foot", 2) + '<div class="ft ft4">' + LEG + '</div>' + BATROW)),
 ("Minimal: chips and Saheli in the footer", "Logo, name and chips up top; the Saheli logo joins the details in the footer.",
  pouch(DS % 46 + NAME + chips("big") + CW + '<div class="ft ft5">' + SAH_ROW + '</div>' + FT)),
]

CSS = STYLE + r"""
.grid{max-width:1500px;margin:30px auto 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(420px,1fr));gap:40px 26px}
.cell{display:flex;flex-direction:column;align-items:center}
.cell .stage{height:auto;padding:26px 0;cursor:default}
.cell .pouch{zoom:1.5}
.cell figcaption{max-width:420px}
.pouch{padding-top:22px}
.pouch .nm{margin-top:8px}
.nm.sm h3{font-size:25px}.nm.xs h3{font-size:22px}.nm.xs h3 small{font-size:9.5px;margin-top:3px}.nm.xs .dv{font-size:11.5px;margin-top:3px}
.pouch .sbig{margin-top:6px;gap:2px}.pouch .sbig img{width:28px}.pouch .sbig b{font-size:13px}.pouch .sbig i{font-size:8.5px}
.sweb{margin-top:5px;padding:2px 8px;border-radius:99px;border:.6px solid color-mix(in srgb,var(--acc) 45%,transparent);font:500 6.2px/1.3 "Jost";color:var(--ink)}
.sbig .sweb b,.sweb b{display:inline;font:700 6.2px/1.3 "Jost";letter-spacing:0;text-transform:none;color:var(--acc)}
.sweb.s{margin-top:4px;padding:1.5px 7px;font-size:5.8px}.sweb.s b{font-size:5.8px}
.sahrow{display:flex;align-items:center;justify-content:center;gap:6px;margin-top:6px;flex:none}
.sahrow img{width:22px}.sahrow div{text-align:left}
.sahrow b{display:block;font:600 10.5px/1 "Fraunces",serif;letter-spacing:.08em;text-transform:uppercase;color:var(--ink)}.sahrow b span{color:var(--acc)}
.sahrow i{display:block;font:italic 400 7px/1.2 "Fraunces",serif;color:var(--acc);margin-top:1px}
.cw{margin-top:auto;display:flex;justify-content:space-between;align-items:baseline;width:100%;font:500 6.4px/1 "Jost";letter-spacing:.1em;text-transform:uppercase;color:var(--ink);padding:0 2px}
.cw b{font-weight:700;color:var(--acc);font-size:9px}
.cw span:last-child{font-size:8px;font-weight:600}
/* nutrition table */
.nt{width:100%;margin-top:6px;flex:none;text-align:left}
.nt table{width:100%;border-collapse:collapse;font:400 5.3px/1.2 "Jost";color:var(--ink)}
.nt th{font-weight:700;text-align:right;padding:1.2px 0;border-bottom:.8px solid var(--ink);border-top:1.2px solid var(--ink)}
.nt th:first-child,.nt td:first-child{text-align:left}
.nt th span{font-weight:400;font-size:4.6px}
.nt td{text-align:right;padding:.9px 0;border-bottom:.3px solid color-mix(in srgb,var(--ink) 25%,transparent)}
.nt tr.sub td:first-child{padding-left:5px}
.nt tr:first-of-type td{font-weight:700}
.nf{font:400 4.4px/1.2 "Jost";margin:1.5px 0 0;opacity:.8;text-align:left}
.nt.card{background:#fffaf2;border:.7px solid color-mix(in srgb,var(--acc) 40%,transparent);border-radius:6px;padding:0 5px 3px;overflow:hidden}
.nt.card th{background:var(--acc);color:#fff8ea;border:0;padding:2px 3px}.nt.card th:first-child{border-radius:0}
.nt.card table{margin:0 -5px;width:calc(100% + 10px);font-size:5px}.nt.card td{padding:.9px 5px}.nt.card th{padding:2px 5px}
.nt.band{width:calc(100% + 40px);margin-left:-20px;margin-right:-20px;background:var(--acc);padding:4px 20px 3px}
.nt.band table,.nt.band .nf{color:#fff8ea}.nt.band th{border-color:#fff8ea}.nt.band td{border-bottom-color:rgba(255,248,234,.3)}
.nt.mini table{font-size:4.9px}.nt.mini{margin-top:0}
.nt.c5 table{font-size:5.8px}
.nt.side{position:absolute;right:8px;top:62px;width:76px;margin:0}
.nt.side table{font-size:4.9px}
.hasside{align-items:flex-start}
.hasside .sidecol{width:150px;display:flex;flex-direction:column;align-items:center;flex:1 1 auto;min-height:0}
.hasside .ft{margin-top:6px;align-self:center}
.nt.foot{margin-top:6px}.nt.foot table{font-size:5px}
.nt.two .nh{font:700 6px/1 "Jost";letter-spacing:.06em;text-transform:uppercase;margin:0 0 2px;border-bottom:1px solid var(--ink);padding-bottom:1.5px}
.nt.two .nh span{font-weight:400;text-transform:none;letter-spacing:0;font-size:4.8px}
.nt.two .cols{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.split{display:grid;grid-template-columns:1.15fr .85fr;gap:8px;width:100%;align-items:center;margin-top:6px;flex:none}
.split .nt{margin:0}.split .sp-r{display:flex;flex-direction:column;align-items:center}
.split .sp-r .sbig{margin:0}.split .sp-r .sweb{font-size:5px;padding:1.5px 4px}.split .sp-r .sweb b{font-size:5px}
.split .sp-r .sbig i{font-size:7px}
/* chips */
.chips{width:100%;margin-top:7px;flex:none}
.chips .ch-h{font:600 5.4px/1 "Jost";letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin:0 0 3px}
.chips .row{display:flex;justify-content:space-between;gap:3px}
.chips span{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;aspect-ratio:1;border-radius:50%;border:.8px solid var(--acc);background:#fffaf2}
.chips b{font:700 9px/1 "Jost";color:var(--ink)}.chips b i{font:500 5px/1 "Jost";font-style:normal;margin-left:1px}
.chips em{font:500 4.6px/1 "Jost";font-style:normal;letter-spacing:.06em;text-transform:uppercase;color:var(--acc);margin-top:1.5px}
.chips.big b{font-size:10.5px}.chips.big em{font-size:5px}
/* bar chart */
.bars{width:100%;margin-top:8px;flex:none}
.bars .ch-h{font:600 5.6px/1 "Jost";letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin:0 0 4px}
.bars .bx{display:flex;align-items:center;gap:6px;border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);padding:4px 0}
.bars .big{flex:0 0 38px;text-align:center}.bars .big b{display:inline;font:700 13px/1 "Jost";color:var(--ink)}
.bars .big i{font:500 5.4px/1 "Jost";font-style:normal}.bars .big em{display:block;font:500 4.8px/1 "Jost";font-style:normal;letter-spacing:.08em;text-transform:uppercase;color:var(--acc);margin-top:2px}
.bars .bl{flex:1;display:flex;flex-direction:column;gap:2.5px}
.bars .br{display:grid;grid-template-columns:26px 1fr 22px;align-items:center;gap:4px;font:500 5.4px/1 "Jost";color:var(--ink)}
.bars .br b{font-weight:700;text-align:right}
.bars .trk{height:4px;border-radius:2px;background:color-mix(in srgb,var(--acc) 18%,transparent)}
.bars .trk i{display:block;height:100%;border-radius:2px;background:var(--acc)}
.bars .nf{margin-top:2px}
/* top row badges */
.toprow{display:flex;align-items:center;justify-content:center;gap:14px;flex:none}
.ebadge,.wbadge{width:46px;height:46px;border-radius:50%;background:var(--acc);color:#fff8ea;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.ebadge b{font:700 15px/1 "Jost"}.ebadge i{font:500 6px/1 "Jost";font-style:normal}.ebadge em{font:400 4.4px/1.1 "Jost";font-style:normal;margin-top:1px;max-width:36px}
.wbadge{font:500 5.4px/1 "Jost";letter-spacing:.08em;text-transform:uppercase}.wbadge b{font:700 11px/1 "Jost";margin-top:2px;letter-spacing:0}
/* footers */
.ft.ft3{grid-template-columns:1.25fr 1fr;align-items:start}
.ft.ft4,.ft.ft5{grid-template-columns:1fr;margin-top:5px}
.ft.ft5{border-top:0;padding-top:0}.ft.ft5 .sahrow{margin:0 auto}
.batrow{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;width:100%;margin-top:4px;font:400 5px/1 "Jost";color:var(--ink)}
.batrow span{border-bottom:.6px solid color-mix(in srgb,var(--ink) 45%,transparent);padding-bottom:6px}.batrow b{font-weight:600}
.legal.l2{font-size:5.2px;line-height:1.35}
.cwl{margin-top:auto!important;white-space:nowrap;font-size:10px}.cwl b{font-size:11px}
.nt table{font-size:6px}.nt th{white-space:nowrap}.nt td{white-space:nowrap}
.sweb.s{white-space:nowrap}
.sahrow b{white-space:nowrap}
.legal.r2 p{margin-bottom:2px}

/* "not too small also" - bigger type now that the front is trimmed */
.legal.l2{font-size:6.2px!important;line-height:1.35}
.legal.r2{font-size:6.2px}
.nt table{font-size:7.2px}.nt th{padding:1.6px 0}.nt td{padding:1.2px 0}
.nt.mini table,.nt.side table{font-size:6px}.nt.foot table{font-size:6.6px}.nt.c5 table{font-size:7.6px}
.nt.card table{font-size:6.6px}
.nf{font-size:5.2px}
.nt.two .nh{font-size:7px}
.chips .ch-h,.bars .ch-h{font-size:6.6px}
.chips b{font-size:11px}.chips.big b{font-size:12.5px}.chips em{font-size:5.6px}.chips.big em{font-size:5.8px}.chips b i{font-size:6px}
.bars .br{font-size:6.8px;grid-template-columns:32px 1fr 26px}.bars .trk{height:5px}.bars .big b{font-size:16px}.bars .big i{font-size:6.6px}.bars .big em{font-size:5.6px}.bars .big{flex-basis:46px}
.sweb.s,.sweb.s b{font-size:6.8px}
.sahrow b{font-size:12px}.sahrow img{width:26px}
.batrow{font-size:6.2px}
@media print{@page{size:A4;margin:10mm}body{background:#fff;padding:0}header.top{display:none}.grid{grid-template-columns:repeat(2,1fr);gap:16px}.cell .pouch{zoom:1.15}.cell{break-inside:avoid}}
"""
cells = []
for i, (n, cap, html) in enumerate(V, 1):
    cells.append('<figure class="cell"><div class="stage">%s</div><figcaption><b>%02d &middot; %s</b>%s</figcaption></figure>' % (html, i, n, cap))
page = """<!DOCTYPE html><html lang="en">
<!-- 15 Oct 2026. Owner: "any possibility of having the nutritional value chart on
     this side itself ... 15 variations". Review page only, noindex. Generated by
     packaging-front-nutrition.gen.py. Values are DRAFT (typical garam masala). -->
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Front Nutrition Options</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600&family=Jost:wght@300..700&family=Tiro+Devanagari+Hindi&display=swap" rel="stylesheet">
<style>%s</style></head><body>
<header class="top"><p class="k">DS Satva &middot; packaging</p><h1>Nutrition chart on the front &mdash; 15 layouts</h1>
<p>Garam Masala, design 2, nutrition on the printed front - trimmed to the essentials: no subtitle, no tagline, no claim line, short web address, and only the nutrients FSSAI asks for. Every layout keeps the logo, name, Satva Saheli, the website line, the full details and the Batch / Packed / Best before space. Values are draft figures until your lab report.</p></header>
<div class="grid">%s</div></body></html>""" % (CSS, "".join(cells))
open(os.path.join(HERE, "packaging-front-nutrition.html"), "w").write(page)
print("ok")
