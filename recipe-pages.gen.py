#!/usr/bin/env python3
"""One page per recipe, for Google.  26 Oct 2026.

The home page shows each recipe in a pop-up, which search engines can't list on
its own. This writes ports/8002/recipes/<id>.html (plus recipes/index.html) from
the same RECIPES + RECIPE_BOOK data in js/satva.js, so the words stay the same
as the pop-up. Each page carries schema.org Recipe data.

Run again after any recipe edit in js/satva.js:
    python3 ~/dssatva/recipe-pages.gen.py
"""
import html, json, os, re, subprocess, urllib.parse

SITE = "https://dssatva.com"
SRC = os.path.expanduser("~/dssatva/ports/8002")
OUT = os.path.join(SRC, "recipes")
WA = "919689888822"
JS = os.path.join(SRC, "js", "satva.js")

# Pulses are off the site (owner, 13 Oct 2026): "Satva Toor Dal" reads "toor dal"
HIDDEN = ["Toor Dal", "Chana Dal"]
# where the site's cards name a different product than RECIPES.uses
MADE_WITH = {"chana-dal": "Chilli Powder", "varan-bhaat": "Turmeric"}
STILL = {
    "Turmeric": "u-turmeric.jpg", "Chilli Powder": "u-chilli-powder.jpg",
    "Coriander Powder": "j-coriander-3-powder.jpg", "Coriander Seeds": "u-coriander-seeds.jpg",
    "Cumin Seeds": "u-cumin-seeds.jpg", "Mustard Seeds": "u-mustard-seeds.jpg",
    "Black Pepper": "u-black-pepper.jpg", "Garam Masala": "u-garam-masala.jpg",
    "Biryani Masala": "u-biryani-masala.jpg", "Chaat Masala": "u-chaat-masala.jpg",
    "Sambar Masala": "u-sambar-masala-8002.jpg", "Chatpat / Kanda Lasun Masala": "u-chatpat-masala.jpg",
    "Chia Seeds": "u-chia-seeds.jpg", "Flax Seeds": "u-flax-seeds.jpg", "Methi Seeds": "u-methi-seeds.jpg",
    "Himalayan Pink Salt": "u-himalayan-pink-salt.jpg", "Coconut Sugar": "u-coconut-sugar.jpg",
    "Monk Fruit Sweetener": "j-monk-3-powder.jpg",
}
CSP = ("default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' "
       "https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data:; "
       "connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests")


def load():
    src = open(JS, encoding="utf-8").read()
    a = src.index("var RECIPES = [")
    b = src.index("\n  ];", a) + 4
    c = src.index("var RECIPE_BOOK = {")
    d = src.index("\n  };", c) + 4
    code = ('var POT="",PAN="",RICE="";' + src[a:b] + ";" + src[c:d] + ";" +
            "process.stdout.write(JSON.stringify({r:RECIPES,b:RECIPE_BOOK}))")
    data = json.loads(subprocess.check_output(["node", "-e", code]))
    return [r for r in data["r"] if r["id"] in data["b"]], data["b"]


def photo(r):
    for name in ("rec-" + r["id"] + ".jpg", "recipe-" + r["id"] + ".jpg"):
        if os.path.exists(os.path.join(SRC, "assets", name)):
            return name
    if r["id"] == "sambar":
        return "rec-idli-sambar.jpg"
    return STILL[r["uses"]]


def iso_time(t):
    """"1 hr 30 min" -> PT1H30M; "+ a night" can't be counted, so None."""
    if "night" in t:
        return None
    h = sum(int(x) for x in re.findall(r"(\d+)\s*hr", t))
    m = sum(int(x) for x in re.findall(r"(\d+)\s*min", t))
    h, m = h + m // 60, m % 60
    return "PT" + (f"{h}H" if h else "") + (f"{m}M" if m else "") if (h or m) else None


def clean(s):
    for p in HIDDEN:
        s = s.replace("Satva " + p, p.lower())
    return s


def e(s):
    return html.escape(s, quote=True)


STYLE = """
:root{--ink:#1e2c16;--green:#2c4220;--sand:#e8dcc6;--ivory:#f4f3e7;--gold:#7f5a0f;--line:#d6c8ab}
*{box-sizing:border-box}
body{margin:0;background:var(--ivory);color:var(--ink);font-family:Jost,sans-serif;line-height:1.65;font-size:17px}
a{color:var(--green);text-underline-offset:2px}
.top{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:12px 24px;background:var(--sand);border-bottom:1px solid var(--line)}
.top img{height:48px;width:auto;display:block}
.top nav{font-size:.9rem;letter-spacing:.06em;text-transform:uppercase}
.top nav a{margin-left:18px;text-decoration:none}
main{max-width:1120px;margin:0 auto;padding:28px 24px 48px}
.crumbs{font-size:.85rem;margin:0 0 18px;color:#4e6848}
.crumbs a{color:inherit}
.rec{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,6fr);gap:40px;align-items:start}
.shot{position:sticky;top:20px;margin:0}
.shot img{width:100%;height:auto;aspect-ratio:4/5;object-fit:cover;border-radius:14px;display:block;background:var(--sand)}
h1{font-family:Fraunces,serif;font-weight:500;font-size:2.4rem;line-height:1.1;margin:0}
.hi{font-family:"Tiro Devanagari Hindi",serif;font-size:1.25rem;color:#4e6848;margin:4px 0 12px}
.facts{display:flex;flex-wrap:wrap;gap:8px 20px;margin:0 0 14px;padding:0;list-style:none;font-size:.95rem}
.facts b{font-weight:500}
.lead{margin:0 0 20px}
h2{font-family:Fraunces,serif;font-weight:500;font-size:1.35rem;margin:26px 0 8px}
.ing{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.ing li{display:flex;gap:14px;padding:7px 0;border-bottom:1px solid var(--line)}
.ing .q{flex:0 0 7.5em;font-weight:500}
.ing .ours{color:var(--green);font-weight:500}
.ing .ours::after{content:"SATVA";font-size:.62rem;letter-spacing:.12em;margin-left:8px;padding:1px 6px;border-radius:9px;background:var(--green);color:var(--ivory);vertical-align:2px}
.steps{margin:0;padding-left:1.3em}
.steps li{margin:0 0 10px;padding-left:4px}
.order{display:inline-block;margin:24px 0 0;padding:12px 22px;border-radius:999px;background:var(--green);color:var(--ivory);text-decoration:none;font-weight:500}
.more{margin-top:44px;border-top:1px solid var(--line);padding-top:6px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:18px;list-style:none;margin:12px 0 0;padding:0}
.cards a{text-decoration:none;color:var(--ink);display:block}
.cards img{width:100%;height:auto;aspect-ratio:1/1;object-fit:cover;border-radius:12px;display:block;background:var(--sand)}
.cards b{display:block;font-family:Fraunces,serif;font-weight:500;font-size:1.05rem;margin-top:6px;line-height:1.25}
.cards span{font-size:.85rem;color:#4e6848}
footer{background:var(--green);color:#efece5;padding:24px;font-size:.9rem;text-align:center;line-height:1.7}
footer a{color:#f7eccf}
@media (max-width:760px){
  body{font-size:16px}
  .top{padding:10px 16px}.top img{height:40px}.top nav{font-size:.78rem}.top nav a{margin-left:10px}
  main{padding:20px 16px 40px}
  .rec{grid-template-columns:1fr;gap:20px}
  .shot{position:static}.shot img{aspect-ratio:4/3}
  h1{font-size:1.9rem}
  .ing .q{flex-basis:6.5em}
  .cards{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
}
"""


def page(title, desc, canon, img, ld, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<!-- Made by ~/dssatva/recipe-pages.gen.py from js/satva.js. Edit the recipe there, then run it again. -->
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="DS Satva Foods">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2c4220">
<link rel="icon" type="image/png" href="../assets/mark-dark.png">
<link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..600&family=Jost:wght@300..500&family=Tiro+Devanagari+Hindi&display=swap" rel="stylesheet">
<style>{STYLE}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="top">
  <a href="../"><img src="../assets/logo-stack-dark-sm.png" alt="DS Satva Foods home" width="400" height="241"></a>
  <nav aria-label="Main"><a href="../">Home</a><a href="./">Recipes</a><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a></nav>
</header>
<main>
{body}
</main>
<footer>
  DS Satva Foods Pvt Ltd, Plot No.-31W, MIDC Chikalthana, Chhatrapati Sambhaji Nagar, Maharashtra -431001<br>
  <a href="tel:+919689888822">+91-9689888822</a> · <a href="mailto:dssatva@gmail.com">dssatva@gmail.com</a> · FSSAI Lic. No. 21526044005691<br>
  <a href="../privacy.html">Privacy</a> · <a href="../credits.html">Photo credits</a>
</footer>
</body>
</html>
"""


def card(r, here=""):
    return (f'<li><a href="{here}{r["id"]}.html"><img src="../assets/{photo(r)}" alt="{e(r["name"])}" '
            f'loading="lazy" width="400" height="400"><b>{e(r["name"])}</b><span>{e(r["time"])}</span></a></li>')


def recipe_page(r, b, all_r):
    made = MADE_WITH.get(r["id"], r["uses"])
    canon = f"{SITE}/recipes/{r['id']}.html"
    img = photo(r)
    ings = [(q, clean(t)) for q, t in b["ing"]]
    ld = {
        "@context": "https://schema.org", "@type": "Recipe",
        "name": r["name"], "alternateName": r["hi"], "description": r["desc"],
        "image": [f"{SITE}/assets/{img}"],
        "author": {"@type": "Organization", "name": "DS Satva Foods", "url": SITE + "/"},
        "publisher": {"@id": SITE + "/#business"},
        "recipeYield": f'{b["serves"]} servings', "recipeCuisine": "Indian",
        "recipeCategory": "Drink" if r["id"] in ("haldi-doodh", "nimbu-pani") else
                          "Dessert" if r["id"] in ("kheer", "shrikhand", "chia") else "Main course",
        "keywords": f'{r["name"]}, {r["hi"]}, Satva {made}, Maharashtrian recipe',
        "recipeIngredient": [f"{q} {t}" for q, t in ings],
        "recipeInstructions": [{"@type": "HowToStep", "text": s} for s in b["steps"]],
    }
    t = iso_time(r["time"])
    if t:
        ld["totalTime"] = t
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Recipes", "item": SITE + "/recipes/"},
        {"@type": "ListItem", "position": 3, "name": r["name"], "item": canon}]}
    li = "\n".join(
        f'      <li><span class="q">{e(q)}</span><span{" class=\"ours\"" if t.startswith("Satva ") else ""}>'
        f'{e(t[6:] if t.startswith("Satva ") else t)}</span></li>' for q, t in ings)
    steps = "\n".join(f"      <li>{e(s)}</li>" for s in b["steps"])
    order = urllib.parse.quote(f"Namaskar! I would like to order Satva {made} (from the {r['name']} recipe).")
    others = [o for o in all_r if o["id"] != r["id"]]
    pick = [o for o in others if MADE_WITH.get(o["id"], o["uses"]) == made][:2]
    pick += [o for o in others if o not in pick][: 4 - len(pick)]
    body = f"""  <p class="crumbs"><a href="../">Home</a> › <a href="./">Recipes</a> › {e(r["name"])}</p>
  <article class="rec">
    <figure class="shot"><img src="../assets/{img}" alt="{e(r["name"])}" width="800" height="1000" fetchpriority="high"></figure>
    <div>
      <h1>{e(r["name"])}</h1>
      <p class="hi" lang="mr">{e(r["hi"])}</p>
      <ul class="facts"><li><b>Time</b> {e(r["time"])}</li><li><b>Serves</b> {e(b["serves"])}</li><li><b>Made with</b> Satva {e(made)}</li></ul>
      <p class="lead">{e(r["desc"])}</p>
      <h2>Ingredients</h2>
      <ul class="ing">
{li}
      </ul>
      <h2>Method</h2>
      <ol class="steps">
{steps}
      </ol>
      <a class="order" href="https://wa.me/{WA}?text={order}" target="_blank" rel="noopener">Order Satva {e(made)} on WhatsApp</a>
    </div>
  </article>
  <section class="more" aria-labelledby="more-h">
    <h2 id="more-h">More recipes</h2>
    <ul class="cards">
      {"".join(card(o) for o in pick)}
    </ul>
  </section>"""
    title = f'{r["name"]} recipe ({r["hi"]}) | DS Satva Foods'
    desc = r["desc"] if len(r["desc"]) <= 160 else r["desc"][:157].rsplit(" ", 1)[0] + "…"
    ld_all = [ld, crumbs]
    return page(title, desc, canon, f"{SITE}/assets/{img}", ld_all, body)


def index_page(all_r):
    groups = [("masala", "With our masalas"), ("seed", "With our seeds & essentials")]
    secs = ""
    for g, label in groups:
        rs = [r for r in all_r if r["group"] == g]
        secs += (f'  <section aria-labelledby="g-{g}"><h2 id="g-{g}">{label}</h2>\n'
                 f'    <ul class="cards">\n      ' + "\n      ".join(card(r) for r in rs) + "\n    </ul>\n  </section>\n")
    ld = {"@context": "https://schema.org", "@type": "ItemList", "name": "Recipes from DS Satva Foods",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/recipes/{r['id']}.html"}
                              for i, r in enumerate(all_r)]}
    body = f"""  <p class="crumbs"><a href="../">Home</a> › Recipes</p>
  <h1>Recipes</h1>
  <p class="lead">Everyday Maharashtrian and Indian home cooking, each made with something from the Satva shelf. Ordinary household measures, cups and spoons.</p>
{secs}"""
    return page("Recipes made with Satva spices and seeds | DS Satva Foods",
                "Home recipes made with Satva spices, masalas and seeds: misal, varan bhaat, biryani, bharli vangi, jeera bhaat, javas chutney and more.",
                f"{SITE}/recipes/", f"{SITE}/assets/og-dssatva.jpg", ld, body)


def main():
    rs, book = load()
    os.makedirs(OUT, exist_ok=True)
    for r in rs:
        open(os.path.join(OUT, r["id"] + ".html"), "w", encoding="utf-8").write(recipe_page(r, book[r["id"]], rs))
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(index_page(rs))
    print(len(rs), "recipe pages + index in", OUT)
    return rs


if __name__ == "__main__":
    main()
