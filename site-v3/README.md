# DS SATVA — website

Static site. No build step, no dependencies. Open `index.html` in a browser to preview,
or upload the whole `site/` folder to any host.

```
site/
  index.html          all the page copy lives here
  css/satva.css       palette + layout
  js/satva.js         product list, hero slider, scroll reveal
  assets/             logos + photos (generated from DS_STICKER.pdf)
```

## Palette

Measured from the brand sticker (`Label_31.08.26`), not invented:

| Token | Hex | Where it comes from |
|---|---|---|
| `--gold` | `#bf8a17` | the D and the wheat sprigs |
| `--sage` | `#55714e` | the S and the SATVA wordmark |
| `--band` | `#3c5128` | the deep green footer band |
| `--cream` | `#faf7f2` | the label background |
| `--chilli` | `#9d0f05` | the chilli powder in the photo |
| `--turmeric` | `#fdbc01` | the turmeric in the photo |

Fonts: **Fraunces** (headings, with the SOFT + WONK axes turned up), **Jost** (text),
**Tiro Devanagari Hindi** (the Hindi names).

## Product photos

The range is listed in `PRODUCTS` at the top of `js/satva.js`. A card shows a real
photo if the file at its `img` path exists, and a designed colour tile if it does
not — so adding a photo is a file drop, no code edit. Save a **square** image,
680x680 or larger.

The "Photo coming" pill was removed from the cards: with most of the range still
un-photographed it read as an unfinished site to a buyer. **This list is now the
only record of what is missing** — keep it current.

A tile is an honest placeholder but it does not sell. Photograph the products in
daylight on a plain sheet with a phone; that is enough at this size, and the same
shots are needed for the labels anyway. If stock photography is used in the
meantime, a shot of **loose ingredients** is a truthful depiction of the
ingredient — a shot of a **branded pouch** is not ours and must never be used.

Already photographed (real crops of the spice photo on the label):

| Product | File | Note |
|---|---|---|
| Turmeric | `assets/p-haldi.jpg` | the actual spice |
| Chilli Powder | `assets/p-mirchi.jpg` | the actual spice |
| Coriander Powder | `assets/p-dhane.jpg` | the actual spice |
| Garam Masala | `assets/p-garam.jpg` | a ground brown masala - representative, not a shot of our own pack |
| Biryani Masala | `assets/p-biryani.jpg` | whole cardamom and cinnamon - the ingredients, not the ground blend |
| Flax Seeds | `assets/p-flax.jpg` | CC0 stock, loose seed in a wooden bowl - see Sourced photos below |
| Quinoa | `assets/p-quinoa.jpg` | CC0 stock, loose grain - see Sourced photos below |

Replace those last two first when you have real pack shots.

Still needed:

16 of the 23 products. The Shelf column is the shelf as of 16 Sep 2026 — Spices,
Pulses, Seeds, Healthy Essentials — with the old six-way shelf in brackets, since
that finer split still lives in each product's `cat` field.

| Product | Save the photo as | Shelf |
|---|---|---|
| Kanda Lasun Masala | `assets/p-kandalasun.jpg` | Spices (blend) |
| Meat Masala | `assets/p-meat.jpg` | Spices (blend) |
| Chaat Masala | `assets/p-chaat.jpg` | Spices (blend) |
| Chatpat Masala | `assets/p-chatpat.jpg` | Spices (blend) |
| Cumin Seeds | `assets/p-jeera.jpg` | Spices (whole) |
| Mustard Seeds | `assets/p-rai.jpg` | Spices (whole) |
| Fenugreek Seeds | `assets/p-methi.jpg` | Spices (whole) |
| Toor Dal | `assets/p-toor.jpg` | Pulses |
| Chana Dal | `assets/p-chana.jpg` | Pulses |
| Chia Seeds | `assets/p-chia.jpg` | Seeds |
| Himalayan Pink Salt | `assets/p-pinksalt.jpg` | Healthy Essentials (pantry) |
| Unprocessed Sugar | `assets/p-khandsari.jpg` | Healthy Essentials (pantry) |
| Groundnut Oil | `assets/p-groundnutoil.jpg` | Healthy Essentials (oils) |
| Sesame Oil | `assets/p-sesameoil.jpg` | Healthy Essentials (oils) |
| Mustard Oil | `assets/p-mustardoil.jpg` | Healthy Essentials (oils) |
| Coconut Oil | `assets/p-coconutoil.jpg` | Healthy Essentials (oils) |

**Shelf photographs** (the picture on a category card and on that shelf's hero
slide) are probed at `assets/cat-<shelf id>.jpg`. Three of the four are stand-ins
copied from the old shelves and should be replaced with a shot that is actually
of that shelf:

| File | What it is now | Replace with |
|---|---|---|
| `cat-spices.jpg` | copy of `cat-ground.jpg` — turmeric in bowls | fine in the meantime; it is genuinely our category |
| `cat-pulses.jpg` | copy of `mission-daily.jpg` — mung, buckwheat and rice | **replace first** — it shows neither toor nor chana |
| `cat-essentials.jpg` | copy of `cat-oils.jpg` — one oil bottle | a shot with the salt and khandsari in it too |

`cat-ground.jpg`, `cat-whole.jpg`, `cat-blend.jpg`, `cat-pantry.jpg` and
`cat-oils.jpg` are all still on disk and still used — the "How it is made" flip
cards read three of them directly.

Pav Bhaji Masala was removed from the range on 3 Sep 2026, so `p-pavbhaji.jpg` is
no longer wanted.

**Easiest wins first:** the whole spices, the seeds and the salt photograph well
loose in a bowl and need no pack. The four oils are the hardest — an oil shot
really wants the bottle you will actually sell.

### Sourced photos, and why only two

Searched Openverse (the Creative Commons aggregator: Wikimedia, Flickr, Rawpixel
and others) for all 16 missing products on **3 Sep 2026**, restricted to licences
that allow commercial use. 54 candidates were reviewed by eye. Only two were both
**honest** and **good enough to sell with**:

| File | Licence | Source |
|---|---|---|
| `p-flax.jpg` | CC0 1.0 | rawpixel.com/image/5907235 |
| `p-quinoa.jpg` | CC0 1.0 | rawpixel.com/image/5941698 |

CC0 means public domain: commercial use is fine and **no attribution is required**.
Both are 684px square, cropped from the largest copy the API serves — not upscaled.

What the free pool actually returned for the rest, and why each was rejected:

- **Masala blends** (kanda lasun, meat, chaat, chatpat) — only photographs of
  *cooked dishes* (chicken curry, rajma, shahi paneer). A curry is not a masala
  powder; using one would misrepresent the product.
- **Mustard seeds** — photographs of mustard *fields* in flower, and a Chinese
  painting manual called "Mustard Seed Garden".
- **Fenugreek** — a botanical illustration, a bowl of dal, and a mackerel dish.
- **Chia** — chia *pudding* with apricots, not the raw seed.
- **Pink salt** — one bowl shot cluttered with a restaurant menu and a phone; one
  out-of-focus crystal macro.
- **Unrefined sugar** — a chana dish, twice.
- **Oils** — a 1939 "Receptacle Peanut Oil" museum record and a 1662 painting.
- **Cumin** — one plausible flat-lay, but the seeds read closer to fennel than
  cumin, so it was rejected rather than risk mislabelling a product.

**Conclusion: the free CC pool cannot dress this range.** It has no studio
photography of Indian ground masalas. The two realistic routes are:

1. **Pexels or Unsplash.** Both have genuinely good spice, seed, oil and salt
   photography, licensed for commercial use with no attribution required. Both
   need a free API key (a couple of minutes to create), or the images can simply be
   downloaded by hand from the site. This is the fast route to a good-looking page.
2. **Photograph the real products.** Daylight, a plain sheet, a phone. These shots
   are needed for the labels anyway, and they are the only ones that show what a
   customer will actually receive — which is the whole premise of the brand.

Until then the browser console logs a harmless 404 for each missing file. Visitors
never see it.

## Adding another product

The range is not fixed at any number, and not fixed to masalas. Everything on the
page that lists products — the cards, the category tabs and their counts, and the
spice-colour rule above the pillars and above the footer — is generated from the
single `PRODUCTS` array at the top of `js/satva.js`. Add an entry and all of them
update:

```js
{ acc:"var(--turmeric)", ink:"#9a6b06", en:"<English name>", hi:"<Hindi name>",
  cat:"ground",            // ground | whole | blend | seeds | pantry | oils
  form:"Ground",           // optional badge: "Ground" or "Whole". Omit otherwise.
  glyph:"<first Devanagari letter or two>",
  d:"<one line about how it is used>",
  img:"assets/p-<id>.jpg",
  tint:"linear-gradient(150deg,#<light>,#<darker>)" }
```

- **`en` is the product's name and leads the card. `hi` is the secondary line
  under it.** The site is meant to be readable globally, so English is never
  demoted below the Hindi.
- `acc` is the bright spice colour (the card's colour bar, the rule segment, the
  hover border). Reuse one of the tokens in `satva.css` or add a new one.
- `ink` is a darkened version of the same hue, used for the product name so it
  stays legible on white. Keep it at 4.5:1 or better against `#fff` — all 21
  current values were measured, the tightest being Groundnut Oil at 4.64:1.
- `cat` is the shelf. `GROUPS`, just below `PRODUCTS`, decides which tabs exist and
  which `cat` values each tab collects, so a tab can still span more than one. As of
  4 Sep 2026 none of them does: `Ground spices` and `Whole spices` were split into
  separate tabs at the owner's request — see "The spice shelves, split" below. A
  group with no products in it renders no tab.
- `tint` is only used until a real photo exists at `img`.

No copy anywhere says how many products there are, or calls the range "masalas", so
nothing goes stale when the range grows.

### Languages

Product names are English-primary with Hindi (Devanagari) underneath. The typeface
is **Tiro Devanagari Hindi**; the class hook for any Devanagari text is `.dv`.
Marathi was used until 3 Sep 2026 and was replaced throughout — if you see `.mr`,
`fc-mr` or "Tiro Devanagari Marathi" anywhere, it is a leftover and should be
renamed. The dish marquee is deliberately in Latin script for the same
global-readability reason.

## The two places only you can fill in

**A specific scene in Our Story.** The founder's 18 years now anchors the section, so
it is no longer anonymous. What it still lacks is one concrete moment: a particular
kitchen, a particular person, a particular afternoon. Everything there now is stated
at the level of the industry; a single scene would make it unanswerable. Drop it in as
a `<p>` after the first one. There is a comment marking the spot.

**Real tester quotes.** The "three questions we actually ask" section currently shows
the questions, plus one dashed card saying real answers are coming. As feedback lands
in the Responses sheet, replace the dashed card with actual quotes - `.vcard` blocks.
Keep the unflattering ones; they are the reason anyone will believe the good ones.

## Where the story's facts come from

Our Story was rewritten to the founder's brand copy: 18 years in the food supply
chain, the meaning of *satva*, the promise, the vision, the tagline. It now covers
the whole DS Satva Foods range in intent — spices, pulses, grains, seeds, Pink
Himalayan salt — not masala alone.

**The one checkable claim in it, and its exact wording.** The story cites *56.4% of
India's **total** disease burden is attributable to unhealthy diets*, sourced on the
page to ICMR-NIN's Dietary Guidelines for Indians (May 2024). The founder's draft
said "over 56% of India's **chronic** disease burden". That is a different and
smaller claim than what ICMR published, so the page uses the accurate version.
If you edit that line, keep it as total disease burden.

### Copy on this page is the owner's, or it does not ship

Our Story was previously filled with assistant-written narrative that read well and
was never verified with the owner: an invented founding realisation, and a sampling
and feedback method described as fact about the business. It has been removed at the
owner's request and is deliberately not recoverable from this repo.

The rule going forward: **no claim about how DS Satva Foods operates goes on this
page unless the owner wrote it or confirmed it.** Placeholder copy is fine while
building, but it must be visibly marked as placeholder, never written in the brand's
own voice as though it were true.

Sections still carrying unverified operational promises are listed below.

### Aligning the rest of the site with the owner's copy

The owner's copy describes DS Satva **Foods** and four families of staple, not masala
alone. Three surfaces were updated to match, all using the owner's own wording:

- **`<title>`, meta description and Open Graph tags** now say DS Satva Foods and
  "Pure Daily Kitchen Essentials", and the description lists the four families.
  These are the SEO surface — if you change them again, change them deliberately.
- **The Range section** is now "Our daily kitchen essentials". Above the masala grid
  sits a four-card strip naming the families the owner listed: stone-ground spices,
  unpolished pulses, nutrient-dense seeds, Pink Himalayan salt. The descriptions are
  the owner's phrasing, lightly tightened.
- **The masala grid is unchanged and now sits under its own sub-heading**, "Masalas,
  listed individually", so the four families are not mistaken for the whole catalogue.
  The first tab was renamed from "Everything" to "All masalas" for the same reason.
  (Stale as written: the tab in `GROUPS` reads "Everything" and always has. The
  rename was described here but never made. Left alone rather than changed blind —
  the label is the owner's call.)

**No pulse, seed or salt products were invented.** The owner's copy names the families
but no product names, pack sizes or prices, so nothing was added to `PRODUCTS`. A
`TO ADD` comment marks the spot in `index.html`. Until then the range section ends
with a line inviting a WhatsApp enquiry about what is packed right now, which is
honest at any stage of stock.

The `--himalayan` token (`#d98a8a`) was added for the salt family; every other family
reuses an existing palette token.

### The paradox section

The section at `#paradox` is the owner's argument, and it replaced the earlier
"three questions we actually ask" — which described a feedback process that had never
been confirmed. The comparison does the work: two purchases we study carefully and can
reverse, against the one we buy out of habit and cannot take back.

Three cards, and the third is deliberately the odd one out — dark green where its
neighbours are white (`.vcard.odd`), because it is the purchase nobody studies. The
labels carry the frequency, which is where the argument actually lands: *bought once
in three years* against *eaten every single day*.

**Renames that came with it.** The section id went from `#feedback` to `#paradox`, so
the nav and footer links were retargeted and relabelled "Paradox". The hero's slide-3
button, which used to point at `#feedback`, now goes straight to the feedback form
instead — the form is still reachable there and from the Contact card, so that path
was not lost. No dead in-page anchors remain (verified).

### Still unverified with the owner

Two sections still make operational promises in the brand's voice and predate the
owner's copy. They should be confirmed or rewritten before the site goes public.

1. **Freshness** — that every pouch carries its actual grind date, and that a customer
   can send a batch code on WhatsApp and be told what went into that grind. The
   example label shows batch `KL-2609-03`, ground 12 September 2026. A freshness
   promise is the first thing a customer tests, and the paradox section now points
   directly at it ("What is on our pouch"), so it carries more weight than before.
2. **Why SATVA, card 04** — "Every masala goes to home kitchens for a verdict before
   it goes on sale."

## Still to fill in

- **FSSAI licence number** — there is a marked comment in the footer of `index.html`.
- **Pack sizes and prices** — deliberately not on the page; every product says
  "Ask price on WhatsApp" instead.
- **Instagram / Google Business links** — not added yet.

## The "why choose" block

Modelled on the three-column block on rumispice.com: big line illustration, heading,
short paragraph, one CTA underneath. Adapted rather than copied — Rumi runs everything
in a single orange, which reads flat and drops body-text contrast. This uses the site's
existing spice-colour idea instead: one accent per column for the illustration only
(sage, turmeric, garam brown), with headings in `--ink` and body in `--sage`.

**It replaced the old `.pillars` strip**, which made the same argument with four 33px
icons. The page already carried several "why we are good" blocks, so this is that idea
given room rather than a fifth one. The four label words (Natural, Pure, Homemade,
Authentic) are not lost — hero slide 3 still names them.

**The illustrations are hand-written inline SVG** on a `0 0 200 200` viewBox at
stroke-width 3.1, `currentColor`, so they recolour from `--rc` and stay sharp at any
size. No image files, no library, a few hundred bytes each. Two things learned drawing
them: the mortar needed to be narrower and deeper than a first pass made it, or it
reads as a soup bowl; and the heap of pulses must be *narrower* than the bowl rim, or
the two arcs close into a circle and the whole thing reads as a ball.

All three claims are the owner's promise wording. The fourth ("uncompromising
standards") stays in the Our Story list — four columns at this size would have cost
the illustrations the room that makes the block work.

Verified: no horizontal overflow at 375 or 1085px; three columns collapse to one at
820px; illustrations scale 158-212px.

## The shelf slider

`#shelves`, between the marquee and the category cards. Five editorial openings,
one per shelf, in the owner's order: whole spices, seeds, oils, ground spices,
pantry. Added 6 Sep 2026 from jainfarmfresh.com/products/spices, which the owner
sent asking for "this kind of picture and incorporation".

**What is taken from that page**, and nothing else: a flat pale ground rather
than a photograph behind the words; a two-line serif headline in the brand green
with the second line carrying the gold; one paragraph at reading width; and an
outlined pill whose arrow sits in a filled circle at its right end. The wording
is this site's own — every claim on the five slides already appears in "Why
choose SATVA", the families list, or the product line it describes.

**Blends are the sixth shelf and deliberately absent.** The owner asked for five.
Adding the slide is markup only: copy an `<article class="shelf">`, set
`data-shelf="blend"`, `data-label`, and a `--sg` ground. The tab strip, the count
line and the CTA wiring all come off the slides themselves.

**It does not autoplay,** unlike the hero. Two carousels advancing on their own
on one page compete for the same attention, and this one is browsed rather than
watched: the named tab strip is the real navigation, with arrows, swipe and
left/right on the tabs for anyone flicking through. Arrows disappear under 620px,
where the hero already drops its own in favour of swipe.

**Counts come off `PRODUCTS` and `GROUPS`** in `js/satva.js`, the same pair the
tabs and the category cards use, so "3 items packed" cannot drift from what the
range below will actually list. Each pill drives the existing range tab instead
of filtering separately — the same thing a category card does, so a visitor
arriving from either lands on the same listed shelf.

### The photographs

Re-picked 6 Sep 2026: the owner asked for "stunning vibrant coloured pictures in
the hero section". Two of the five now use the panoramas from the deleted brand
hero, which were the best and most colourful assets in the project and were left
unused when that block went:

| Slide | File | Why |
|---|---|---|
| Whole Spices | `hero-3.jpg` | Green cardamom, cinnamon bark, star anise, pepper — whole spices, and the most colour of any shot we own |
| Seeds | `cat-seeds.jpg` | Seed and pulse bowls on warm beige; the only truthful seed photo |
| Oils | `cat-oils.jpg` | The only oil photo |
| Ground Spices | `hero-2.jpg` | Turmeric, chilli and coriander heaped in bowls — literally the three ground products |
| Pantry | `cat-pantry.jpg` | Pink salt, coarse and fine, on marble |

`hero-1.jpg` is a near-duplicate of `hero-3.jpg` from the same shoot and is left
unused. Dedicated wide shots still belong at `assets/shelf-<id>.jpg` — swap the
`src` and the `alt` when they exist.

**Three per-slide knobs**, all set inline on the `<article>`:

- `--shot-pos` picks which part of the photograph survives the crop. The
  panoramas are 1700px wide and only ~800px is ever seen, so this matters: whole
  spices sits at `16%` specifically to clear a thin border stripe baked into the
  left edge of `hero-3.jpg`, which otherwise showed as a vertical line.
- `--shot-pos-m` is an optional second crop for the narrow-screen band, which is
  wide and short where the desktop panel is narrow and tall. Only the oil bottle
  needs one — centring it in a tall panel cuts its neck off in a band.
- `--vib` lifts a flat photo. **Kept between 1.00 and 1.20 on purpose.** This is
  a brand whose argument is that colour comes from the spice and not from a dye
  drum, so the already-vivid shots are barely touched (ground spices sits at
  1.03) and only the soft ones are pushed — the oil bottle at 1.20, the seed
  bowls at 1.16. Do not raise these to make a photo pop; replace the photo.

### How long the picture is, and where it fades

Lengthened again 6 Sep 2026 — "a little more longer, and then taper it down near
the writings". Above 1024px the photograph is an inset frame bleeding off the
right edge, `min(58%,900px)` wide, which starts at x=605 on a 1440 viewport. It
fades leftward on a five-stop ramp and is at full strength by 58% of its own
width. Before this it was `min(44%,620px)` reaching full strength at 78%, which
left only ~140px of picture at its real colour and read short and washed; it is
now ~350px.

Five stops, not two: a straight ramp bands visibly over this distance.

**The 58% is measured, not chosen.** It is set so the taper finishes dying in the
empty gap between the copy and the subject. Measured across all five slides, the
longest line of type on each sits where the mask is **at most 4.4%** — i.e. the
photograph is invisible behind every word. Raise the 58% and the fade crowds the
type; lower it and the taper turns back into an edge.

If the copy column or the panel width is ever changed, **re-measure this.** The
first attempt at lengthening widened the panel to 64% at the 1080 breakpoint and
put the photograph at 18–43% opacity directly behind the body text between 900
and 1080px, which is legible-ish on the pale slides and not on the vivid ones.
That is why two things changed with it:

- the two-column layout now stacks from **1024px** down, not 900px — the
  viewport below that is simply too narrow for a 58% copy column and a long
  photograph to share;
- the remaining two-column band, 1024–1080px, gets a deliberately smaller panel
  (`min(46%,540px)`) so the taper still finishes before the type does.

Worst case across 1440 / 1200 / 1080 / 1030 is now under 5% everywhere.

Every photo in the hero is shot on a pale ground (stone under the panoramas,
beige under the seed bowls, marble under the salt), which is what lets it
dissolve into the cream at all rather than sitting on it as a rectangle. A photo
shot on a dark ground would need its own handling — the old `.sh-shot.deep`
escape hatch for that was **removed** on 6 Sep 2026, because once the default
taper reached 58% the `.deep` rule at 56% had become the same rule under a name
that claimed otherwise, which is worse than no escape hatch at all.

Below 1024px the two stack: photograph on top, copy under it on the ground. The
band is `clamp(250px,54vw,380px)` and its **bottom** tapers into the cream — the
stacked layout's version of the same instruction. Where the desktop panel dies
out horizontally as it nears the column of type, this one dies out vertically as
it nears the type below it; without it the photograph stops at a ruled
horizontal line directly above the kicker, which is the one edge the desktop
layout no longer has.

Stacking replaced a full-bleed photo behind a near-opaque cream scrim, which was
legible but spent the picture to get there — a wash at .965 over the turmeric
and chilli left almost none of the colour that is the whole reason these shots
are here.

## Shop by category, and the footer

Both modelled on vahdam.com.

### Shop by category

`#categories`, above the range. Five arch-topped cards — the arch is the one shape
borrowed wholesale, because it is what makes Vahdam's block read as a shelf rather
than a table.

**The cards are generated in `js/satva.js` from `GROUPS` and `PRODUCTS`**, so labels
and counts cannot drift from the grid below. Clicking a card drives the existing range
tab rather than filtering separately — one filtering mechanism, not two. Add a product
or a group and this block follows.

Art lives in `CAT_ART`, keyed by group id, so `GROUPS` itself stays untouched. A group
with no `CAT_ART` entry, or no products, renders no card.

Vahdam uses a photograph per category. This uses a tinted field and a line icon
instead — there are only a handful of product photos in `assets/`, and mixing photos
with placeholder tiles across five cards would look unfinished. Drop photos in later
if you want them.

### The footer

Four columns: brand, The range, Explore, Reach us.

**Where Vahdam puts a newsletter signup, this puts WhatsApp** — that is the channel
this business actually runs on, and there is no mailing list to sign up to.

**No social icons.** Vahdam has a row of six. There are no DS Satva accounts to link
to yet, and icons that go nowhere are worse than none. There is a marked `TO FILL` for
Instagram and Google Business.

The footer's large bottom padding is not decoration: `.wafab` is fixed at the
bottom-right and sat directly on top of "Made in Chhatrapati Sambhajinagar" until the
clearance was added.

### Two bugs worth remembering

**Class-name collision.** The category grid was first called `.cgrid`, which the
contact section already used. The contact rule came later in the file, so it silently
won and the categories rendered four-across instead of five. Nothing errored. When
adding a block, grep the stylesheet for the class name first.

**The dev server now sends `no-store`.** Edits to `css/satva.css` and `js/satva.js`
were being served from the browser cache, so a finished change looked broken and
several minutes went into debugging correct code. Start the site with
`python3 <scratchpad>/serve.py` rather than `python3 -m http.server 8000`; it is the
same server with `Cache-Control: no-store` added. A browser that already cached the
old files may still need one hard refresh to let go of them.

## Everyday essentials

Modelled on the "Flavorful Essentials" block on jacobsensalt.com. Sits between Shop
by category and the full range, so the page reads broad → curated → complete: pick a
category, start with these, or scroll the whole catalogue. **Nothing was removed to
make room for it.**

What was taken from the reference: the heading and the tabs sitting on **one
baseline**, and a horizontally scrollable row whose last card runs off the edge to
invite the swipe. What was not: their diamond arrows and FAV badges are their motif,
so the arrows here reuse this site's own round hero-arrow shape.

### The three tabs, and why these labels

Generated from `ESSENTIALS` in `js/satva.js`. A tab resolves either by `names` (a
hand-picked order) or by `cats` (everything in those categories):

| Tab | Source | Basis for the label |
|---|---|---|
| Kitchen staples | 6 hand-picked names | a recommendation, in our own voice — not a popularity claim |
| Whole spices | `cat:"whole"` | factual, straight off the data |
| Cold-pressed oils | `cat:"oils"` | factual — every oil's own description says cold-pressed |

The reference's third tab is "Best Sellers". **That was deliberately not copied**:
there is no sales data, and a bestseller badge is exactly the kind of unverifiable
claim this site avoids. "Kitchen staples" is a recommendation we can stand behind.

A name not present in `PRODUCTS` is skipped, so a tab can never show a phantom
product, and a tab that resolves to nothing renders no tab at all.

### Not copied: pack-size pills

Jacobsen's cards carry pack-size pills (4 OZ / 16 OZ / 5 POUND CHEF BAG) that switch
the price. That needs real pack sizes, which are deliberately not on this site. **When
the owner supplies them, this row is where they belong first** — tapping a size should
pre-fill the WhatsApp message with it. Marked in `index.html`.

### One refactor and one bug

**`buildCard(p, cls)`** was extracted so the essentials row and the full grid share a
single card implementation. Before this the markup existed once; adding a second
consumer would have duplicated it, and the two copies would have drifted.

**`display:flex` beats `[hidden]`.** All three tab panels rendered at once, stacked, at
double the intended height — an author `display:flex` overrides the `hidden`
attribute's UA `display:none`. Fixed with `.etrack[hidden]{display:none}`. Worth
remembering for any future tabbed flex or grid container.

Arrows hide themselves when a track fits without scrolling (Whole spices, 3 cards),
and are dropped entirely below 720px where the row is swiped.

Verified: no horizontal overflow at 375 or 1100px; tab switching leaves exactly one
track visible and resets its scroll; the full range grid still renders all 21 products
and the category and reasons blocks are untouched.

## The header

Upgraded after curiospice.com. Two changes, both chosen because the site had grown
into needing them.

### The "Our Range" dropdown

With 21 products in 5 categories, a single `#range` anchor was thin navigation. The
nav item is now a nested list: **Everything (21)**, then each category with its count.

Built from `GROUPS` and `PRODUCTS` in `js/satva.js`, so it lists exactly what the grid
can show. Each item drives the existing range tabs — the same mechanism the category
cards and the essentials row use, so there is still one filtering path for the whole
site.

It opens on hover **and on `:focus-within`**, so keyboard users get it without any JS,
and the parent anchor still jumps to `#range` on its own if scripting fails. Escape
closes it. On a touch screen there is no hover, so inside the burger menu the submenu
is simply always open and indented.

### The rotating announcement line

The top line now cycles four messages instead of showing one static string, like their
announcement bar. **Every line is copy that already appears elsewhere on the site** —
nothing new is claimed. The fourth is written by JS from `PRODUCTS.length`
("21 daily kitchen staples, and counting") so it cannot go stale as the range grows.

Messages stack in a single CSS grid cell, so the bar never changes height as they
swap. Rotation stops for `prefers-reduced-motion`, on hover, and when the tab is
hidden.

### Not taken from the reference

- **Their header is black.** This site is warm cream and green throughout; inverting
  the header would be a brand decision, not a header upgrade.
- **Their nav is centred, with search / account / cart icons.** There is no cart or
  account here, and this logo is a wide horizontal lockup — centring the nav between
  it and the WhatsApp button would squeeze both. Search over 21 products is arguably
  worth having, but the category dropdown covers the same need for now.
- **Language and currency selectors.** One market, one currency.

### Three bugs found doing it

**`.nav ul` captured the nested list.** `.nav ul{display:flex}` (specificity 0,1,1)
outranked `.submenu` (0,1,0), so the dropdown inherited `display:flex` and
`margin-left:auto` and rendered as a 614px horizontal strip. Every submenu rule is now
scoped `.nav .submenu`. The same trap hit `.nav ul a` over `.submenu a`.

**Two rules for `.topline .left`.** A grid rule was added while a `display:flex` rule
for the same selector still sat 10 lines below it and won. The messages laid out in a
row and the fourth wrapped to a second line, showing as a ghost under the first and
pushing the bar from 39px to 55px. The fix was deleting the superseded rule, not adding
specificity.

**The hover bridge overflowed the page.** The invisible strip that lets the pointer
cross the gap between the nav item and the menu was `width:150%` and centred — 508px
on a 339px item. Harmless on desktop inside `overflow-x:hidden`, but once the nav
stacked on mobile it pushed the document 67px wide. It now spans the item (`left:0;
right:0`) and is disabled entirely in the open mobile menu.

Two pre-existing mobile defects surfaced and were fixed at the same time: the WhatsApp
button was anchored to the same edge as the open menu panel and sat on its first row
(the panel now reserves a strip for it), and `.nav.open ul a{display:block}` outranked
the submenu's `display:flex` so the item counts sat flush against their labels.

Verified: no horizontal overflow at 375, 985 or 1265px, menu open or closed; the
901-1200px single-line nav fix still holds with 40px of slack; dropdown click-through
filters the grid and closes the menu.

## The nav between 900 and 1200px

The full nav needs about 1190px: logo, six links, and the 208px WhatsApp button.
The burger only took over at 900px, so every window from roughly 900 to 1200px
rendered the header on **two lines** — links breaking mid-word, the bar growing past
its 80px, and section headings sliding up underneath it. Common laptop widths sit
right in that gap.

Two changes fix it, both in `css/satva.css`:

- `.nav ul a` gets `white-space:nowrap`, so a link can never break mid-word.
- A new `@media (max-width:1200px) and (min-width:901px)` block hides `.navcta` and
  tightens the link gap and letter-spacing. The button is redundant at those widths —
  the top line already carries the number, and `.wafab` appears once the hero scrolls
  away.

Measured after the fix: at 905px (tightest, just above the burger breakpoint) all six
links sit on one line with 37px of slack and no overlap; at 1205px the button is back
with 32px of clearance. No horizontal overflow at 375, 905, 1085, 1205, 1265 or 1425.

Worth knowing when you edit the nav: `body` has `overflow-x:hidden`, so anything too
wide is silently **clipped** rather than given a scrollbar. A nav that does not fit
will not announce itself — it just loses its right-hand end.

## The powder over the hero

`js/grind.js` + `css/grind.css` suspend ground spice in the air over the hero — a
few hundred to ~2600 grains on a 2D canvas, hand-written, no library and no build
step, about 8 KB. It is the one deliberately "designed" moment on the site, and it
is on-brand rather than decorative: the powder is the colour of the masala on the
current slide, and every slide change drops a fresh fall from above, which is what
*ground in small batches* looks like.

**It is removable in two lines.** Delete the `grind.css` link and the `grind.js`
script tag in `index.html` and the hero is exactly as it was. Nothing in
`satva.css` or `satva.js` was modified to add it.

### Per-slide colour

Data-driven, like `PRODUCTS`. Each `.slide` carries a `data-powder` of two or more
hexes, and the palette follows whichever slide is active:

| Slide | `data-powder` | Reading as |
|---|---|---|
| Absolute purity | `#e8a713,#bf8a17,#93a04b` | turmeric, gold, coriander |
| Small batch | `#c3341a,#a8462a,#e2912b` | chilli, kanda lasun, biryani |
| Every masala | `#93a04b,#7d5630,#55714e` | coriander, garam, sage |

Add a slide with three hexes and it just works. A slide with no `data-powder`, or
with malformed hexes, falls back to turmeric/chilli/coriander.

### Tuning

Every dial is a named constant in the block at the top of `grind.js`.

- `GRAIN_ALPHA` — **the honest dial for "show me more powder."** Raise it to make
  the effect more obvious without costing a thing.
- `GRAIN_AREA` — the performance dial: one grain per this many px² of hero, clamped
  to `GRAIN_MIN..GRAIN_MAX`. Raise it for fewer grains.
- `PUSH_R` / `PUSH_F` — the cursor pushes powder aside within this radius, like
  brushing it off a surface. Touch devices simply do not get this; the powder still
  drifts.

Grain sizes come off a power curve (`Math.pow(random(), 2.7)`), so most grains are
dust and only a few are coarse specks. A flat `random()` was tried first and read
as confetti, not spice.

### Two things it is careful about

**Legibility.** The headline's real bounding box is measured from the live layout,
and grains fade to 8% as they cross it. There is deliberately no hard-coded "keep
right of 40%" rule — the first version had one, and on a phone, where the copy is
full-width, it put powder straight through the headline. The box is re-measured on
resize and after each slide transition, so it stays correct at any width and with
any length of headline.

**Not running when it does not need to.** It stops when the hero scrolls out of
view (`IntersectionObserver`), stops when the tab is hidden, caps DPR at 1.5, and
scales grain count to the hero's area so a phone does less work than a desktop.
`prefers-reduced-motion: reduce` is honoured twice over — `grind.js` returns before
allocating anything, and `grind.css` hides the canvas.

### Where to take it next

The same particle system is the basis for two more moments, in rough order of
payoff: a product card that pours a little of its own powder on hover, and the
`.spectrum` rule becoming something you can drag a finger through. Both reuse
`makeSprite`, `seed` and `step` as they stand.


## Regenerating the image assets

Every file in `assets/` was cut from `~/Downloads/DS_STICKER.pdf`: the logo is keyed out
of a 600 dpi vector render, the photos are crops of the embedded spice photograph, and
`leaf-mask.png` is the label's leaf watermark turned into a CSS mask (the mask must keep
its **alpha** channel — a plain greyscale PNG renders as a solid block).

## The 4 September 2026 reference walkthrough

The owner sat through roughly twenty-five food and spice sites on a call that
morning and said what he wanted taken from each. The source is a Plaud recording,
*"09-04 Meeting: DSatwa Spice E-commerce Website Design Decisions and Next Steps"*
(47 min, three speakers). It is heavily code-switched between English, Hindi and
Marathi and the transcription garbles several stretches — notably 840–960s and
1599–1708s. Where a decision below is quoted, the quote is from a clean stretch.

Four sections were built from it, plus two hero slides and a shelf split. **The
reference sites were opened and read before building** — every "what was taken /
what was not" note below is from the live page, not from memory.

### What the owner rejected, and is still rejected

Worth writing down, because these come up every time someone adds a block:

- **Bright palettes and dark palettes both.** "So much of brightness"; "these are all
  something like dark, I don't think it will relate with our this". Everything added
  here is warm and light. The one dark band is Satwa Saheli, and it uses `--band`,
  which the footer and marquee already use.
- **Discount banners.** Rumi Spice runs a "20% off + fast free shipping" welcome
  offer; the owner picked that out as the thing to remove.
- **Non-vegetarian imagery.** Three reference sites were dismissed on sight for beef,
  chicken and sausage photography. (Meat Masala stays in `PRODUCTS` — it is a product
  the business sells. This is about photography.)
- **Video, for now.** "We'll not have a video as of now." Every media slot added is
  photo-first.
- **Clutter.** On one reference hero: "so much of information… that will look very
  good, so now this looking clumsy." One subject per hero, one line of headline.

### The spice shelves, split

The owner walked through a competitor's product nav and asked for the same shelving:
"so it's whole spices, blend and seeds and all, in that way we can have." `Spices`
in `GROUPS` collected both `ground` and `whole`; it is now **`Ground spices` (3)** and
**`Whole spices` (3)** as separate tabs and separate category cards.

Everything downstream followed on its own, which is the point of generating all of it
from one array: 7 tabs, 6 category cards, the nav dropdown, and the counts. `CAT_ART`
gained a `whole` entry (two whole-pod outlines) and `spice` became `ground`.

`.catgrid` went from `repeat(5,1fr)` to `repeat(6,1fr)` and its max-width from 1080 to
1180px, and the 3-column breakpoint moved from 940 to 1080px so six cards never sit at
174px each.

### Origin — `#origin`, after onyxcoffeelab.com

Onyx runs three place cards — PERU / ECUADOR / COLOMBIA — each a looping background
video behind a place name, one paragraph of terroir and a "View Coffees →" link. The
owner pointed straight at it: "if you can get the videos from where you actually
source the spices, from there we can put it here."

What was taken: the three-card shape, the place name leading, one paragraph, one link.

What was not:

- **The video.** Each card renders a tinted ground with line art and probes for
  `assets/origin-<id>.jpg`. Drop a file in and that card switches over — same
  probe-then-swap as the product cards, no code edit.
- **Three named regions.** *This is the important one.* **Two of the three cards are
  deliberately unfinished.** The owner has not said where this range is sourced from,
  and a sourcing story is exactly the kind of claim this page does not invent. They
  carry a `TO CONFIRM` pill and say plainly that nothing is written until the growers'
  own account arrives. Only card one states a fact — Chhatrapati Sambhajinagar, where
  the spice is ground — and that was already on the page.

Cards come from `ORIGINS` in `js/satva.js`. Remove `todo:true`, write the paragraph,
drop the photo.

### Recipes — `#recipes`, after dandelionchocolate.com

Their recipe row puts the cook time on the card: *Just Chocolate Cake · 2½ Hours*.
Speaker 1 read it out loud in the meeting, which is how it got in. **That badge is the
one thing taken** — it is what turns a photograph into something a cook can decide
about.

What was not taken: their `MORE RECIPES` link. There is no recipe library to link to,
so each card names the SATVA product it uses instead and picks up that product's
accent colour from `PRODUCTS`. The CTA is a WhatsApp enquiry.

Three recipes, from `RECIPES` in `js/satva.js`: Kanda Lasun Zunka (25 min), Everyday
Varan Bhaat (40 min), Sunday Biryani (1 hr 30). These are ordinary household recipes
in our own voice — they are **not** claims about the business, which is why they could
be written without the owner. Times are deliberately honest rather than flattering.

`uses` must match an `en` name in `PRODUCTS` or the accent falls back to gold.

### Satwa Saheli — `#saheli`, after rumispice.com

Rumi runs "Empowers Afghan Women" as one of three why-choose columns. The owner wanted
it as a section of its own, under a name he supplied himself: "I want to have this
one… it's like Satwa Saheli."

**The owner has confirmed the programme is real. He has not yet supplied the figures,
the location, or the women's own words.** Every such slot is marked `todo` and renders
visibly unfinished. Search `index.html` for **`TO FILL: SAHELI`** to find all of them:

| Slot | What it needs |
|---|---|
| One further `<p>` | Who these women are, what work they do, what changed for them. One specific person beats any number. |
| `Women working with us` | A count, once it is a real one. |
| `Village or ward` | Where they are. |
| `assets/saheli-1.jpg` | A portrait, 3:4, 680px wide or larger. |
| `assets/saheli-2.jpg` | The same, at work. |

**Photograph the actual women, with their consent, and name them.** A stock photograph
of an anonymous woman in a field would undo the entire point of the section, and this
is the one block on the site where that temptation is strongest.

Only one figure is stated: *100% of this work stays local*, which is a structural fact
about a business that packs in one town, not a claim about the programme.

### Our Mission — `#mission`, and the colour shift

The owner noticed a site whose ground changes colour only for its mission section:
"when we come here to our mission, the site color is changing. It's like that only for
our mission." **He never named the domain**, and the recording gives no way to
recover it, so only the idea was borrowed — the implementation is ours.

`js/satva.js` drives `--mx` from 0 to 1 as the section's centre approaches the centre
of the viewport, and the CSS mixes cream toward gold across that range with
`color-mix(in oklab, …)`. A `@supports not` block cross-fades a second layer instead
for engines without `color-mix`. Nothing else on the page reads `--mx`, so the effect
cannot leak into a neighbouring section. `prefers-reduced-motion` gets the flat ground.

**The words are the owner's own vision statement, moved not written.** It had been
sitting as a `blockquote` two thirds of the way down Our Story where nobody reached it.
It now has the section the owner asked for, and Our Story carries a comment saying
where it went. No new copy.

### Hero slides 4 and 5

"Do you like? We have only four to five sliders. What is that? Four to five pics
sliders. That's all." There were three; there are now five. `.dots` and the progress
bar are generated from the slide count, so nothing else needed touching.

Both new headlines are **one line** — the owner praised the openings on
onyxcoffeelab.com and stumptowncoffee.com specifically for being simple ("the way it's
simple, and the way they are showing production") — so neither uses the stacked `<em>`
of the first three.

**The soft CTA.** The owner liked that Rumi says *Upgrade my Spice Rack* rather than
Buy: "it's not like they are not saying you to buy." Slide 4's is **Fill my spice
rack** — same idea, our wording. Slide 5 is the other thing he liked, a reference
site's "cook a meal for someone you love", turned into our own line: *You are not
cooking for yourself.*

**Their photos are borrowed product crops.** Slides 4 and 5 use `p-staranise.jpg` and
`p-chilli-whole.jpg` as their band because dedicated wide hero shots do not exist.
`assets/hero-4.jpg` and `assets/hero-5.jpg` are where the real ones belong — swap the
`src` and the `alt` together.

### Why the new sections are in the footer and not the nav

All four are linked from the footer's Explore column, which went from 5 items to 9.
**None was added to the top nav**, because the nav's width budget is measured and
already full: six links plus the 208px WhatsApp button need about 1190px, and a
seventh link would have reintroduced the two-line header this repo already fixed once
(see "The nav between 900 and 1200px"). Measured after this change: at 1205px the nav
is still one line, still 80px, still with 32px of clearance before the button — the
same figures as before.

Every new section also has an in-page entry point: hero slide 4 links to `#origin`,
slide 5 to `#recipes` and `#saheli`, and the origin note links to `#freshness`.

### Deferred, and agreed

**Gifting.** "Shopping gifts, maybe we can try handmade gifts and something like
that." Not built. It needs pack sizes and prices, which are deliberately not on this
site yet, and "maybe we can try" is not a decision. When it is built, the essentials
row's pack-size pills are the other half of the same problem — do both at once.

### The browser cache, again

Two CSS edits looked like they had failed. The file on disk was correct and the
computed style in the browser was the previous version — `serve.py` sends `no-store`,
but a page already open holds what it has. Reloading was not enough; the fix while
iterating is to rewrite the stylesheet href with a query string:

```js
document.querySelectorAll('link[rel="stylesheet"]').forEach(l =>
  l.href = l.href.split('?')[0] + '?v=' + Date.now());
```

This is the second time this has cost real time. If it happens a third, put a build
stamp on the `<link>` and `<script>` tags.

### Verified

- No horizontal overflow at **375, 905, 1205 or 1265px**, measured by element edge
  rather than `scrollWidth` — `body` has `overflow-x:hidden`, so a too-wide element
  is silently clipped and `scrollWidth` always equals `clientWidth`. The only element
  past the edge is the hero's decorative `.leaf`, which predates this work.
- All three grids collapse to one column at 375px; `.catgrid` to two.
- 5 slides, 5 dots. 7 tabs, counts 3/3/6/3/2/4 summing to the full 21. 6 category
  cards. 3 origin cards, 2 marked unfinished. 3 recipe cards.
- `--mx` measured at 0.256 scrolled away and 1.000 centred, with the background
  genuinely interpolating (`oklab(…)` in the computed value).
- No dead in-page anchors.
- 20 console errors, all of them 404s from the probe-then-swap pattern: the 14 known
  missing product photos plus 6 new slots (3 origin, 3 recipe). No script errors.

### New asset slots

None of these exist yet. Every one degrades to a designed tile, so the page is
complete without them.

| File | What | Size |
|---|---|---|
| `assets/origin-grind.jpg` | Chhatrapati Sambhajinagar / the grinding floor | landscape, 1200px+ |
| `assets/origin-region-1.jpg` | first sourcing region, once named | landscape, 1200px+ |
| `assets/origin-region-2.jpg` | second sourcing region, once named | landscape, 1200px+ |
| `assets/recipe-kanda-lasun-masala.jpg` | zunka and bhakri | 16:10, 900px+ |
| `assets/recipe-turmeric.jpg` | varan bhaat | 16:10, 900px+ |
| `assets/recipe-biryani-masala.jpg` | biryani | 16:10, 900px+ |
| `assets/saheli-1.jpg` | portrait, with consent | 3:4, 680px+ |
| `assets/saheli-2.jpg` | at work, with consent | 3:4, 680px+ |
| `assets/hero-4.jpg` | wide hero, whole spices | landscape, 1600px+ |
| `assets/hero-5.jpg` | wide hero, chilli | landscape, 1600px+ |

The recipe filename is derived from `uses` — lowercased, non-letters to hyphens. Change
a recipe's product and its photo path changes with it.

## The alternating grounds, after sweetgreen.com

The owner picked sweetgreen out of the 4 September walkthrough for its colour
combination, and asked for cream and sage green alternating "wherever needed".

**What was actually wrong before this.** Measured across all 16 sections, the page was
one continuous warm-cream wash — `#faf7f2`, `#fdfcf8`, `#f5eee0`, `#fbf6ea`,
`#fdefe7` — with three dark green bands as the only punctuation. Nothing alternated.
Sections ran into each other and white cards on cream had almost no separation.

**Sampled from the live sweetgreen page, not from memory:**

| Theirs | Hex |
|---|---|
| cream ground | `#f4f3e7` |
| sage ground | `#d8e5d6` |
| warm sand | `#e8dcc6` |
| ink | `#00473c` |

The thing worth stealing is not either colour on its own — it is that **their cream is
not warm.** It carries the same green-yellow cast as the sage, so the two read as one
family rather than two unrelated decisions. That is what makes the alternation calm
instead of stripey.

**Adapted, not copied.** `--cream` is measured off the brand sticker and is untouched.
Three tokens were added:

| Token | Hex | Why this value |
|---|---|---|
| `--cream-sg` | `#f7f6ed` | a barely greener cream that sits next to `--cream` without clashing |
| `--sage-mist` | `#e6ede0` | lightened from the brand's own `--sage` (`#55714e`), not from sweetgreen's cooler green, so gold still belongs on it |
| `--sage-mist-2` | `#dce6d2` | the deeper end, for gradient stops |

`--sage-mist` is deliberately no darker than it is: **4.54:1 against `--sage` body
text**, which is what let existing copy stay as it was instead of being restyled.

### The order

Read down the page. No two adjacent sections share a family, and the three dark bands
stay as punctuation:

```
hero        cream (per-slide tints, untouched)
reasons     ivory
  marquee     ── DARK ──
categories  SAGE
essentials  cream
range       SAGE  (white product cards finally separate from their ground)
recipes     cream
origin      SAGE
freshness   ivory
mission     cream ──► SAGE   ← the hinge
why         SAGE
promise     cream
story       SAGE
  saheli      ── DARK ──
paradox     cream
contact     SAGE
  footer      ── DARK ──
```

**The mission section is now the hinge, and this is the best thing about the change.**
At rest it is the cream of Freshness above it; fully shifted it is the sage of Why
SATVA below it. So the scroll effect the owner asked for is no longer decoration — it
is the transition between the cream half of the page and the sage half, and it does
the job a hard section border used to. Retargeting it from gold to sage is also what
the owner wanted; gold was the wrong end all along.

`prefers-reduced-motion` gets the sage end as a flat gradient, so the block still
reads as its own rather than collapsing into its neighbours.

### Contrast, because moving grounds breaks text

An audit of every text node against its real computed ground (walking up for the first
opaque background, and reading gradient stops and `::after` scrims) found **22
failures** after the repalette. All are now fixed; the audit reports **zero**.

Worth knowing what they were:

- **`--sage-soft` was already failing before any of this.** At `#6f8168` it was 4.19:1
  on plain white — used on product names' Devanagari, pack-form pills, card body copy
  across the whole site. Darkened to `#64775d`, **4.84:1 on white**. This fixed nine
  reported failures at once and is a straight improvement independent of the palette.
- **`--sage-soft` must never sit on a sage ground** — it is 4.04:1 there even
  darkened. Four rules that moved onto sage (`.catcard .cblurb`, `.wcard p`,
  `.story .sign`, `.families p`) switched to `--sage` (4.54:1). If you move a section
  to sage, grep it for `--sage-soft` first.
- **The 01–04 numerals in Why SATVA** were 1.97:1 on cream and worse on sage. They are
  decorative but they carry the card order, so they are now
  `color-mix(in srgb, var(--wc) 55%, var(--band))` — each keeps its own hue and
  darkens. 55% is the measured floor: turmeric, the lightest accent, lands at 3.21:1.
- **`.btn-ghost` on the Saheli band was 1.26:1.** The shared ghost button assumes a
  light ground — `--green` text on translucent white — which over `--band` resolves to
  dark green on muddy green. Inverted for that one section: 5.24:1.

Four reported failures were **false positives** and no code changed for them: the
origin cards' white copy sits over an `::after` scrim at `rgba(30,44,22,.82)`, and an
audit that only accepts fully opaque backgrounds reads straight past it to the section
ground. If you re-run this, accept alpha ≥ 0.5 as an effective ground.

**Verified:** zero contrast failures, zero horizontal overflow, all six category cards
and 21 products intact.

## The cream, after oddbox.co.uk

The owner asked for Oddbox's cream on our page. Read off their live site 5 Sep 2026 —
it is **`#fcedde`**, their `--color-bg-secondary-minimal`, and it is worth knowing how
they use it: it is a **section** ground, not a body colour. Their page alternates
`#fcedde` with plain white and `#f6f6f6`, punctuated by dark brown `#2d1c0e` and olive
`#425412`, with orange `#f2673d` as the hero. The body itself is transparent.

**What changed:**

| Token | Was | Now |
|---|---|---|
| `--cream` (body, hero) | `#faf7f2` | `#fcedde` |
| `--cream-sg` (the alternating cream band) | `#f7f6ed` | `#fcedde` |
| `--ivory` (the pale band between them) | `#fdfcf8` | `#fef7f0` |
| `--tint-cream` (voices gradient) | `#fbf6ea` | `#fdf3e6` |

`--ivory` had to move too. It was a near-neutral white that worked beside a near-neutral
cream; left alone next to `#fcedde` it reads cold and slightly grey. `#fef7f0` is the
same hue taken lighter, so the pale band still reads as the light end of one family.
The sticker colours — gold, sage, band green, the ten spice accents — are untouched.

**This supersedes the sweetgreen note above.** That paragraph argues the cream should
carry a green-yellow cast so it and the sage read as one family. `#fcedde` is a warm
peach cream and deliberately does not. The cream half of the page and the sage half are
now two families rather than one, which is closer to how Oddbox actually works (their
cream sits against olive, not against a matching green).

### The hero foot, again

`.vig` hardcoded `rgba(253,252,248,…)` — the old `--ivory` — in three places, because
the dissolve needs alpha ramps and cannot use the token directly. That value is what
made every hero slide meet the next section with no tonal step (the fix logged in
progress entry #33). Moving `--ivory` without moving those three stops would have put
the seam straight back. They are now `rgba(254,247,240,…)`. **If `--ivory` ever moves
again, grep `.vig` and `.field` for its literal rgb first.**

### Verified

Ran the contrast audit twice in one pass — once with the new tokens, once with the old
ones re-applied to `:root` at runtime — and diffed by element. **Zero regressions: no
element crossed from passing to failing, and the failure count is identical under both
palettes.** Diffing against a baseline rather than reporting an absolute number is the
honest test here; a naive audit reports the same crop of false positives either way
(decorative gradient stops read as grounds, low-alpha marquee glyphs).

Also confirmed in the browser: `.essentials` computes to `rgb(252, 237, 222)`, the white
product cards now sit on cream exactly as Oddbox's do, and the mission hinge still
resolves cream → sage at full scroll.

## Recipes, rebuilt as a category — and the de-duplication that came with it

Two changes on 5 Sep 2026, both from references the owner sent.

### The recipe index, after flamingoestate.com

Their recipe index is photograph-first: a four-across grid where the picture carries
the card, the title sits under it in a serif, and the byline is the only other thing on
it. Ours takes the structure and keeps its own furniture — the cook-time badge (from
dandelionchocolate, logged above), the Marathi name under the English one, and
`MADE WITH <product>` in that product's own accent colour, which is our equivalent of
their byline: it says what of ours the dish needs.

**Fifteen recipes in two tabs**, from `RECIPES` in `js/satva.js`:

| With our masalas (9) | With our seeds & grains (6) |
|---|---|
| Everyday Varan Bhaat · Sunday Biryani · Aitwarcha Rassa · Chole · Bhel · Masala Shengdana · Misal · Bharli Vangi · Kanda Lasun Zunka | Jeera Bhaat · Fodnicha Poha · Methi Dal Tadka · Javas Chutney · Overnight Chia · Quinoa Bowl |

The seeds tab exists because the range is no longer masala alone, and a seed needs a
use before anyone buys it. Every card's `id` keys its photo, **not** its `uses` — so
two recipes may share a product, which the old `uses`-keyed filename could not do.

**Kanda Lasun Zunka has no photograph and sits last in its group on purpose.** The
free pools have no honest zunka: the near misses were a keema-style crumble, a khichdi
and a bhaji. It keeps its designed tile, and the tile leads no row.

### Where the recipe photographs came from

Pexels, 14 photographs, **free for commercial use with no attribution required** —
route 1 of the two the "Sourced photos" section above recommended. Every one was
looked at before it was used, and two were rejected after looking: a quinoa bowl whose
hero was a salmon fillet, and every "zunka" candidate. Cropped 4:5 at 880×1100 from
the largest copy the CDN serves, ~2.1 MB for all fourteen.

The earlier finding still stands and is worth restating: the CC pool has **no studio
photography of Indian ground masalas**, which is why the products still have tiles. It
does have good photographs of *cooked dishes* — which is exactly what a recipe card
needs, and why this section could be dressed when the range could not.

### Shop by category, rebuilt — and Everyday Essentials deleted

The owner's note was "I don't want the spices to be repeated in the home page", and it
was correct. Three blocks were introducing the same products:

- **Shop by category** — 6 shelves
- **Everyday Essentials** — a curated row of 13 products
- **The range** — all 21

Everything in Essentials was already in the range, so **Everyday Essentials is gone**
(section, renderer, and its CSS except the `.etab` styling the recipe tabs now use).
It also had a bug worth recording: **Cumin Seeds appeared twice inside it**, being in
both the "Kitchen staples" and "Whole spices" lists.

What remains is one listing and one way in: the categories filter the range rather than
restating it. Verified — 21 products, each appearing exactly once; clicking Blends
selects the Blends tab and shows exactly its 6.

The category cards themselves are now photograph-led, after the two references:

- **uk.huel.com** — the label sits ON the photograph, and the block is given far more
  air than a product grid gets. Their four cards carry a whole viewport between them.
- **jainfarmfresh.com/products/spices** — one honest photograph per category, no icon
  standing in for a product.

**Three across, not six.** Six categories at six-across made every photograph a stamp;
at three-across on two rows each picture is large enough to be worth taking. Six new
photographs — `assets/cat-{ground,whole,blend,seeds,pantry,oils}.jpg` — cover exactly
what the owner asked for: spices, masala, seeds and oil. **The branded oil bottles in
the pool were rejected**: several otherwise-good shots carry another company's label,
and the rule from the product-photo section applies here too — a shot of someone
else's pack is not ours.

### The scrim, and why it is short

A label on a photograph needs a scrim, and the first one (62% tall, flat to
transparent) read as a grey smudge across the pink-salt and oil shots, which are light.
It is now **52% tall and much darker at its foot**, so it reads as a shadow the label
sits in rather than a wash over the picture.

**Verified by sampling the rendered pixels, not by eye** — the labels were hidden, the
page screenshotted, and the exact label rectangles sampled out of the PNG:

| Category | Mean ground behind the label | White text | Worst single pixel |
|---|---|---|---|
| Ground spices | `rgb(29,31,17)` | 16.7:1 | 10.0:1 |
| Whole spices | `rgb(39,41,25)` | 14.8:1 | 9.6:1 |
| Blends | `rgb(18,24,14)` | 18.1:1 | 11.7:1 |
| Seeds | `rgb(53,52,36)` | 12.6:1 | 7.9:1 |
| Pantry | `rgb(59,67,60)` | 10.2:1 | 8.9:1 |
| Oils | `rgb(64,70,60)` | 9.7:1 | 7.4:1 |

Sampling beats modelling here: an earlier attempt to *calculate* the scrim's alpha from
the gradient stops returned 0.12 for all six, which is plainly wrong at the foot of the
gradient. If you re-check this, hide `.cname`, screenshot, and read the pixels.

### Two bugs found doing it

1. **`.recgrid[hidden]` kept rendering.** An author `display:grid` beats the `[hidden]`
   attribute's UA `display:none`, so both recipe tabs painted at once. This is the same
   trap already logged for `.etrack`, re-entered because the new grid was written from
   scratch. Fixed with `.recgrid[hidden]{display:none;}`.
2. **Inactive tab labels were 4.22:1.** `--sage-soft` on the cream ground — and it was
   already only 4.46:1 on the *old* cream, so this predates the repalette. Inactive
   tabs now use `--sage` (4.74:1). This fixes the range tabs too, not just the new ones.

### Still to do here

- A real zunka photograph — the one card still on a tile.
- The recipes are written in our voice and are ordinary household method, not claims
  about the business, so they did not need the owner. **The seed recipes should still
  be read by him** before they go public: the methi-seed count and the flax-chutney
  keeping time are the kind of detail a cook will test.

### One knock-on: the category block moved to cream

Deleting Everyday Essentials broke the alternating-ground rule from the section above
("no two adjacent sections share a family"). Essentials carried the cream that sat
between Shop by category and the range — with it gone, **two sage sections met**. The
category block is now `--cream-sg`, which restores the alternation and is also what
jainfarmfresh puts behind its own category cards, so the reference and the ground rule
agree. Re-verified down the whole page: **zero adjacent sections sharing a family.**

```
hero cream · reasons ivory · cats CREAM · range sage · recipes cream · origin sage
trace ivory · mission hinge · why sage · promise cream · story sage · saheli DARK
voices cream · contact sage
```

## Two corrections from the owner, 5 Sep 2026

### The category pictures are shorter, so all six read as one block

The photographs were right; the frame was not. At 4:5 each card ran ~530px tall, so at
a ~1280px viewport one row of three filled the screen and the second row always sat
below the fold — six shelves that never appeared together.

**The frame is now 3:2.** Card height went 530px → 334px, and the whole grid is 698px,
inside an 800px viewport, so the six sit in one screen. The grid also widened
(1180 → 1280) and the gaps tightened, both to buy that height back.

The asset files were **re-cropped to 3:2 at source** rather than left portrait for the
browser to crop — a 4:5 file in a 3:2 frame throws away a third of the picture and
picks the middle of it, which is not where the subject necessarily is. 1200×800 each,
~1.0 MB for all six.

The scrim moved with the frame: on a shorter card it went from a shadow to a wash over
half the picture, worst on the light pink-salt and oil shots. It is now **46% tall and
harder at its foot**. Contrast was re-sampled from the rendered pixels after the change
(see the method above) and every label still clears AA comfortably.

### The range is a menu now, not a listing

The owner: *"Keep this only as a section menu, and only if the user selects, then
display all the items on the screen."*

Before, `Everything` was selected on load and all 21 products were listed before anyone
had asked for any of them. Now **nothing is listed until a shelf is chosen**:

- no tab starts selected; every `.pcard` starts `hide`
- `#rangepick` — a dashed prompt — holds the grid's space, and is removed for good on
  the first choice
- one entry point, three ways in: the tab pills, the six photo cards further up, and
  the header's *Our Range* dropdown all call the same `showGroup()`

Verified: on load 0 products and no selected tab; picking Seeds lists exactly its 3;
the Oils photo card lists exactly its 4; `Everything` still lists all 21.

**A card revealed this way needs `.in` adding by hand.** It was `display:none` when the
page loaded, so the reveal observer never saw it and it would return at opacity 0 —
the same trap the recipe tabs hit.

### `[hidden]` is now handled once, globally

This bug has now been found three times in this file — `.etrack`, `.recgrid`, and
`.rangepick` — and each time it was patched for that one selector:

> the `[hidden]` attribute is only a UA `display:none`, so **any** author `display:`
> rule beats it and the element keeps rendering.

There is now a single `[hidden]{display:none!important;}` next to the box-sizing reset
at the top of the file, and the per-selector patches are gone. Anything toggled with
`el.hidden` from here on will actually hide, including whatever gets built next.

## The recipes now run as a strip, after graza.co

The owner asked for "Cook something for someone" to move in slides, pointing at the
*See what else we're cooking up* marquee on graza.co. Measured off their live page
5 Sep 2026 rather than guessed at:

| Theirs | Ours |
|---|---|
| Fixed card width, **varying heights**, top-aligned | same — `--rar` cycles `4/5 · 1/1 · 3/4 · 5/6 · 4/5 · 2/3` |
| 20px corners | the card's existing 18px |
| Set duplicated **exactly twice**, track translated on a linear loop | same |
| 20s linear infinite | measured pitch ÷ 62px per second |
| Bleeds edge to edge, leftmost card cut by the viewport | same |
| **Does not pause on hover** | **pauses** — see below |

**The one deliberate divergence: ours pauses on hover and on keyboard focus.** Their
slides are photographs and nothing else, so movement costs the reader nothing. Ours
carry a name, a Marathi name, a cook time and the masala the dish needs — a moving
target you cannot finish reading is worse than no movement.

### The seam bug, which is the whole trick

The obvious loop is `translateX(-50%)` on a track holding two copies. **It stutters**,
and it took measuring to see why: with a flex `gap`, half the track is `9w + 8.5g`
while the set actually repeats every `9w + 9g`. The loop is therefore half a gap short
on every single pass — 10px here, which reads as a jolt.

So the shift is **measured, not computed**: `--shift` is the real pitch from a card to
its own duplicate (`kids[setLen].offsetLeft - kids[0].offsetLeft`), set from JS and
re-measured on resize, because the card width is clamped to `vw`. Verified exact at
1280px (pitch 2488 = shift 2488), on the shorter seeds strip (1659 = 1659), and again
after resizing to 390px (2178 = 2178).

Speed is held constant at ~62px/s rather than a fixed duration, so the 9-card masala
strip runs 40s and the 6-card seeds strip 27s and both *feel* the same.

### The bleed, and the 7px

`width:100vw` counts the scrollbar, so the full-bleed strip put **7px of horizontal
overflow on the whole page**. `.recipes` now has `overflow-x:clip`, which contains it
without clipping the sticky header or breaking the mission section's scroll effect.
Page overflow re-checked at 1280px and 390px: zero at both.

### Reduced motion

`prefers-reduced-motion: reduce` stops the animation, hands back a real scrollbar
(`overflow-x:auto`), and **hides the duplicate set** — the second copy exists only to
make a loop that is no longer running, and leaving it would show every recipe twice.
Rules confirmed present by reading them back out of the parsed stylesheet.

### A note on testing a moving component

Playwright refuses to hover a card in the strip — *"element is not stable"* — because
it is moving. That is a useful signal rather than an obstacle: hover the stationary
container instead, then assert on `animationPlayState` and on the `transform` not
changing across a timeout. Confirmed paused, transform identical over 700ms.

## The recipe strip moved up under the hero — 6 Sep 2026

The owner asked for it "in the hero section", and chose, of the options put to them,
moving the **whole block** — heading, tabs and strip — to sit directly below the hero
rather than embedding the strip inside the hero itself. The hero keeps its slider,
headline, buttons, floating card and powder canvas untouched.

New order: **hero → Cook something for someone → Why choose → shelf slider → Shop by
category → the range → Origin → …**

### It broke the ground order in two places at once, not one

Moving a section moves *two* seams. The strip was cream and the hero is cream, so they
met; and taking it out from between the range and Origin left **those** two both sage:

```
before          hero cream · … · range SAGE · recipes cream · origin SAGE
after the move  hero cream · recipes cream ✗ … · range SAGE · origin SAGE ✗
```

Resolved by a swap rather than a new colour: **recipes took sage, Origin took the cream
recipes gave up.** Re-checked down the whole page — zero adjacent sections sharing a
family. This is the second time a section move has broken this rule (deleting Everyday
Essentials was the first), so it is worth saying plainly: **moving or deleting a
section always requires re-running the adjacency check, because it changes two seams.**

### The eight contrast "failures" in Origin are the known false positives

Putting Origin on cream made an audit report 8 failures at 1.15:1 there, which looks
alarming and is not real. `.ocard::after` is a scrim —
`linear-gradient(to top, rgba(30,44,22,.82), transparent)` — over the card's own photo
field, so the white copy has never sat on the section ground at all; an audit that
walks up to the first opaque background walks straight past a gradient on a
pseudo-element and finds the section.

Settled by sampling the rendered pixels rather than trusting either result: the true
ground behind that text is `rgb(82,73,37)`, giving **7.65:1 average and 5.97:1 at the
worst single pixel** for its `rgba(255,255,255,.9)`. Unaffected by the ground swap, as
expected. The README's earlier note stands — accept alpha ≥ 0.5 *and* read
pseudo-element gradients, or just sample the pixels.

### Console 404s are expected

18 of them, all `probe.src` misses for art that does not exist yet: 15 un-photographed
products, the two Origin region placeholders, and `recipe-zunka.jpg`. No script errors.
Each one is a card correctly falling back to its designed tile.

## The shelf slider is now the hero — 6 Sep 2026

The owner asked for the shelf slider ("The Pantry Shelf — Unrefined, Unbleached") to
open the page in place of the five-slide brand hero. The slider moved to the top,
took `id="top"` so the logo still links home, and the old hero was removed.

**The old hero is not lost.** Its full markup — five slides, the headline "Bringing
absolute purity to the heart of the Indian kitchen", the floating product cards, the
NEXT card and the powder canvas — is saved as **`REMOVED-old-hero.html`** in the
session scratchpad. Nothing in it exists anywhere else on the page, so if any of that
copy is wanted back it has to come from that file.

### What the page loses by opening here, and it is worth a decision

The site now opens on **a product shelf rather than a brand statement**. The old hero
said what DS Satva is before showing what it sells; the first thing a stranger now
reads is "Whole Spices — Ground When You Cook". That may well be the right call for a
shop, but it is an editorial change, not just a layout one — the brand line has no
other home on the page.

### Two things that only worked because the hero existed

1. **The floating WhatsApp button.** Its IntersectionObserver was written *inside*
   `if (hero && slides.length)`, observing `.hero`. With the hero gone that whole block
   stops running, so the button would have sat invisible forever — no error, no
   console warning, just permanently missing. It is now its own block, observing
   `main > section` — whichever section happens to open the page — so it survives the
   next reshuffle too. Verified: hidden at the top, shown after scrolling, hidden
   again on return.
2. **`grind.js`** (the powder over the hero) is inert: it guards on `.hero` and
   `#grind`, both of which went with the hero. The file is still loaded and does
   nothing. Left in place rather than deleted, in case the hero comes back.

### Checked after the swap

- Ground order: **zero adjacent sections sharing a family** (`shelves → recipes sage →
  reasons ivory → cats cream → range sage → origin cream → …`)
- The slider still drives from its own 5-tab strip; the CTA still points at `#range`
- No horizontal overflow; console is the same 18 expected image 404s, no script errors

**Still not autoplaying.** The original reason ("two carousels fight each other") named
a hero that no longer exists, but it still holds because the recipe strip below moves
on its own. The stale comment in `index.html` has been corrected. Easy to turn on.

### The hero photograph: smaller, and tapered out to the left

Two asks, and the first one has a trap in it.

**"Reduce the size" — narrowing alone made it bigger.** The frame went from
`min(50%,840px)` at `inset:0` to `min(44%,620px)`, and the picture got *larger*:
`object-fit:cover` crops harder the taller and narrower its box becomes, so a
42%-wide full-height frame zoomed into the cinnamon instead of showing the flat-lay.
The height had to come down with the width. The frame is now inset top and bottom by
`clamp(26px,4.5vw,58px)`, which crops less, so more of the photograph fits and
everything in it reads smaller. Measured: the cover scale fell from **0.90 to 0.74**.

**The taper.** The old mask was a short feather, fully opaque by 24%. It is now a
five-stop ramp that reaches full opacity only at **78%**, so the picture fades the
further left it goes and its left half is a whisper on the ground. Five stops rather
than two because a straight ramp bands visibly over that distance — the slope has to
ease rather than step.

### The seam this introduced, and why the fix is two elements

Insetting the frame put its top and bottom edges on-canvas, where they read as two
hard cuts. The obvious fix — two mask layers on one element, composited — produced a
**hard vertical edge down the entire photograph**, measured at `x=708` with a delta of
118 against a smooth surround. Cause: setting both `-webkit-mask-composite:source-in`
and `mask-composite:intersect`, which are different syntaxes that do not agree on
which layer wins.

The fix is to need no compositing at all: **the vertical feather lives on `.sh-shot`,
the long left taper on the `img` inside it.** Two single-layer masks on two elements.
Re-measured after: worst column delta **17**, and that is photo detail, not an edge.

**A note on measuring an edge.** "Darkest pixel in the row" is the wrong test and it
raised a false alarm here — it reports whatever dark detail sits anywhere along the
row, so a dark spice near the top of the frame looks like a hard bottom edge. Read a
**single column top to bottom** instead: a feather is a monotonic ramp into the ground
(`76 → 115 → 152 → 213 → 242`), an edge is a step.

### Checked

- Left edge smooth on the **darkest** slide too (Ground Spices, max delta 5), so no
  slide needs the `.deep` long-dissolve class that exists for dark photos
- Top and bottom feathers ramp over ~55px into the ground, verified by column
- **Mobile:** the `max-width:900px` block turns the panel into a full-width band and
  already cleared the image mask — the new *container* mask needed clearing too, or it
  would have faded the top and bottom of that band. Both are off below 900px.
- No horizontal overflow at 1280px or 390px

## The footer stands on a pinned photograph — 6 Sep 2026

After the band at the foot of dip-a-chip.com. Their `<footer>` carries nothing; the
effect is one section above it with **`background-attachment:fixed` + `background-size:
cover`**, so the image holds still in the viewport and the section scrolls over it like
a window. That is the whole technique.

**The picture is ours.** `assets/footer-collage.jpg` is a contact sheet built from
twelve photographs already on this site — the six category shots and six recipe shots —
4x3 with ink-green gutters.

**Two layers, two attachments:** `background-attachment:scroll,fixed`. The scrim scrolls
with the footer so it always covers exactly the footer; only the photograph is pinned.

**Verified pinned, not assumed:** the same point of the footer was sampled at two scroll
positions 267px apart — mean channel difference 18.5, i.e. different photo content under
the same point. A background that scrolled with the footer would have been identical.

**Contrast over twelve different photographs.** Sampled from the render with the text
hidden. At the *lightest* background pixel `rgb(51,64,42)`: body 6.23:1, headings 8.22:1.

- The gutters were first drawn in band green and **glowed** — band green is lighter than
  the ink scrim, so they read as a visible grid. Redrawn in the scrim's own ink.
- **`.fnote` was 3.89:1** — below AA. It was **3.13:1 before this change**, on the flat
  band; the photograph did not cause it, it only made it visible. Raised to `.68`.
- `background-attachment:fixed` is a jank source on touch and **iOS Safari ignores it
  outright** (renders as scroll — still fine, just no parallax). Set to `scroll`
  explicitly under 900px and under `prefers-reduced-motion`.

## Vibrancy, after jainfarmfresh — and blocks that fit the screen

**The spice colour is pushed harder now**, at the owner's request, in three places so the
page agrees with itself: the five hero slides (`--vib` lifted ~0.18 each, now 1.21–1.38),
the category and recipe photographs (`saturate(1.18)` / `saturate(1.16)`), and the footer
collage (rebuilt at 1.35, pushed hardest because a .90–.94 scrim drains colour).

This reverses the note in the `--vib` block above, which held saturation to 1.00–1.20 on
the argument that a brand whose case is "colour comes from the spice, not a dye drum"
should not push colour. **That was a deliberate position and the owner has overruled it** —
worth knowing if the argument ever comes back.

### Each block fitting the screen

Two parts, and the honest result is partial.

**Padding cut about a third** across every section — that is where the height actually
was. **8 of 15 sections now fit** a 719px usable viewport (800px less the 81px header),
up from 7, including `why`, which missed by 2px.

**Seven still do not, and cannot without cutting content:**
`story 1401px (+682)` · `cats 1135 (+416)` · `recipes 1055 (+336)` · `origin 947 (+228)` ·
`voices 899 (+180)` · `range 864 (+145)` · `reasons 803 (+84)`

**Snapping is `proximity`, not `mandatory`, and deliberately.** Mandatory snapping on a
section taller than the screen traps the reader — the browser drags them back to the top
of a block they were reading down. Verified: scrolling to 300px short of every one of the
14 sections settles it at exactly **88px**, clear of the sticky header
(`scroll-padding-top`).

### Why snapping did nothing at first, which is worth remembering

The snap rules were correct and had **no effect at all**. The cause was three rules away:

```css
body{ overflow-x:hidden; }     /* to kill sideways scroll */
```

**A hidden axis forces the other axis to compute as `auto`** — which makes body its own
scroll container. The sections' nearest scroll container was therefore body, while the
page actually scrolls `html`, so snap rules on `html` had no snap areas to act on. Moving
the rules to body did not fix it either; the fix is to stop body being a scroll container:

```css
body{ overflow-x:clip; }       /* clips without creating a scroll container */
```

Horizontal overflow re-checked after the change: still zero.

### Making the blocks actually fit — the height-aware pass

The first attempt at "each block fits the screen" only cut padding, and it was not
enough, because **every size on this page was tied to viewport WIDTH**. A wide but
short window — a laptop with browser chrome and a bookmarks bar, about 660px of page —
still got full-height headings, 610px hero slides and 318px recipe images. Nothing
fitted, and no amount of padding would have fixed it.

The fix is a `@media (max-height:1000px)` pass where the shared parts answer to
**height**: `vh`-based clamps on section padding, display headings, ledes, and — the
important one — on the things whose height is set indirectly:

| What | Why it is sized by height now |
|---|---|
| `.recmq .reccard` width | a card's image height comes from its WIDTH via the aspect ratio, so the only way to shorten the strip is to narrow the card |
| `.catgrid` max-width | same: the 3:2 photo follows the card width down |
| `.shelf` min-height | was `clamp(430px,52vw,610px)` — pure width, so a short window still got 610px |
| `.sh-copy` padding-block | 86px top and bottom was what kept the hero at 719px after its min-height already answered to vh |
| `.origin .ofield` | the photo was 428px of a 430px card |

Ledes and card descriptions clamp to two or three lines rather than shrinking to
nothing. The breakpoint is 1000px, not 780px: every value inside is a `vh` clamp so it
scales up smoothly, and cutting it off at 780 left a 900px window with none of it.

**Result, measured:**

| Window | Sections fitting | Still over |
|---|---|---|
| 1280×900 | **14 of 15** | story +363 |
| 1280×660 | **13 of 15** | origin +117, story +578 |

**`story` cannot be made to fit, and should not be.** It is nine paragraphs of prose —
the drop cap, the pull quote, the whole argument of the brand. At 660px it would have
to lose roughly half its text. That is a content decision, not a layout one.

`origin` at 660px is three cards of photo + place + blurb + link; it fits at 900px and
is 117px over at 660px. Losing the blurb line would do it, at the cost of the sourcing
copy.

**A dead end worth recording:** `.families` was forced to two columns to save height,
which made it *taller* — 686px to 829px. Its default is
`auto-fit/minmax(210px,1fr)`, which already puts all five on one row at desktop widths.
Two columns meant three rows. Reverted; only its spacing and type came down.

## The hero slider autoplays and fills the screen — 9 Sep 2026

The owner asked for a hero that advances on its own and fits the screen, after
consciousfood.com, and asked explicitly that nothing else change. Two edits, both
inside the hero.

**It fills the screen.** `.shelves.is-hero` is `calc(100svh - 81px)` — the viewport less
the sticky header — as a flex column: the bar of tabs and arrows sits at its foot and
the stage takes the rest. `svh`, not `vh`, so a phone's collapsing address bar does not
leave a gap. The slide's old `min-height` stays as the floor for anywhere this block is
*not* the hero. Measured: 579px in a 660px window, exactly viewport-minus-header.

**It advances every 6 seconds**, and four things keep that from being annoying:

| | |
|---|---|
| pointer over it, or focus inside it | pauses — nobody loses a line they are reading |
| tab hidden | pauses — no invisible carousel burning a phone battery |
| visitor picks a shelf, arrow or swipe | **stops for good** — once someone has chosen, moving it under them is the site arguing with its reader |
| `prefers-reduced-motion` | never starts |

The active tab carries a gold progress line while it runs, so the movement is announced
before it happens; a carousel that jumps with no warning reads as a fault. The line
disappears the moment autoplay pauses or stops.

**Verified:** advances at 6s intervals; held under the pointer for 9s it did not move;
on leaving, the progress line returned; after clicking Pantry it stayed on Pantry for
9s with no line. **Nothing else moved** — every other section measures exactly what it
did before (`shelves 514→579` is the only change), 13 of 15 still fit at 660px, zero
horizontal overflow.

### Hero type: bigger, and spread across the breadth

The owner: the letters looked small against the photograph, and the middle of the hero
read as a hole. Both were true, and the cause of the first was **my own height-aware
pass** — `min(4.2vw,5.6vh)` with a `1.45rem` floor resolved to a **37px headline and
13px body copy** on a 660px-tall window, next to half a metre of photograph.

| | before | after |
|---|---|---|
| headline, 1600×900 | 53px | **62px** |
| headline, 1280×660 | 37px | **49px** |
| body, 1280×660 | 13px | **17px** |
| copy column | `min(620px,53%)` | `min(780px,62%)` |
| paragraph measure | 46ch | 56ch |

The column can run to 62% because the photograph's left half is a whisper under its
taper — it only becomes solid at 78% of its own width. Checked: at 1600px the copy ends
at x=934 and the photo is solid from x=1387, so nothing readable sits on anything busy.

**One regression this caused, found by measuring.** Running the paragraph further right
puts it over the faint end of the photograph, where `--sage` measured **4.28:1 at its
darkest pixel** — under AA, though its average (4.89:1) passed. It is now `--green`:
**8.89:1 on the same ground**, and still clearly secondary to the `--ink` headline.
(Averages hide this sort of thing; the darkest pixel under the text is the test.)

Verified across all five slides at 1280×660: every headline still holds its intended
**two lines**, the copy clears the stage with 17px to spare, nothing overflows, the hero
still fills the screen exactly, and horizontal overflow is zero.

### Shop by category moved to second, and spread across the breadth

Two asks: bring the fourth block up to second, and stop the six cards sitting in a
narrow middle column.

**Order now:** hero → **Shop by category** → Cook something for someone → Why choose →
the range → Origin → … Ground alternation re-checked after the move: **zero adjacent
sections sharing a family** (`shelves grad · cats cream · recipes sage · reasons ivory ·
range sage · origin cream · …`).

**Why it was stuck in the middle, and it was not the grid.** `.catgrid` had a
`max-width` — but a child cannot outgrow its parent, and `.wrap` is 1280px. On a 1920px
screen that left **365px empty on each side** whatever the grid asked for. `.cats .wrap`
is now `min(1720px,94vw)`; the grid fills it.

There was also a `max-width:min(1080px,86vh)` in the height-aware pass — capping a
block's **width by the viewport's height**, which is what squeezed it into a column on a
short wide screen. Removed: one row of six is shorter than two rows of three anyway, so
the height problem it was solving solves itself.

**Six columns, explicitly — not `auto-fit`.** `auto-fit` does not know there are six
cards: at 1280px it produced **five tracks and stranded the sixth card alone** on a
second row. The counts are now 6 / 3 / 2 / 1, every one a divisor of six, so no row is
ever left with an orphan.

| Window | Columns | Rows | Grid width | Section height |
|---|---|---|---|---|
| 1920×1015 | **6** | 1 | 84% of screen | 702px — **fits the screen** |
| 1280×660 | 3 | 2 | 86% of screen | 801px — over that window's 579px |

Worth being straight about the second row of that table: at 1280 the block is balanced
(3+3) but no longer fits a short window. Six across at that width would fit, but the
cards fall to ~170px and the photographs stop being worth showing. Balance won; say so
if the fit matters more.

## "Where it comes from" — moved to third, and rebuilt

The owner did not like the block and asked for it third. Fair: it rendered all three
`ORIGINS` entries as equal full-height cards, so **two thirds of the section was a
placeholder** — two tall panels of empty gradient saying *Region to be named*.

The honesty was right. Those regions are not confirmed and this page does not invent a
sourcing story. But **giving an unknown the same visual weight as a known fact is a
design error, not an honest one** — the one thing the section can actually state was
outnumbered two to one by things it cannot.

**Now:** the named place leads — a wide, low, horizontal card, photo panel on the left,
copy on an ivory panel on the right. The two unconfirmed regions sit beside it under
*Still to be named*, as small dashed notes. Still visible, still plainly unfinished,
sized like what they are. **When a region is confirmed, drop its `todo` flag in
`ORIGINS` and it renders as a lead card of its own** — no CSS to touch.

The card's copy now sits on ivory rather than over a photograph, so it takes the page's
own ink and needs no scrim; only the photo panel keeps the tint-and-line-art fallback
while `assets/origin-grind.jpg` does not exist.

**Two things caught by checking rather than by eye:**

1. **The move broke the ground order — for the third time.** Third position put `cats`
   (cream) next to `origin` (cream). Origin is now `--ivory`, which sits correctly
   between cream above and sage below. Re-verified: zero adjacent sections sharing a
   family. *Reordering sections always moves two seams; run the adjacency check every
   time.*
2. **The new gold chip failed AA.** `--gold-dk` on `--gold-pale` measured **4.09:1**.
   The chip stays gold; its text is now `--ink` — **10.98:1**. Every other string in
   the rebuilt block passes: place 13.86, blurb 10.37, Devanagari 5.16, link 5.16,
   pending notes 5.13.

## "How it is made" — the third block, rebuilt as a flip carousel — 9 Sep 2026

The owner replaced *Where it comes from* with this, after the **Meet Our Canneries**
carousel on eatfishwife.com: *"each spice how it's made, and when we turn, the image of
the spice there."*

**What the reference actually is,** measured off their live page rather than guessed:
a Swiper coverflow of **flip cards** — centre slide larger and in front, neighbours
scaled down on negative z-index, `2px` border, `20px` radius, and the back face rotated
`180deg`. Ours is the same behaviour with no Swiper: position comes from one custom
property per card, `--d` (signed distance from centre), so the layout is CSS and the JS
only sets a number.

**Front:** the process, on video. **Back:** the spice itself and one line about it.
Six cards — chilli, turmeric, coriander, seeds, oils, salt.

### The video

Six clips, **1.4 MB for the lot**, from Pexels (free commercially, no attribution):
chillies falling into a bowl, turmeric root on a stone grinder, stone grinding in an
Indian kitchen, sesame in a mortar, oil poured from a glass bottle, rock salt under a
pestle.

The sources are 11–320 MB each, and Pexels ignores size parameters on its download
endpoint, so they were cut locally: **6 seconds, square, 720px, silent, H.264 CRF 31**.
There is no system ffmpeg here — `pip install --target ./pylibs imageio-ffmpeg` ships a
static binary, which is what did the work. A poster frame is extracted from each so a
card paints before its video loads.

**Only the centre video plays.** Six decoding at once is a fan-spinner for no benefit;
the rest are paused, `preload="none"`, muted, looping, `playsinline`.

> **MEDIA HONESTY.** This is generic process footage — **not our mill, not our hands**.
> It depicts the process, which is true, but a visitor may reasonably read it as our
> facility. The section carries a line saying so, and the owner's own films should
> replace it. Same rule as the product photographs: a shot of loose ingredients is an
> honest depiction; anything implying it is *ours* is not.

### Three bugs, all found by measuring

1. **A stray `}` broke the whole file.** Cutting the old renderer left one closing brace
   too many, and the parser reported it 150 lines later at `var POT` — every block after
   it stopped running. `node --check js/satva.js` is the one-second version of this
   check and is worth running after any surgical replacement.
2. **`.mtrack` was already taken.** The Marathi dish marquee owns it
   (`display:flex; width:max-content` + a scroll animation). Reusing the name gave the
   carousel `width:max-content`, which with `inset:0` computes to **zero width** — so
   all six cards piled up at x=0 and threw **2849px of page overflow**. Renamed
   `.mkrow`, and every rule in the block is now scoped under `.made`.
3. **Both arrows stacked on one spot.** `.arrow` is absolutely positioned by default —
   it belongs to the hero — so only one was visible. Same override the shelf bar makes.

### Contrast over moving video, and two sampling traps

A card-wide gradient cannot be trusted over video the way it can over a still: the frame
changes, and the turmeric clip goes very bright. Measured against the brightest frame
with only the card scrim: body copy **3.20:1**, Devanagari **1.76:1** — both under AA.
The copy now carries **its own backdrop**, and where the glyphs actually sit the worst
pixel gives title **10.19:1**, body **9.08:1**, Devanagari **5.25:1**.

Getting there meant discarding two false alarms, both worth remembering:

- the first "worst pixel" was the **rounded corner**, where the page background sits
  *outside* the card but inside a rectangular sample;
- the second was a **single 1px row** at the top edge of the backdrop gradient, where no
  glyph ever renders.

Sample the box the glyphs occupy — inset from the corners and clear of the gradient's
own boundary — or the number is about the sampling, not the design.

### Bigger cards, fewer words, and a cycle that turns itself — 9 Sep 2026

Four changes to *How it is made*, all in that block.

**The cycle the owner asked for: four seconds on the front, the card turns itself, three
seconds on the back, then the next card** — which arrives on *its* front, so the rhythm
repeats rather than drifting. Verified by recording the live carousel: **3961ms →
turn → 2999ms → next**, over and over.

Two timers, not one interval, because the two halves are different lengths and an
interval cannot say that. Both are cleared on every state change, so a visitor who
clicks never gets a stale timer turning a card under them.

**It pauses on hover, on keyboard focus, and while the tab is hidden — then RESUMES.**
Unlike the hero (which stops for good once a visitor takes over), here the turning *is*
the content: stopping it permanently would leave the block sitting on one card. Verified:
held under the pointer for 9s it did not move, and it carried on when the pointer left.

**Cards are bigger** — `clamp(270px,34vh,400px)` at 4:5, up from `clamp(230px,30vh,330px)`
square: 297×371 at 1600×900, against 270×270 before. The centre card now carries a gold
edge and a deeper lift; the others sit back behind a quiet green hairline.

**The copy is cut to one line each**, front and back. This is the change that mattered
most: a card that turns after four seconds cannot carry a paragraph, because nobody
finishes it before the card moves. The long version of any of it belongs in the range or
the story.

**A trade-off worth stating.** Bigger cards took the section to 932px against 819px of
usable screen, so it stopped fitting — the thing this page was tuned for two days ago.
The stage came down from 58vh to 46vh, which keeps most of the size gain and puts the
block back inside one screen: **811px, fits, and the page is back to 14 of 15 sections
fitting** (`story` remains the only one that cannot, as before).

### The selected card is bigger and a different shape — 9 Sep 2026

The owner asked for the highlighted masala alone to be larger and rectangular, with
everything else unchanged.

`.mcard` carries the side size (`clamp(240px,31vh,360px)` at 4:5) and `.mcard.is-on`
overrides it (`clamp(280px,37vh,430px)` at **3:4**). At 1600×900 that is **333×444
against 234×293** — bigger in both dimensions and a visibly taller rectangle, so the
chosen card reads as chosen by shape as well as by position. `width` is in the card's
transition, so growing into the centre is part of the same movement as sliding there.

**Not taller than 3:4.** At 2:3 the selected card needs about 500px, which overflows the
stage, and the stage cannot grow without the section leaving the screen.

**Timing is now 4s on the front, 2s on the back** (was 3s), then the next card.
Verified live: `3999ms → turn → 2000ms → next`, repeating.

**The taller card cost 37px of screen fit**, so `.made` padding moved from
width-based `clamp(38px,4.6vw,66px)` to height-based `clamp(22px,3vh,48px)`. Section is
**778px against 819px usable — fits**, and horizontal overflow is zero.

**Widened twice more, ending landscape.** The selected card went 3:4 → 6:7 → **5:4**,
i.e. `333×444 (0.75)` → `387×452 (0.86)` → `468×374 (1.25)`, against side cards that
stay `234×293 (0.80)`. It is now a **wide rectangle among tall ones**, which is the
clearest that distinction can be drawn without touching the neighbours.

Worth knowing for next time: **going wider past square buys height back.** A 5:4 card is
shorter than the 6:7 one it replaced, so the stage shrank with it and the section came
down to **715px** — shorter than the 778px it was before the card got bigger. Widening
was free; it was the *taller* shapes that cost screen fit.

## "Cook something for someone", rebuilt clean — 9 Sep 2026

After the *Odd for every occasion* row on oddbox.co.uk: **four plain photographs, the
dish name underneath, and nothing else**. No card, no border, no badge, no scrim over
the picture — the whole point of that row is the air around it.

Out with it went the graza-style moving strip, its two tabs, the cook-time pill and the
three-line description on every card. Section height **480px**, against 819px of usable
screen.

**Four, not fifteen.** The other eleven recipes stay in `RECIPES` and are still correct;
a new `FEATURED` array picks which four show, so changing the row is one line. The four
are chosen to be genuinely everyday and genuinely good for you, and each is built on a
**different** product we pack, so the row reads as four reasons to buy four things:

| Dish | Made with |
|---|---|
| Fodnicha Poha | Mustard Seeds |
| Methi Dal Tadka | Fenugreek Seeds |
| Bharli Vangi | Coriander Powder |
| Quinoa Bowl | Quinoa |

A card whose photograph is missing now renders **nothing at all** rather than a coloured
tile — a placeholder tile was fine in a busy strip and would be conspicuous in a row this
clean.

### The accent line failed AA on this ground

`MADE WITH …` takes each product's own accent, and those accents were chosen to sit on
**white** cards. On the sage ground of this section two of the four fell under AA —
mustard **4.44:1**, quinoa **4.38:1**. Each accent is now mixed 62% toward `--ink`,
which keeps its hue and its identity while clearing the threshold:

| | before | after |
|---|---|---|
| Fodnicha Poha | 4.44 | **6.64** |
| Methi Dal Tadka | 4.88 | **7.04** |
| Bharli Vangi | 4.91 | **7.01** |
| Quinoa Bowl | 4.38 | **6.53** |

**A measuring trap worth recording:** `color-mix()` computes to `color(srgb 0.38 0.31
0.07)` — 0-to-1 components, not 0-to-255. A contrast script that assumes `rgb()` reads
those as almost black and reports a confident **17.52:1 for every card**. If a checker
returns the same suspiciously high number for several different colours, it is parsing,
not measuring.

## Three colours from uk.huel.com, in "What we will not do to your food"

The owner liked the 1st, 3rd and 4th tiles of Huel's *Food to fuel your goals* row and
asked for those colours only — not the layout. Each column of the why-choose block is
now a panel in one of them.

**Sampled, not guessed.** Those tiles have no CSS colour: the colour lives in the
photographs, each of which is a lit gradient sweep. Taking the most common pixel gives
the *shadow* side (`#9f6333` for the caramel tile, which is far darker than it looks).
The values below are the median of each sweep's **lit half**, which is the colour the
eye actually reads:

| | Huel tile | ours |
|---|---|---|
| blush | More protein | `#ce9f8b` |
| pistachio | Manage weight | `#d2d9b8` |
| caramel | Save time | `#ddaf7b` |

**Two things had to change to sit on them.** The body copy was `--sage`, chosen for an
ivory ground and much too light here — it is now `--ink` at 82%. The line art took each
panel's own colour darkened, so it reads on the panel instead of floating over it.
Measured on all three panels: headings **6.28 / 10.06 / 7.35**, body **4.51 / 6.34 /
5.07**, artwork **4.59 / 6.00 / 4.42**. All pass.

**And a gap that only appeared once there was a panel.** The illustrations occupy just
the middle of their `0 0 200 200` viewBox, so the box is always larger than the ink in
it. On a flat ground nobody could see that; inside a coloured panel it read as a hole
between the icon and the heading — **110px of it**. The box is smaller now and the
columns centre their content: the gap is **15px**, and the section is 513px.

### "Why choose SATVA" moved to third — 9 Sep 2026

Order is now: **hero → Shop by category → Why choose SATVA → How we make → Cook
something for someone → the range → …**

**It broke the ground rule in two places, which is what a move always does.** Landing
`reasons` (ivory) at third put it against `made` (ivory), and pushing `made` down put
`recipes` (sage) against `range` (sage). Both fixed by reassignment rather than new
colours: `made` took cream, and `range` swapped its sage ramp for a cream one
(`--cream-sg → --sand`). The white product cards read at least as well on it, and its
note line measures **4.74:1** there.

Re-verified: **zero adjacent sections sharing a family**, zero horizontal overflow.

```
shelves grad · cats cream · reasons ivory · made cream · recipes sage · range cream
trace ivory · mission hinge · why sage · promise cream · story sage · saheli DARK
voices cream · contact sage · footer DARK
```

That is now **four moves in a row that each broke this rule** (Essentials deleted,
recipes up, origin to third, why-choose to third). Reordering moves two seams every
time — run the adjacency check, always.

### 10 Sep 2026 — the sweetgreen plate shape on "Cook something for someone"

The owner pointed at sweetgreen.com's menu row and asked for "this shape …
the shapes of the plate inside". Measured what sweetgreen actually does before
copying it: their `.menu-item__image` is a plain 366×366 square with
`border-radius: 20px` and no clip-path or mask anywhere on the page. The shape
they liked is not the tile — it is the **bowl in the photograph**, a soft square
whose corners are so full it reads as round.

That outline is a superellipse (|x|⁴+|y|⁴=1, the "squircle"). CSS has no keyword
for it, and `border-radius` cannot make one: a radius rounds only the corner arc
and leaves the sides flat, while a squircle curves continuously the whole way
round — and it is that continuous curve that reads as a bowl instead of a
rounded box. So `.recgrid .rshot` now carries a 32-point `clip-path: polygon()`
tracing the superellipse in **percentages**, which keeps the shape true at every
card width (261px on desktop, 339px at 390px wide). 32 points puts the worst
chord error under 0.7px at the desktop size.

The photos went from 4:3 to 1:1 to suit it (`object-fit: cover` already handled
the recrop). Section height 511 → 487px, still inside a 625px viewport.

**Alignment.** The heading was `text-align:center; max-width:52ch; margin:0 auto`
sitting over a full-bleed four-column grid. Both were centred on 613, so nothing
was mathematically off — but a narrow centred block over a wide grid *reads* as
unaligned, which is what the owner saw. sweetgreen sets its type to the grid
edge, so ours does too: heading, lede, cards and the "Ask for a recipe" button
now all start at x=50 (x=18 on mobile).

One trap on the way: `.rechead` is defined twice, and the earlier definition is
a wrapping flex row left over from when a heading and a link shared one line.
Overriding only `text-align`/`margin` left it a flex container, so the h2 and
the lede were two wrapped flex items carrying the row's 24px `gap` — a 56px hole
between them. The later rule now sets `display:block` explicitly.

Verified at 1240×625 and 390×780: zero horizontal overflow, titles and the
"made with" lines each on one baseline, contrast untouched.

### 10 Sep 2026 — the paradox block deleted

"We study a phone for days. We buy our food out of habit." — `section.voices
#paradox`, the three-card comparison with the dark odd-one-out — removed at the
owner's request. Backed up to `REMOVED-paradox-block.html` (markup) and
`REMOVED-paradox-css.txt` (the `.voices/.vgrid/.vcard/.vnote` rules) in the
scratchpad before cutting, as with the earlier deletions.

What had to go with it:

- **Both "Paradox" nav links** (header and footer). The header now reads
  Our Range · Our Story · Contact. Checked every in-page `href="#…"` against the
  document afterwards: zero dead anchors.
- **The CSS**, ~25 lines. Also removed `.voices` from the selector list in the
  `max-height:1000px` short-window rule, which is where the previous deletions
  left `.why` and `.promise` behind — both are now gone from that list too.
- The block's own `How we make it` button pointed at `#made`, which still
  exists, so nothing was orphaned in the other direction.

**Ground order.** The block was a cream gradient between the saheli (dark green
`#3c5128`) and contact (sage `#e6ede0`). Removing it puts dark next to sage —
different families, so the alternation rule still holds and no seam opened.
Verified on the rendered page rather than by reading the CSS: sections now run
hero → cream → ivory → cream → mission gradient → cream → sage → dark → sage.

Page 6511 → 5889px. Zero console errors, zero horizontal overflow.

Note for future full-page screenshots: sections that have never been scrolled
into view shoot **blank**, because the reveal observer has not fired on them.
Add the reveal classes by hand before capturing, or the seam you are checking
will look like a hole.

### 10 Sep 2026 — the icon was painting over the heading in the circles

The owner reported the drawing overlapping the letters inside each circle. It
was real, and the cause was not in the circle CSS at all:

```
@media (max-height:1000px){
  .reasons .rgrid svg{width:clamp(74px,13vh,120px);height:auto;}   /* the bug */
}
```

That rule was written when these were 212px line drawings on a flat ground, and
it survived the move into the circles. `.reason .art` sized the wrapper to 55px
and `.reason .art svg` asked for `width:100%`, but this rule has the same
specificity (0,2,1) and comes later in the file, so it won: 13vh of a 625px
window is **81.25px** — the exact figure measured on the svg — and with
`overflow:visible` the extra 26px painted straight down onto the h3. It only
ever appeared on windows under 1000px tall, which is why it went unnoticed.

Diagnosing it took a detour worth recording: `getComputedStyle(svg).width`
reported 81.25px while the parent reported 54.55px, and an inline `width` of the
same `clamp()` fixed it — which looks exactly like a percentage failing to
resolve, and I wrote that down as the cause before checking. It was not. The way
to actually find it is to walk every rule in `document.styleSheets`, including
inside `@media`, and test `el.matches(rule.selectorText)` — that lists what is
really in the cascade, media queries and all, instead of what you expect to be.

Three changes:

- **`--icon` on `.reason .art`**, used by the wrapper *and* the svg, so the two
  can no longer be sized by different rules. The short-window rule now moves
  that one property (`clamp(40px,8.6vh,58px)` — smaller on a short window, which
  was its intent all along) instead of setting the svg's width behind its back.
- **`overflow:hidden` on the svg.** All four drawings sit inside their 0-200
  viewBox (the widest spans 16.3-184.4), so this clips nothing today; it is a
  guard so a future icon drawn past the edge cannot land on the type again.
- **`min-height:7em` on `.reason p`** (five lines at line-height 1.4). The four
  circles are the same size and their content is centred, so the standards card
  with three lines of copy centred its whole block 15px below its neighbours.
  Reserving the tallest body's height puts every icon and every title on one
  line across the row.

**Mobile, found while verifying.** At 390px the circles were not circles: capped
at the 230px floor meant for four-across, the content was taller than the box,
and `aspect-ratio` gives way in that case — they were rendering as 230x287
ovals, each a different height. One per row there, so the circle gets the column:
`max-width:330px`, and they are round again with the copy 28px clear of the curve.

Measured after, at 1240x625, 1440x1100 and 390x780: circles square to within a
pixel, no icon/heading overlap, every title and body inside the curve, all four
icons and titles on one baseline, zero horizontal overflow.

### 10 Sep 2026 — Our Mission rebuilt as a two-slide slider, in the Rumi layout

The owner pointed at rumispice.com/pages/about: "let this our mission block be
designed this WAY with one slider having mission and the other one story."

**The layout was measured, not eyeballed.** At 1240 wide their row is:

| | Rumi | ours |
|---|---|---|
| photograph | 368 x 556 (2:3), flush left | 360 x 540 at 1440x1100 |
| gap to the copy | 71px | 71px |
| copy | top-aligned with the picture | same |
| body type | 16px / 28.8px (line-height 1.8) | 1.04rem / 1.8 |

Top alignment is most of the look — it is what leaves the deep well of space
under the paragraph. Their tile has square corners; ours keeps the site's 20px
radius, because square corners here would be the only ones on the page.

**The picture is sized by viewport HEIGHT** (`height:clamp(280px,56vh,540px)`
with `aspect-ratio:2/3`, the column `auto`), not by width. A 2:3 portrait at
Rumi's 33% of the wrap is 556px tall, which is most of a laptop window on its
own, and this section has to fit a screen. Driving the height and letting the
ratio give the width is the only way a fixed-ratio picture can answer to the
space it has — the same trick the recipe strip already uses.

**Two slides, stacked in one grid cell** rather than laid out in a track. A
track has to have its width measured and shifted, which is the trap the recipe
marquee hit (half the track is not the pitch once a gap exists). One cell needs
no arithmetic, cross-fades for free, and takes the height of the taller slide,
so the ground does not jump when they swap.

Autoplay follows the shelf slider's manners exactly — pauses under the pointer
and on focus, pauses on a hidden tab, **stops for good** once a visitor drives
it, never starts under `prefers-reduced-motion` — at 9s rather than 6s, because
a slide here is a paragraph to read. The off slide is `inert` and `aria-hidden`,
not just faded: it is still in the grid cell, so it has to leave the reading
order too. Verified live: it advanced on its own at 9s, and after one click on
the arrow it had not moved 11 seconds later.

**Copy.** Slide 1 is the mission, word for word as it was. Slide 2 is a precis
of Our Story that introduces no new claim — every line is condensed from the
owner's own copy in the `#story` section — and it links to that section rather
than replacing it. The long story stays where it is.

**Two photographs, both Pexels, free commercially, no attribution required:**

- `mission-daily.jpg` — mung beans, rice, sunflower seeds and peppercorns in
  small bowls on warm stone (7421306, Vie Studio)
- `story-stone.jpg` — a stone mortar and pestle with dried chillies and whole
  spices (33428717, shootsaga)

Centre-cropped to 2:3 and resized to 900x1350, ~145KB each. **Neither shows a
person, a pack or a facility** — deliberately. Rumi puts a founder portrait
here, and a stock portrait beside the words "Our story" would read as our
founder, which is exactly the line the media-honesty rule draws. A stone mortar
carries the same meaning and claims nothing. The owner's own photograph should
replace it when one exists.

The colour-shifting ground stays untouched: it is the thing the owner asked for
when this section was built, and the new layout sits on top of it.

Checked at 1240x625, 1440x1100 and 390x780 (one column, picture 4:3 above the
copy): fits the viewport at every size, zero horizontal overflow, no console
errors, and next/prev/dots all drive it with `aria-selected` tracking.

### 10 Sep 2026 — the mission slide after brightland.co, and the story folded in

Two changes to the slider built earlier today.

#### 1. The mission slide, in Brightland's layout

The owner pointed at brightland.co. Their mission block **reverses** the Rumi
one: copy on the LEFT, picture on the RIGHT, the mission set as a **quotation**
rather than a headline, and signed underneath. Measured at 1240 wide:

| | Brightland | ours |
|---|---|---|
| copy column | 677 | 666 |
| quote | 40px, breaking at 26 characters | clamp to 2.35rem, capped 26ch (624px vs their 621) |
| picture | 449 x 520, 18px radius | 440 x 313 at 625px tall, 439 x 540 at 1100 |
| column gap | 18px | 20px |
| caption | 12px, letter-spacing .6px, capitalised | .72rem, .1em, uppercase |

The tight 18px gap is the deliberate part — it makes the picture read as a panel
butting against the words rather than a separate column — and it is the thing
that went wrong twice while building it:

- `.mscopy` still carried the Rumi slide's `max-width:64ch`, so the copy box
  ended at 722 while the picture began at 875. Brightland's 18px gap had become
  **153px**. The measure now lives on the quote (26ch) and the paragraph (46ch),
  where it belongs, and the column is free to meet the picture.
- Sizing the picture by viewport height (right for the Rumi slide) left the
  quote ending **201px** short of it on a laptop window. On Brightland the
  picture fills a *share* of the width — 39% against the copy's 59% — and is
  cropped to fit. Doing the same restored the gap to 20px.

**The signature.** Brightland signs this with a scan of the founder's
handwriting and her name. There is no signature and no founder name anywhere in
this project, and inventing either would be a lie on the owner's own page — so
it is signed with the brand mark and the words already used to sign off Our
Story. Swap in a scan and a name when they exist.

`mission-daily.jpg` was **re-exported square** (1100x1100). The slot's ratio
runs from 1.4:1 on a short window to 0.81 on a tall one, and the old 2:3
portrait master crushed to a hard centre crop at the wide end — partial bowls at
both edges. A square master crops honestly at both extremes; both were rendered
and looked at before the change was kept.

#### 2. Our Story now lives inside the story slide

"Take the whole story from this block and keep it here in this block itself, so
that when the Read the whole story is clicked, the person is able to read the
whole story." The standalone `section.story` is gone; its markup moved verbatim
into the story slide behind a disclosure.

- **`id="story"` moved onto the slide**, so every existing `#story` link — the
  nav, the footer, the dropdown — still lands in the right place. `satva.js`
  listens for the hash on load and on `hashchange`, turns the slider to that
  slide and opens the story, because otherwise the link would land on a slide
  that is faded out and a story that is shut.
- **Opening stops autoplay for good.** Sliding an article out from under someone
  mid-paragraph is the worst thing this carousel could do.
- The summary is swapped **out** when the full text opens rather than sitting
  above it, so the same ground is not covered twice on one screen.
- The collapse is `grid-template-rows: 0fr -> 1fr`, the animatable way to reach
  `height:auto`. That needs **one** inner wrapper: `0fr` sizes only the first
  row, and the story has nine children, so the other eight would have stayed at
  their natural height. `.msfullin` is that wrapper.
- The story's own styling (`.first` drop cap, the ICMR pull-quote and cite, the
  four promise ticks, the sign-off) was rewritten to hang off `.msfull`, since
  `.story` no longer exists.

Ground order after the deletion: `recipes` cream meets `saheli` dark. Different
families, so the alternation rule holds.

#### A trap worth recording

`@media` adds **no specificity**. The one-column phone rule was written as
`.msslide{grid-template-columns:1fr}` (0,1,0) while the Brightland slide sets
`.msslide.brt{...59fr 39fr}` (0,2,0) — so on a 390px phone the Brightland slide
stayed two columns, with the copy crushed into a 128px strip 637px tall. Inside
a media query the overriding rule has to name the same classes.

Verified at 1240x625, 390x780 and by following `#story` cold: no console errors,
no horizontal overflow, the disclosure opens to 917px of story (drop cap, pull
quote, four promise lines, sign-off) and closes again, and the picture leads the
copy on a phone on both slides.

### 10 Sep 2026 — Satwa Saheli up, Cook something for someone down

Straight swap of the two blocks. The order is now:

    hero → shop by category → why choose → how we make → mission/story slider
         → Satwa Saheli → cook something for someone → contact

**Ground order re-checked, because a swap disturbs two seams, not one.** The
families now run: cream, ivory, cream, gradient(cream→sage), DARK, cream, sage —
no two adjacent sections share a family. Verified by reading the *rendered*
background of every section and comparing neighbours, not by reading the CSS.

Two comments in the stylesheet were describing neighbours this move invalidated,
and both were corrected rather than left to rot:

- `.mission` said its cream→sage shift ended on "the sage of the section after
  it". The section after it is now the dark green Saheli band, so the shift no
  longer lands on its neighbour's colour — it carries the page from cream into
  the dark.
- `.recipes` said its cream was what stopped "sage meeting sage" after the Dil
  Se Pure block was deleted. It now sits between the dark Saheli band and the
  sage of Contact, where cream is still the only one of the four grounds that
  works.

No dead anchors (`#saheli` and `#recipes` both still resolve), no horizontal
overflow, no console errors. Page 4783px.

**Pre-existing, not caused by this move:** `shop by category` is 691px against a
625px window, so it is the one section that does not fit a short screen. It was
that height before the swap too. Flagged, not silently changed.

### 10 Sep 2026 — bigger story picture, a Vahdam circle for the mission, and a first-click bug

**The story picture, bigger.** 56vh matched Rumi's 556px exactly, but on the
laptop window this is actually read on (625px of page) that came to 233x350 and
left 137px of screen unused under the block. Now 74vh: **308x463** here, 413x620
on a tall window. The mission picture went with it, because the two slides share
one grid cell and the view is as tall as the taller of them — leaving one at
50vh would have left it small in a box sized by its neighbour.

**The mission picture is now a circle, after vahdam.com.** Their block is
copy-left / portrait-right like Brightland's, but the portrait is ROUND with the
signature and name beside it. Measured at 1440 wide: row 1208, copy 625, and the
right-hand group 584x369 — one flat PNG with the circle (about 252px), the
script signature and three caption lines baked in. Ours is built from parts so
the picture stays an image and the words stay text: a round `.msshot`
(170–260px, `aspect-ratio:1/1`, `border-radius:50%`) with the brand mark and
caption beside it in a flex row, stacking under it on a phone. The right column
is `auto`, not a share of the width — a circle has a size of its own and should
not be stretched by its column.

**A first-click bug in the story disclosure, found and fixed.** The panel was
animated `grid-template-rows: 0fr -> 1fr`. Measured, that did not interpolate:
the row sat at 15.4px for the whole half second and then snapped to 923. `1fr`
resolves against the container's height, and a collapsed container gives it
nothing to resolve against. Replaced with a pixel height measured off the
content and set from `satva.js`, which animates because both ends are real
lengths, then handed back to `auto` so the panel still reflows.

That first fix had a worse bug in it, caught only by testing the click twice
from a cold load: the hand-back to `auto` hung off `transitionend` alone, and
where transitions do not tick, **the first click left the panel at zero while
the picture shrank — the section got SHORTER than when it was closed, and the
story never appeared.** A reader would have had to press it twice. There is now
a 600ms timer beside the `transitionend`, whichever fires first cancels the
other, so the end state never depends on the animation running at all.
Verified from a cold load: open → 917px panel, section 1244; close → 0, section
555; open again → identical. `worksOnFirstClick: true`.

**Measurement note.** rAF does not tick in this headless browser, so animation
smoothness cannot be measured here — only the end states can. Two earlier
readings in this session were artefacts of that and were wrong before they were
right; the end-state test above is the one to trust.

### 10 Sep 2026 — sweetgreen's palette, and what it cost

"This colours are very nice, incorporate these colours in my site." Read off
their live page: **sand #e8dcc6, mint #d8e5d6, off-white #f4f3e7**, ink #0e150e.

This **reverses the 5 Sep decision** to use oddbox.co.uk's warmer cream
(#fcedde). The two are not compatible — one is a warm peach, the other a
green-cast khaki — and the newer instruction wins. #fcedde comes back on request.

The part that was not a find-and-replace: **sweetgreen's grounds are darker than
the ones they replaced**, and sweetgreen can afford that because their body ink
is near-black. Ours is a mid-green. Measured before changing anything:

| | on old cream | on new sand | on new mint |
|---|---|---|---|
| `--sage` #55714e | 4.74 | **4.01** | **4.17** |
| `--gold-dk` #8a6210 | 4.77 | **4.04** | **4.20** |

Four failures below AA. Both inks were darkened by the smallest amount that
clears 4.5:1 on the darker of the two new grounds, holding hue and saturation:
`--sage` → **#4e6848** (4.56 on sand, 4.74 on mint) and `--gold-dk` → **#7f5a0f**
(4.59 / 4.77). Nothing else in the palette had to move.

Audited afterwards on the rendered page — every text node's own colour against
the real ground behind it, not against what the CSS says: **110 checked, zero
failures.** The single flag was a false positive worth recording: a ghost button
whose own background is `rgba(255,255,255,.08)` was read as an opaque white
ground. An alpha of 0.08 is not a ground; the dark band behind it is.

Section grounds now run: sand, off-white, sand, gradient, DARK, sand, mint.

### 10 Sep 2026 — Satwa Saheli takes brightland.co's lilac

The owner asked for the pale lilac of the press-logo bar on brightland.co.
Sampled off their live page rather than the screenshot: `.logo__bar_section`,
**#e2d9e3**.

This was not a one-line swap. Satwa Saheli was the **dark brand green** with
white type, pale-gold headings and an inverted ghost button — every piece of it
was designed light-on-dark and had to be turned round. Measured on the new
ground before touching anything:

| | on #e2d9e3 | |
|---|---|---|
| `--ink` #1e2c16 | 10.70 | headings |
| `--green` #2c4220 | 8.01 | body copy, the note |
| `--band` #3c5128 | 6.36 | stat labels, the unfilled slots |
| `--gold-dk` #7f5a0f | 4.53 | kick, the Devanagari, the 100% |
| `--sage` #4e6848 | **4.49** | a hundredth under AA — not used here |
| `--gold-lt` #dfb459 | **1.41** | dropped |
| white | **1.38** | dropped |

Body copy takes `--green` rather than `--sage` precisely because of that 4.49:
body text is the last place to spend a marginal ratio. The `.saheli .btn-ghost`
override was **deleted** rather than re-tuned — it existed only to invert the
shared button for a dark ground, and the shared light-ground version is now
correct again. The two placeholder tiles keep their own dark inline gradients,
so the white icons and the dark-to-transparent caption strip on them are
unchanged; only their borders went from pale gold to a dark translucent green.

Audited after: 11 text nodes in the section, zero failures; 108 across the page,
zero failures. Section grounds now run sand, off-white, sand, gradient, **lilac**,
sand, mint — no two neighbours alike.

**Flagged, not decided:** this was the only dark band in the body of the page.
The footer is now the only one, so the page carries less weight low down than it
did. If it reads too light, the green comes back on request.

### 10 Sep 2026 — the two Satwa Saheli tiles take the lilac too

The owner asked for "the small two rectangles" — the two placeholder tiles — in
the same shade. Their inline `--tint` gradients went from the old dark green
(#6f8168 → #3c5128) and brown (#b08b3a → #7d5630) to one lilac for both:
**#dbcfdc → #cbbdcd**.

A step **deeper** than the section ground (#e2d9e3), not the same colour: a
panel painted its own background's colour is not a panel. That leaves only
1.3:1 between tile and ground, which is fine here because the dashed border
carries the boundary — but it is the reason the fill is not lighter still.

Two things on the tiles were built for a dark fill and had to come with it:

- **the icons** were `#fff` at 50% — invisible on a pale tile. Now `--band` at
  40%.
- **the caption scrim**, a dark-to-transparent gradient that existed to lift
  pale gold off a dark photo tile. On the lilac it would be a dark smear across
  the bottom of an otherwise pale panel, so it is gone and the caption takes
  `--band` directly: 4.88:1 on the tile's darker stop, 5.82 on its lighter one.
  `--gold-dk` was the other candidate and only reaches 3.45 there, so it is not
  used.

**For whoever drops the real photographs in:** `.stag` now has no scrim, because
it is currently a label on a flat pale tile. The moment a real photo goes behind
it, that scrim has to come back or the caption will sit on whatever the picture
happens to be. The `.sahshot img` rule is still there and still correct.

### 10 Sep 2026 — Get in touch deleted, its mint given to the footer

"All the information in Get in touch is already there in footer." Checked before
cutting, and it is — all four cards have a twin in the footer's Reach us column:
the WhatsApp number, dssatva@gmail.com, the feedback form and the
Chhatrapati Sambhajinagar address. Nothing was lost. Markup backed up to
`REMOVED-contact-section.html`.

**`id="contact"` moved onto `<footer>`**, so the nav's CONTACT link still lands
where the contact details actually are. Zero dead anchors after.

**The footer took the deleted section's mint (#d8e5d6), and that turned it
inside out.** It was dark green with cream type, so everything had to reverse:

- the **logo** was `logo-h-cream.png` — a cream logo on a mint ground is
  invisible. Now `logo-h-dark.png`.
- links `rgba(cream,.74)` → `--green`; column headings `--gold-pale` →
  `--gold-dk`; muted text and the bottom bar → `--sage`; the rule between the
  columns from pale gold to a dark translucent green.
- the **veg mark** was `#7fbf6a`, a pale green chosen for a dark ground. The
  real mark is a dark green square and dot on a light ground, so it is `#2f7d32`.
- the **collage stays** — it is our own contact sheet and it was carrying the
  footer visually. Its overlay is now a 94–97% mint wash instead of a 90–94%
  green one. At that strength it is more a texture than a picture; if it should
  read more strongly, the wash is the number to change.

**A contrast bug fixed by accident.** `.fbrand .fnote` ("Prices are quoted per
gram…") was `rgba(cream,.68)` on the old footer and measured **3.89:1** — below
AA, and only the photograph behind it made it legible at all. There is a comment
in the CSS from an earlier pass admitting exactly that. On the mint it takes
`--sage` and measures 4.74:1.

Audited after: 22 text nodes in the footer, zero failures; **122 across the
page, zero failures**. Bands now run sand, off-white, sand, gradient, lilac,
sand, mint — no two neighbours alike. Page 4849 → 4511px. No console errors.

**Worth saying plainly:** the page now has no dark band anywhere. The Saheli
green went this morning and the footer green has gone tonight, so every band is
pale. It may read as light and airy or it may read as unanchored — that is a
judgement for the owner's eye, and both greens are one line each to restore.

### 16 Sep 2026 — four categories: Spices | Pulses | Seeds | Healthy Essentials

The owner: *"Keep everything in the site in this order Spices | Pulses | Seeds |
Healthy Essentials ... any thing else can be added later. SO only these four
categories. Alter the whole site accordingly."*

**`GROUPS` in `js/satva.js` is now that order, and it is the only place the order
is written down.** The shop-by-category cards, the header's Our Range dropdown
and the shelf counts all read it; the hero slides and the footer's range list are
written to match it. A fifth shelf goes into `GROUPS` first, never into the
markup first.

The six shelves were not thrown away, they were **folded in**:

| Was | Is now | Items |
|---|---|---|
| Ground spices, Whole spices, Blends | **Spices** | 12 |
| — (new) | **Pulses** | 2 |
| Seeds | **Seeds** | 3 |
| Pantry, Oils | **Healthy Essentials** | 6 |

Each product's `cat` still holds the *fine* shelf (`ground`, `whole`, `blend`,
`seeds`, `pantry`, `oils` became `spices` / `pulses` / `seeds` / `essentials`),
so the split can be un-folded later without retyping the range.

**Pulses had no products at all**, while the meta description, the Why-choose
list and Our Story have all promised "unpolished pulses" since the site was
written. Rather than ship a category the site talks about and cannot show, it
opens with the two dals the venture's own master list
(`~/fmcg/Household-Items-List.md`) marks ✅ *already in your plan* — **Toor Dal**
and **Chana Dal**. Moong, masoor, urad and rajma are on that list as later
additions and are deliberately not here. Neither dal has a photograph, so both
fall back to a designed tile, which is what every un-photographed product already
does. **Check the two Hindi names and the two descriptions before this goes
public** — they are the only product copy on the site not written from an
existing document.

Everything derived from `PRODUCTS` followed on its own: the announcement line now
reads 23 daily kitchen staples, and the spice spectrum rule under the hero is 23
segments.

Two things that needed a decision rather than a rename:

- **`Everything` is no longer a group.** It was `{id:"all"}` inside `GROUPS`,
  which would have made the array five entries when the owner asked for four. It
  is now a separate `ALL` constant that the dropdown prepends, so `GROUPS` is
  exactly the four shelves and the dropdown still offers a way to see the lot.
- **The category grid was `repeat(6,1fr)`.** With four cards that left Healthy
  Essentials stranded alone on a second row. It is `repeat(4,1fr)` now, 2x2 under
  1400px and a single column under 560px, so no width ends in an orphan.

The Spices headline was first written *Ground, Whole & Blended* to name all three
folded shelves. It ran to a third line where every other slide takes two, which
made the opening slide taller than the rest, so the headline is the old Ground
Spices line — *In Their Own Colour* — and the paragraph names the three shelves.

New accents, both measured rather than picked by eye: Toor `#cf8f34` with ink
`#8a5c14` (5.80:1 on white, 5.43:1 on cream), Chana `#cbab3c` with ink `#7f6a14`
(5.28:1 / 4.94:1). Both clear AA on both grounds, as every other `ink` does.

The four card tints are deliberately far apart — spice orange, dal sand, seed
green, salt rose — because three of the four shelves are otherwise yellow and the
cards read as one block.

Verified in the browser at 1600 / 1440 / 1280 / 1024 / 390px: tabs, cards,
dropdown, footer and counts all read Spices 12, Pulses 2, Seeds 3, Healthy
Essentials 6 in that order; 12+2+3+6 = 23 = `PRODUCTS.length`; every headline two
lines; no dead anchors; no horizontal overflow; zero console errors.

**Not touched, on purpose:** the "How it is made" flip cards still have their own
six process cards (chilli, turmeric, coriander, seeds, oils, salt). They are
processes, not categories — they are not a second navigation and do not claim to
be the range.

### 16 Sep 2026 — one card, one frame

The owner, with a screenshot of the category block: *"Fix this content to the
page and design it so that these things are in one frame and one block."*

**What was wrong.** Only the photograph was framed. `.cshot` carried the radius
and the shadow; the blurb and the ITEMS line sat *below* it on the section's bare
sand, outside any border. With six small cards that passed, but at four cards on
a 1280–1400px laptop the grid dropped to two columns, each card came out ~830px
wide and ~550px tall, and the two lines of text were stranded a long way under
their own picture. The four shelves then needed two screens.

**The frame.** `.catcard` is now the frame — white ground, one `--line` border,
one 20px radius, `overflow:hidden`, one shadow — and the picture and the words
live inside it. `.cshot` gave up its own radius and shadow, because doubling them
drew a visible seam across the middle of the card. The whole card lifts and takes
a gold border on hover, instead of the photograph sliding out from under its own
caption.

Side effect worth having: the blurb and count moved from sand onto white, so
their contrast went **4.7:1 → 6.18:1** and **4.9:1 → 6.23:1**.

**The block.** Four across now holds down to **1080px** instead of 1400px. At
1290px that is four 268px cards on one row, the section 346px tall — the whole
range readable without scrolling. Below 1080 it is 2x2, below 560 a single
column.

### 16 Sep 2026 — a horizontal scrollbar that was there all along

Found while measuring the above at 1081px: **the whole page scrolled sideways by
54px between about 1081px and 1224px wide.** Not the category cards — hiding that
grid entirely changed nothing. It was the "Why choose SATVA" circles.

A `.reason` circle's min-content width is its longest word (*Nutrient-preserved*)
plus 15% padding each side, about 254px, and a `1fr` track cannot shrink below
its min-content. At 1081px that made four tracks 258px each — 1131px of track and
gap inside a 980px container, so the fourth circle hung 54px off the right edge
and took the document's scroll width with it.

The 4→2 breakpoint moved from 1080px to **1240px**, which is where four of those
tracks plus three 3vw gaps actually stop fitting. Four circles still show at
1240px and above; a 1100px window now gets 2x2 rather than a sideways scroll.

This one was **not** caused by the category work and is **not** part of what was
asked for — it is a pre-existing bug, fixed because it was found. If four circles
are wanted back down at 1100px, put the breakpoint back and shorten the headings
instead; the words are what set the floor.

Checked after both: 1600 / 1440 / 1290 / 1200 / 1100 / 1081 / 1024 / 900 / 768 /
560 / 390px — zero horizontal overflow at every one, cards 4 / 2x2 / 1, no
console errors.

### 16 Sep 2026 — long rectangles, and the shelves take a whole screen

The owner: *"Make these pictures rectangular so that the screen has only that
block and what we dont do goes for the next scrolling"* — then, on the shape:
*"long rectangle"*.

**The picture is sized in `svh`, not by an aspect ratio.** An aspect ratio ties
the picture's height to the card's own width, and the card's width is set by how
many columns fit — which has nothing to do with whether the block fills a screen.
Since the whole point was to fill the screen, the height answers to the window:
`clamp(280px, 56svh, 520px)`. At 1290x860 that is a **266x482 picture — a 3:5
rectangle**. The 280px floor keeps it sane on a short laptop window; the 520px
ceiling stops it stretching into a sliver on a tall monitor.

`svh` rather than `vh` so a phone's collapsing toolbars cannot make the block
taller than the screen it is meant to fit; a plain `vh` line sits above it for
anything that does not know `svh`.

**`.cats` is `min-height:100svh`,** a centred flex column, so the shelves hold
one screen on their own and "What we will not do to your food" starts below the
fold. Measured at 1290x860: section exactly 860px, the next section's top at
exactly 860 — **0px of it visible**. `min-height`, not `height`, because at two
columns or stacked on a phone four cards are legitimately taller than a screen
and the section has to be allowed to grow.

Portrait was rejected once before, and the old comment saying so is still worth
reading: with SIX cards in two rows, a tall first row pushed the second row off
the screen. Four cards on one row is what makes tall pictures possible now.

Two things this broke, both found by measuring rather than by eye:

- **The heading slid under the sticky nav.** With the content centred in exactly
  one screen, a short window (1366x660) left the "SOMETHING FOR EVERY SHELF" line
  at y=83 against a nav 81px deep — a 2px escape, and a shorter window would have
  swallowed it. `.cats` now takes `padding-top:max(96px, ...)`, in the base rule
  and again inside the `max-height:1000px` block which was overriding it. The
  clearance is 82px at 1290x860 and 68px at 1366x660.
- **The cards got narrower on a phone.** `.wrap` carries `margin:0 auto`, and an
  auto margin on the cross axis switches OFF a flex item's stretch - so the
  moment `.cats` became a flex column the wrap fell back to fit-content and the
  single mobile card came out **282px wide inside a 367px wrap**. `.cats .wrap`
  now has `width:100%`; the card is 331px again.

Two columns and one column get shorter pictures — `38svh` and `34svh`, capped at
380px and 330px — because four rows of a 56svh picture would be a very long
scroll for the same four shelves.

Checked at 1600x900, 1440x900, 1366x660, 1290x860, 1200x800, 1100, 1081, 1024,
900x800, 390x844: no horizontal overflow anywhere, the heading clears the nav at
every one, and where four cards sit on a single row the next section is exactly
off-screen. No console errors.

### 16 Sep 2026 — the four circles become four arches

The owner, on the "What we will not do to your food" circles: *"try this in some
other shape so that i see a uniqueness when compare to the other wesite flow and
fit in to the screen as one block."*

**The shape is an arch** — a dome over straight sides on a flat foot:

```css
--r:22px;                                                  /* the flat foot */
border-radius:50% 50% var(--r) var(--r) / 44% 44% var(--r) var(--r);
```

Four of them side by side read as a colonnade — a shopfront, or the niches in a
temple wall. A row of pastel circles and a row of rounded cards are both things
every other food site has; this is not, and it belongs to this brand rather than
to a template.

**It is also what makes the block fit a screen.** A circle can only hold type
inside its inscribed square, roughly 70% of its width, which is why it needed
15% padding on all four sides — and that padding is what pushed its minimum width
to ~254px and made four circles overflow the page between 1081px and 1224px
(logged this morning; the fix then was to give up and switch to two columns at
1240px). An arch is straight-sided exactly where the words are, so the padding is
~26px instead of a seventh of the width, and the same copy now sits in a **216px
arch at 1001px wide**. So four across is back, down to 1000px, verified by
measurement at 1001px and 1024px rather than by eye — that is how the original
bug got in.

`.reasons` is `min-height:100svh`, a centred flex column, with the same
`padding-top:max(96px, ...)` nav clearance and the same `width:100%` on its
`.wrap` that the shelves block needed. At 1290x860 the section is exactly 860px
and the next block shows **0px**.

Two passes on the proportion, both worth recording because the first looked
wrong for a reason that is easy to repeat:

- **48svh (a 413px arch) with the content centred** left a third of each panel as
  dead colour at the foot — the group of icon + title + copy is only ~194px.
- **`justify-content:space-evenly`** was the obvious way to use that depth up,
  and it was worse: it pushed the copy ~50px clear of the title it belongs to, so
  each panel read as three floating things instead of one statement.
- **What worked: a shallower arch, 40svh capped at 380px, content still
  centred.** The section is `min-height:100svh` regardless, so the leftover
  height goes into the ivory above and below the colonnade, where it reads as
  air, instead of into the bottom of four coloured panels, where it read as a
  mistake.

Widths: four across above 1000px; 821–1000px is two across, and that band gets
its own width cap (`clamp(240px,34vw,320px)`) because the four-across cap of 23vw
left a 210px arch adrift in a 400px track. **That override is written as
`.reasons .reason` and banded off `<=820px` on purpose** — the base `.reason`
rule sits later in this file, a media query adds no specificity, and an
equal-specificity override up at the grid rules simply loses. The one-per-row
rule at the foot of the file still owns `<=820px`, where the arch is 330px wide.

Nothing about the colours changed: the four panels keep the Huel/sleepyowl
sampling and their darkened line art, so the contrast audit from 10 Sep stands.

Measured at 1600x900, 1366x660, 1290x860, 1024x820, 1001x800, 900x800 and
390x844: four/two/one across as intended, no copy overflowing any panel, all four
titles on one baseline, the heading clear of the nav at every one (157px at
1600x900 down to 55px at 1366x660), no horizontal overflow, no console errors.

### 17 Sep 2026 — "How we make" is four cards, one per shelf

The owner: *"Keep the design same, but here also only spices pulses seeds and
healthy essentials should only be there"* — and, with a screenshot of this
carousel, *"IN these cards sliding, have only those categories."*

The design is untouched: same coverflow, same flip, same video front and
photograph back, same tab strip. Only what the cards ARE has changed.

Six cards named after products and processes — Chilli Powder, Turmeric,
Coriander Powder, Seeds, Cold-Pressed Oils, Pink Salt — became the four shelves
in `GROUPS` order, so the site names its range once instead of offering a second,
competing list of it:

| Card | Film | Back |
|---|---|---|
| Spices | `proc-turmeric.mp4` — turmeric on the grinding stone | `cat-spices.jpg` |
| Pulses | **none yet** | `cat-pulses.jpg` |
| Seeds | `proc-seeds.mp4` | `cat-seeds.jpg` |
| Healthy Essentials | `proc-oil.mp4` — the press | `cat-essentials.jpg` |

**`film` is now a separate field from `id`.** The id is the shelf; the film is
named for what the footage actually shows. The Spices card plays turmeric being
ground, and calling that file `proc-spices.mp4` would have invited the next
person to believe a "spices" clip exists. `film:null` means no footage, and
`still` is the photograph shown instead — the card then renders with **no
`<source>` at all**, so nothing requests an mp4 that was never shot, and
`mPaint()` already wrapped `play()` in a `.catch()`, so the card just sits on its
still. Verified: zero console errors, zero failed requests.

**Pulses is the weak card and should be fixed first.** It has one photograph and
no film, so it shows the same still on both faces and only its words change on
the turn. The page says so out loud - the note under the carousel now reads
"...Pulses has no film yet at all."

**A four-card coverflow needed one CSS rule.** Position comes from `--d`, the
signed distance from centre, and with an EVEN number of cards the one opposite
the centre has no mirror. At six it landed at `--abs: 3` and was already hidden;
at four it lands at `--abs: 2` and hung on the right on its own with nothing at
-2 to answer it. `js/satva.js` now writes the card count onto `.mkrow`, and the
stylesheet hides `--abs: 2` at `[data-count="4"]` — left, centre, right, and the
fourth rotates in. Measured with Spices centred: 354px / 638px / 921px against a
stage midpoint of 638px, and the fourth card at opacity 0.

`proc-chilli`, `proc-dhaniya` and `proc-salt` (and their posters) are now unused
but kept: salt is the obvious second film for Healthy Essentials, and the chilli
and coriander clips return if Spices is ever split again. `p-mirchi.jpg`,
`p-haldi.jpg` and `p-dhane.jpg` left this block but are still each product's own
photo in `PRODUCTS`, so nothing is orphaned.

The tab strip's `aria-label` went from "Choose a spice" to "Choose a shelf".

Checked at 1290x860 and 390x844: four tabs, four cards, the strip fits without
wrapping, three cards visible and symmetrical, the flip shows the right back
face, no horizontal overflow, no console errors.

### 17 Sep 2026 — Satwa Saheli takes the pink salt wash

Chosen off a comparison page built for the purpose, which previewed 26 grounds as
the real full-width edge rather than as swatches. The owner picked **Pink salt
wash `#f3dfdc`** — a pale step of `--himalayan #d98a8a`, the unrefined salt
already in the range, and the only candidate that names a product we sell.

**What was actually wrong with the lilac.** Not the colour — its position. This
band's upper neighbour is the mission band's mint, and `#e2d9e3` sat only +0.042
from it in lightness while being cool, like it. No warmth change, no step, so the
boundary did not announce itself and the section read as a continuation of the
one above. The salt wash is **+0.099 lighter and a 101° hue turn** from that
mint: the edge now reads twice over.

**Nothing else had to move, because every ink got better:**

| | on the lilac | on the salt wash |
|---|---|---|
| `--ink` headline | 10.70:1 | **11.49:1** |
| `--green` body | 8.01:1 | **8.60:1** |
| `--band` labels | 6.36:1 | **6.83:1** |
| `--gold-dk` kick, Marathi, numerals | 4.53:1 | **4.86:1** |

`--sage` is the interesting one: it measured 4.49:1 on the lilac, a hundredth
short of AA, which is why body copy was moved to `--green` in the first place. On
this ground it reaches 4.83 and would now be legal — but `--green` measures 8.60,
so it stays. White (1.38) and `--gold-lt` (1.41) remain unusable here.

**Two values, in two files.** The ground is in `css/satva.css`; the placeholder
panels' tint is inline in `index.html`, at the same 0.96x / 0.89x steps the lilac
pair used: `#dbcfdc → #cbbdcd` became **`#e9d6d3 → #d8c6c4`**. They have to be
changed together or they drift, and there is now a comment in the CSS saying so.
`--band` on the tile's darker stop — the "PORTRAIT TO COME" caption — improved
from 4.88:1 to **5.33:1**.

**Correction to what was said while choosing this.** The comparison page was
built on the belief that this band sits between two mints. It does not: the block
below it is **`.recipes`, which computes to the sand `#e8dcc6`** — the footer's
mint is three blocks further down, past the recipes and the spectrum rule. The
upper edge, which is the one the owner screenshotted and asked about, is
unaffected by the mistake. The lower edge is:

- against the sand below, the salt wash is +0.046 in lightness but only a **31°
  hue turn** — both warm, both pale. The lilac's lower edge was carried entirely
  by hue (255°) and almost not at all by lightness (-0.011).

So this change strengthens the edge that was asked about and softens the one
below it. At +0.046 the lower boundary is still a visible step, and the recipes
band opens with its own heading and photographs, so it does not read as one
continuous field — but if it ever should, the fix is to push the salt wash a
shade pinker and deeper, away from the sand's yellow, rather than to touch the
recipes band.

Verified live: ground `rgb(243,223,220)`, both tiles carrying the new tint, all
seven pieces of type measured in the browser at the figures above, no console
errors.

### 18 Sep 2026 — the footer goes plum grey

Chosen off a page of eighteen warm charcoals previewed against the sand band that
arrives above the footer. The owner picked **plum grey `#372e35`** — a warm
charcoal with a trace of violet, which also keeps that violet somewhere on the
page now that Satwa Saheli has gone to the salt wash.

**This answers a question the 10 Sep entry left open.** That pass ended: *"the
page now has no dark band anywhere ... it may read as light and airy or it may
read as unanchored — that is a judgement for the owner's eye."* The judgement is
in. The page has weight low down again.

**It is the 10 September inversion run backwards.** Every ink here was flipped
for a light ground in September and had to flip again:

| | was (on mint) | is (on plum) | measured |
|---|---|---|---|
| logo | `logo-h-dark.png` | `logo-h-cream.png` | — |
| blurb + links | `--green` | `--cream` | 9.65:1 |
| column headings, bottom Devanagari | `--gold-dk` | `--gold-pale` | 9.77:1 |
| fnote, address, bottom bar | `--sage` | `--f-muted #c9bda4` | 7.04:1 |
| veg mark | `#2f7d32` | `#7fbf6a` | 5.96:1 |
| link hover | `--gold-dk` | `--gold-lt` | 6.74:1 |
| column rule | `rgba(30,44,22,.16)` | `rgba(255,255,255,.18)` | — |

None of the old values survive on this ground: `--green` 1.19:1, `--sage` 2.12,
`--gold-dk` 2.10, the dark veg mark 2.56.

**The muted text is a solid, and must stay one.** The original dark footer set
`.fnote` to `rgba(cream,.68)`, which measured **3.89:1** and was only legible
because of the photograph behind it; the mint fixed that by accident in
September. It is now `--f-muted`, a solid `#c9bda4` at 7.04:1, declared once on
`footer` so the fnote, the address line and the bottom bar cannot drift apart
again. **Do not put the alpha back.**

Collage wash is **92–95%**, between the 90–94% this footer used when it was dark
green and the 94–97% the mint used. That pair is the dial — lower shows more
photograph, higher more flat colour.

Verified live: ground `rgb(55,46,53)`, cream logo loading, and all seven type
roles measured in the browser at the figures above. No console errors.

**Not applied, for the owner to decide:** a preview of the STACKED logo (the DS
above the wordmark rather than beside it). The artwork already exists as
`logo-stack-cream.png` / `logo-stack-dark.png` (760x722), so nothing needs
drawing. The only real decision is size: the stacked file is ratio 1.05 against
the horizontal lockup's 3.27, so at the footer's current 52px it shrinks to about
a third of the width and reads as a stamp; it wants 88–112px, which makes the
brand column taller than the three link columns beside it. In the sticky nav it
costs more — a square mark drives the header deeper on every screen — so that is
worth deciding separately from the footer.

### 18 Sep 2026 — the footer takes the stacked logo

`logo-h-cream.png` → **`logo-stack-cream.png`** in the footer: the DS monogram now
sits ABOVE the wordmark rather than beside it, with "Dil Se Pure" and the wheat
sprigs beneath. No artwork was made — that file already existed at 760x722.

**The decision was the size, not the arrangement.** The horizontal lockup is
ratio 3.27 and 52px suited it. The stacked file is all but square at 1.05, so at
52px it came out roughly a third of the width and read as a stamp. It is now
`clamp(84px, 9vw, 112px)`:

- **112px** on a desktop, rendering 118x112. The brand column and the link
  columns both measure 289px, so the grid stays level rather than the logo
  dragging one column out of line.
- **84px floor**, because below about that the strapline inside the artwork stops
  being readable at all. On a 390px phone it lands at 88x84 with no overflow.

**The nav still carries the horizontal lockup, on purpose.** A square mark in a
sticky header drives that header deeper on every screen and pushes the block
below it down - a different trade from the footer, where there is room. Samples
06 and 07 on the preview page show what it would cost; that decision is still
open.

Verified at 1290x860 and 390x844: logo loading, columns level, no horizontal
overflow, no console errors.

### 18 Sep 2026 — the stacked logo, everywhere

*"I want the logo to be changed in the whole site."* All three instances now
carry the stacked lockup — DS above the wordmark, not beside it:

| Where | File | Height | Rendered |
|---|---|---|---|
| sticky nav | `logo-stack-dark.png` | **76px** | 80x76 |
| mission signature | `logo-stack-dark.png` | `clamp(46px,6vh,66px)` | 54x52 |
| footer | `logo-stack-cream.png` | `clamp(84px,9vw,112px)` | 118x112 |

**The nav height is 76px because it was measured, not chosen.** The bar's depth
is set by its own padding and the WhatsApp button, not by the logo, so there was
free headroom above the old 50px. Trialled in the browser: the bar stays exactly
**81px deep at 62, 68, 72 and 76**, and only grows at 82 (83px) and 88 (89px).
76 is therefore the largest this mark can be for nothing — a 23% bigger logo than
the 62px I first set, with the header, the full-screen blocks' nav clearance and
everything below it untouched.

That clearance was the thing to watch: `.cats` and `.reasons` are `100svh` blocks
whose headings are held off the sticky nav by `padding-top:max(96px,...)`. Had
the bar grown, that number would have had to grow with it. It did not, and the
measured clearances are unchanged at 108px and 148px.

The mission signature's cap went from 42px to 66px for the same reason as the
footer's: a square mark at the old height was 44px wide and read as a speck
beside the caption. Its `width`/`height` attributes were corrected to 760x722 to
match the new file, so the layout reserves the right box before it loads.

Checked at 1290x860 and 390x844: all three loading, the bar still 81px, the logo
clear of the burger by 216px on a phone, no horizontal overflow, no console
errors.

### 18 Sep 2026 — "Cook something for someone" takes the mission's mint

*"Keep this same background for cook for someone also - green shade."* The
recipes block was the sand `#e8dcc6`; it now carries the mission band's own
ground — the same two mint stops on the same 160deg — so the two green blocks on
the page are green in the same way rather than approximately.

**The static pair, not the live one.** The mission mixes those stops against
cream through a `--mx` property as you scroll; that is the colour-shifting ground
the owner asked for in September. Copying the shift as well would have put two
grounds changing under the reader at once, so this is where that gradient
settles.

**Two rules were fighting over this ground.** There were two `.recipes` blocks in
this file at equal specificity, both setting a background — the later silently
won while the earlier one sat there looking authoritative, carrying a comment
about sage that had not been true for some time. The ground is declared once now;
the earlier rule keeps only layout and says so.

**A contrast bug the change exposed.** The block's lede was `--sage`, which was
fine on the flat sand. On a GRADIENT a colour has to clear AA at *both* stops,
and `--sage` only managed the lighter one — **4.74:1 on `#d8e5d6` but 4.24 on
`#c9dbc5`**. It is `--band` now: 6.71 / 6.01. (`--sage-soft` would have been
worse still, 3.71 / 3.32. The palette note at the top of this file already says
to prefer `--sage` over `--sage-soft` on a sage-mist ground; on the deeper stop
of the gradient even `--sage` is not enough, which is worth knowing the next time
a block takes this ground.) Both copies of the `.rechead .lede` rule were changed
together so they cannot drift.

Everything else on the block was already safe at both stops: heading and card
titles 11.28 / 10.11, the ghost button 8.44 / 7.56, and the four "MADE WITH"
labels 14.40, since those already mix their product accent toward the ink — a fix
put in when this block last sat on a sage ground.

The run of bands now reads **mint · salt wash · mint · plum**, with no two
neighbours alike. Verified at 1290x860: no horizontal overflow, no console errors.
