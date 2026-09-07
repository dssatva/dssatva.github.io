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

The "Photo coming" pill was removed from the cards: with 16 of 21 products still
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

14 of the 21 products, after two were sourced on 3 Sep 2026 (see below).

| Product | Save the photo as | Group |
|---|---|---|
| Kanda Lasun Masala | `assets/p-kandalasun.jpg` | blend |
| Meat Masala | `assets/p-meat.jpg` | blend |
| Chaat Masala | `assets/p-chaat.jpg` | blend |
| Chatpat Masala | `assets/p-chatpat.jpg` | blend |
| Cumin Seeds | `assets/p-jeera.jpg` | whole spice |
| Mustard Seeds | `assets/p-rai.jpg` | whole spice |
| Fenugreek Seeds | `assets/p-methi.jpg` | whole spice |
| Chia Seeds | `assets/p-chia.jpg` | seeds |
| Himalayan Pink Salt | `assets/p-pinksalt.jpg` | pantry |
| Unprocessed Sugar | `assets/p-khandsari.jpg` | pantry |
| Groundnut Oil | `assets/p-groundnutoil.jpg` | oils |
| Sesame Oil | `assets/p-sesameoil.jpg` | oils |
| Mustard Oil | `assets/p-mustardoil.jpg` | oils |
| Coconut Oil | `assets/p-coconutoil.jpg` | oils |

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
