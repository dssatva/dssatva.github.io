# DS SATVA — variant C, the dark hero

Two pages, identical except for **one line**, so the comparison is the photograph
and nothing else:

| | |
|---|---|
| **B1** — the spice box we already own | `index.html` → http://127.0.0.1:8003/ |
| **A3** — chilli and garlic on slate (CC0) | `a3.html` → http://127.0.0.1:8003/a3.html |

Served by this folder's `serve.py` on **:8003**. Variant A (`../site`, :8000) and
variant B (`../site-v2`, :8002) are untouched.

## The whole change is one stylesheet

`css/hero-dark.css`, loaded after `satva.css`. Delete that one `<link>` and the
page is variant A again. `satva.css` had already predicted this file: the note
above `.sh-shot img` reads *"A photo shot on a dark ground would need its own
handling."* Three things happen in it:

1. **The photograph goes full-bleed.** The inset right-hand frame and its taper
   exist to dissolve a PALE photo into cream. On a dark photo there is nothing to
   dissolve into and the taper only ate the picture.
2. **A scrim carries the type** — α .80 where the copy sits, dying to nothing by
   88% so the right end of the photograph is at full strength.
3. **Every ink inverts**, the same exercise the footer went through on 18 Sep.

**Measured:** cream `#e8dcc6` over `rgba(10,13,9,.80)` against the worst case — a
white blowout in the photograph — is **6.8:1**. The floor for cream over any
photograph is α 0.68, so .80 carries margin. **`--gold-lt` is unusable on a dark
hero at any sane scrim strength** (3.4:1 at α .70), so the accent is
`--gold-pale`. That is why "Own Colour" reads pale gold here and metallic gold
everywhere else.

## All four shelves

| Shelf | Picture | Kind |
|---|---|---|
| Spices | `cat-blend.jpg` (B1) / `hero-dark-slate.jpg` (A3) | dark studio |
| Pulses | `hero-pulses-toor-plant.jpg` | the crop, growing |
| Seeds | `hero-seeds-flax-plant.jpg` | the crop, in flower |
| Healthy Essentials | `hero-essentials-coconut-plant.jpg` | the crop, growing |

**19 Sep, second pass.** The three non-spice slides were first built as a duotone
over the pale studio shots, because no dark studio photograph of dal or of oil
exists under any usable licence — CC0 first, then every commercial licence
Openverse indexes, about twenty-five queries, which returned coffee beans, a
bulldog on a bean bag and a salt pond in New Zealand.

The owner's answer was better than the workaround: *"it would be good to have
green pictures related to what plants they are."* So the disguise is gone and
each of the three carries its own crop in the ground instead. Spices keeps the
dark studio shot, which is the one that was approved.

**Why a black spice box and three green fields still read as one hero:** the
left-hand scrim. It darkens the third of the picture the type sits on and leaves
the rest at full strength, so the difference between the two kinds of photograph
lands on the right-hand side, where it looks like variety rather than
inconsistency. Cream on that scrim against the worst case — a white blowout in a
sunlit field — is still 6.8:1, so the bright pictures needed no extra handling.

The plant shots take no grade beyond a light `saturate(1.12)`. The duotone and
the `graded` / `graded-soft` rules are gone from the markup; the CSS keeps them,
commented, in case a pale studio shot is ever needed in this hero again.

## What this variant is still short of

- **Three of the four fields are not ours.** The crops are real and correctly
  matched — pigeon pea is genuinely toor, flax is genuinely the javas plant — but
  they were photographed somewhere else, and a crop in a hero implies it is your
  land. The sourcing block still says "Region to be named" for this reason.
- **Seeds is flax, and flax alone.** No usable picture of a chia or quinoa plant
  exists in the free pool, so the slide shows one of the three seeds it names.
- The shot list, if they are: one subject, black paper, light from the SIDE,
  phone at minimum focus distance, underexposed so the black stays black. Two
  photographs — a handful of toor on black, and oil pouring — would replace both
  duotones and cost nothing but an afternoon.

### 20 Sep 2026 — the range, as the owner set it

Twelve spices, two pulses, four seeds, three essentials — **21 items**.

| Shelf | Items |
|---|---|
| Spices (12) | Haldi, Mirchi, Coriander (whole), Mustard, Jeera, Black Pepper, Coriander Powder, Garam Masala, Biryani Masala, Meat Masala, Sambar Masala, Chatpat |
| Pulses (2) | Toor Dal, Chana |
| Seeds (4) | Chia, Flax, Quinoa, Methi |
| Healthy Essentials (3) | Pink Salt, Coconut Sugar, Monk Fruit Sugar |

**This was not a relabelling.** Three things left or moved, and copy all over the
page had been written around them:

- **Methi moved from Spices to Seeds.** It was "Fenugreek Seeds", a whole spice
  for the tadka; it is a seed on the Seeds shelf now.
- **The four cold-pressed oils are gone** — groundnut, sesame, mustard, coconut.
  Healthy Essentials went from six items to three.
- **Khandsari is gone too**, replaced by coconut sugar and monk fruit.
- Kanda Lasun Masala and Chaat Masala also left the spice list; Coriander Seeds,
  Black Pepper and Sambar Masala joined it.

**What had to change besides the list:**

- **The Healthy Essentials headline.** It read *"Pressed, Not Refined"*, which
  described the oils. Nothing on that shelf is pressed now. It takes the old
  Pantry slide's line, *"Unrefined, Unbleached"* — which also avoids a third
  "Nothing …" after Pulses and Seeds. Still two lines, like the other three.
- **That slide's paragraph** was rewritten rather than trimmed: almost every noun
  in it had gone with the oils.
- **Its arch** was a bottle of oil; it is the pink salt now. **The coconut grove
  behind it stays** and still earns its place — coconut sugar is the sap of that
  palm, so the picture now stands for the sweetener instead of the oil.
- **The "How it is made" card** for this shelf played the oil press. `proc-salt.mp4`
  was the unused film in that set and is the right one now.
- **The Spices paragraph** listed fenugreek among the whole spices; it lists
  coriander, cumin, mustard and black pepper. **The Seeds paragraph** gained methi.
- **Three recipes pointed at products nobody can now buy.** Bhel moved from Chaat
  to Chatpat Masala. Methi Dal Tadka follows methi to its new name. Kanda Lasun
  Zunka was built entirely on Kanda Lasun Masala, so rather than aim a recipe at
  a discontinued product the card became **Sambar** — which also gives Sambar
  Masala, a new product, a recipe of its own. Checked afterwards: all 14 `uses`
  references resolve to something in the range.

Everything derived from `PRODUCTS` followed on its own — the shelf counts read
12 / 2 / 4 / 3, the dropdown totals 21, the ticker says 21, and the spice
spectrum under the hero is 21 segments.

**Two things to confirm before any label is printed:**

1. **"Chana", not "Chana Dal".** The description is written for the SPLIT dal. If
   the product is whole chana, that line needs changing and so does the Pulses
   hero copy, which says "the two dals this kitchen cooks most".
2. **Monk fruit is a sweetener, not a sugar.** "Monk Fruit Sugar" is the owner's
   wording and is kept, but Indian labelling rules are strict about the word
   sugar — the same caution that sat on khandsari before it.

**Photography still missing** for the new items: Coriander Seeds, Black Pepper,
Sambar Masala, Coconut Sugar, Monk Fruit Sugar. All five fall back to their
designed tile, as every un-photographed product does.

**Variant A on :8000 still carries the OLD range** — twelve spices including
fenugreek and chaat, and six essentials with the four oils. It was frozen at the
owner's request, so the two sites now disagree about what is for sale.

### 20 Sep 2026 — the range listing is back

The owner, looking at the four category cards: *"So where have you added these?
When I click these cards, it should turn to display all those items."*

**They were nowhere.** The listing was deleted on 10 September and the category
cards were rewired to open WhatsApp, so the site was counting 21 products in four
separate places — the cards, the dropdown, the shelf slides, the ticker — and
showing them in none. Clicking a card that says "12 items" opened a chat window.

**Almost nothing had to be built.** Every style the listing needs survived the
deletion untouched: `.range`, `.sechead`, `.grid-p`, `.pcard`, `.pthumb` with its
designed tile and Devanagari glyph, `.pbody`, the `GROUND`/`WHOLE` pill, the veg
mark, the tab strip with its counts. Only the markup and the render function had
gone, so this is those two coming back — `<section class="range" id="range">` and
a renderer driven entirely by `PRODUCTS` and `GROUPS`.

**One way in, three doors.** The category cards, the hero pills ("See all
spices") and the Our Range dropdown all now call the same `goToShelf(id)` — filter
the grid, scroll to it. Previously all three opened WhatsApp. There are now zero
"tell me about your …" fallbacks left in the file.

**A photograph flag, because probing cost 404s.** The original design tried
`img` for every product and fell back to the tile if the file was missing, so
"adding a photo later" was just dropping a file in. That convenience cost
**thirteen 404s on every page load** once the range grew to 21 items, 13 of them
un-photographed. Products now carry `photo:true` when a file really exists, and
the probe only runs for those. The `img` path stays on every product as
documentation of where the photograph belongs. To add one: save it at that path
and add `photo:true` to the same line.

Verified: 21 cards on Everything, 8 with photographs and 13 with tiles; clicking
the Pulses card filters to Toor Dal and Chana Dal, selects the Pulses tab and
reads "2 items on the Pulses shelf"; no console errors.

---

## Field to plate — the turmeric journey (20 Sep 2026)

The owner asked for **"a stunning video of how this turmeric powder is got from
the actual plant … from the beginning till the end … whoever enters the website
will also learn how the product is got from the field to the plate."**

### The video does not exist under a licence we can use

Searched Wikimedia Commons (`filetype:video`, eight query sets) and the
Openverse API (CC0 / PDM / BY / BY-SA, commercial-use filter, eight query sets).
The **entire** free-licence pool holds two turmeric clips:

| Clip | Licence | Verdict |
|---|---|---|
| `Rotating grinding disc grinding turmeric powder.webm` | CC BY 4.0 | **Rejected — mislabelled.** Downloaded and watched it: the footage is a Chinese market stall grinding Yunnan yellow *ginger*. The price board reads 云南小黄姜面 10元/4两. Wrong spice, wrong country, and a cluttered stall that would have looked cheap beside everything else on this page. |
| `Sprinkling Turmeric for Lord Khandoba.webm` | CC0 | Religious use, not processing. |

Everything else the queries returned was weddings, temple ritual, or unrelated
plants. There is **no full-journey turmeric film** available to us. Openverse
added nothing Commons did not already have.

### What was built instead

The real six-stage process, one stage per screen, in licensed photographs, with
motion where we genuinely have footage. It teaches the process *better* than one
film would, because each stage carries its own caption and its own elapsed time,
and every frame is cleared for commercial use.

Every timing is from the agricultural literature, not invented — 7–9 months in
the ground, boiling 40–60 minutes, sun-drying 10–15 days:

| # | Stage | Asset | Licence |
|---|---|---|---|
| — | intro | `j-turmeric-1-field.jpg` | CC0 |
| 01 | It grows as a root, not a spice | `j-turmeric-1-field.jpg` | CC0 |
| 02 | Lifted, washed, and split | `j-turmeric-2-lifted.jpg` | CC BY-SA 4.0, Liat Portal |
| 03 | Boiled, within two days of lifting | `j-turmeric-3-cured.jpg` | CC BY-SA 3.0 |
| 04 | Dried in the sun, turned every day | `j-turmeric-4-drying.jpg` | CC BY-SA 4.0 |
| 05 | Rubbed smooth — and nothing added | `j-turmeric-5-polished.jpg` | CC BY-SA 4.0 |
| 06 | Ground slowly, so it keeps its oils | **`proc-turmeric.mp4`** (video) | Pexels, free commercially |
| — | And that is what is in the packet | `j-turmeric-6-ground.jpg` | CC BY 2.0 |

Stage 06 reuses the clip the "how it is made" carousel already plays — real
turmeric on a stone grinder. It is the only turmeric footage on this site that
is both licensed and actually turmeric.

Every CC BY / BY-SA credit renders on its own stage, bottom right, linked to the
source file. That is the attribution the licences require; it is not optional.

### How it is wired

- `css/journey.css` — the whole feature. Delete the `<link>` and the feature goes.
- `js/satva.js` — a `JOURNEYS` object keyed by the product's English name, plus
  `openJourney()` / `closeJourney()`. **To add the next product, add one entry.**
  The "See how it is made" button appears on that card by itself; a product with
  no entry gets no button, so a button never opens an empty panel.
- The trigger is delegated off `#pgrid`, so it survives every re-render when the
  shelf filter changes.

### Decisions worth knowing

**An overlay, not a page.** Sending someone to `/turmeric.html` and back loses
their place in the grid and their shelf filter. This opens over the grid and
closes back exactly where they were.

**Scroll-snap, not a carousel.** The point is that this is a sequence with a
direction. A carousel lets you arrive at stage 5 first; snapping down a single
column makes the order unskippable, which is the whole teaching job.

**The body is pinned, not `overflow:hidden`.** `scrollIntoView()` walks every
scrollable ancestor and an overflow-hidden body still counts as one, so each
snap quietly dragged the page underneath — measured, the grid ended up 1137px
from where it was opened. `position:fixed; top:-Ypx` removes the second scroll
container, and Y is what we scroll back to. Verified: opens at 873, closes at 873.

**Only the stage in view decodes its video.** Several clips decoding at once is
what makes this kind of page stutter.

**The panel is removed from the DOM on close**, not hidden — six full-screen
photographs and a video element parked in memory is not worth it for a panel
most visitors open once. Rebuilding is instant from cache.

### Contrast, measured

Worst case is cream type over the brightest photograph in the set (the leaves).

| Ink | Before | After | Fix |
|---|---|---|---|
| body copy `rgba(244,243,231,.9)` | **4.24:1** ✗ | 5.09:1 | intro/end get their own ramp with a .58 floor; ink to .94 |
| stage number, gold-lt at 50% | **2.00:1** ✗ | 3.50:1 | opacity to .78 (large text, 3:1 floor) |
| credit line, cream at 50% | **4.29:1** ✗ | 5.74:1 | opacity to .64 |
| closing card, cream over powder | 6.18:1 ✓ | — | — |

The copy-band stop went from `.62` to `.70` to buy the headroom.

### Checked

1290×860 and 390×844, `index.html` and `a3.html`: eight stages, rail tracks one
dot per stage, video plays only in view, Escape closes, focus returns to the
button, DOM cleaned, body unlocked, scroll restored to the pixel, no horizontal
overflow, **zero console errors or warnings**.

### Open

- **Stage 03 is illustrative, not literal.** No photograph of turmeric being
  boiled exists in the free pool — none. The image shows a cut root with its
  orange face and the powder beside it, which is what the boil *is about*; the
  caption never claims to show a boiling pot. Say the word and it becomes a
  text-only panel instead.
- **Stage 06 shows a hand.** The no-people rule was given for the hero blocks.
  This is the grinding itself, and the same clip already plays in the "how it is
  made" carousel, so it is consistent with what is already on the page — but it
  is a hand, and it should be a deliberate choice rather than an oversight.
- **Twenty products still have no journey.** Chilli Powder is the obvious next
  one: `proc-chilli.mp4` is already in `assets/` and unused.

### The trigger was invisible — fixed same day

The first cut put a single quiet text link at the foot of the card body. On a
real screen that link fell **below the card's visible edge**; the owner opened
the page and could not find the feature at all. Two changes:

- **A gold "How it's made" badge now sits ON the photograph**, bottom-right,
  where nothing can push it out of view. `--ink` on `--gold` — 4.81:1, the same
  pairing the "Order on WhatsApp" button uses, so it reads as the same family of
  control. Hover goes to `--gold-lt` (7.57:1). White on gold was the first try
  and measured **3.06:1**, under AA for text that size.
- The badge lives **inside** `.pthumb`, and the photo probe rewrites that
  element's `innerHTML` wholesale — so `productCard()` now carries the badge
  across the swap by hand. Verified: badge still present and clickable after the
  photograph replaces the tile.

The text link stays as a second route for anyone reading rather than scanning.
Both carry `data-journey`, and the delegate listens on `[data-journey]`.

---

## `inline.html` — the same journey, nothing hidden (20 Sep 2026)

> "I'm not sure how many customers will open and see."

That is the right objection to the overlay, and it is not a design problem — a
click is a toll and most people do not pay it. So this page puts the whole thing
in the open. **`index.html` is untouched**; the two exist side by side.

| | `index.html` | `inline.html` |
|---|---|---|
| Turmeric card | 248px tile + gold "How it's made" badge | **full-width band, spans the grid row** |
| The six stages | behind one click | **all visible while scrolling** |
| The clip | in the overlay | **plays in the strip, in place** |
| Overlay | the main event | still there, optional |

### What the band is

A full-bleed row inside the range grid: the product on the left, the "How
turmeric becomes haldi" lede on the right, then a **six-tile filmstrip** — one
portrait picture per stage with its number, its elapsed time, its title and a
one-line caption. The sixth tile is the stone-grinder clip, which starts playing
when it scrolls into view. Under it, one line and a quiet link to the full-screen
version for anyone who wants it.

The stage captions are a new `short` field on each stage — the overlay's
paragraphs are too long for a 180px column, and truncating them would have lost
the timings, which are the most persuasive thing in the whole sequence.

### How it is switched on

`<body class="jrn-inline">` plus one extra stylesheet. That is the entire
difference between the two files. `showGroup()` picks the renderer:

```js
pGrid.appendChild(INLINE && JOURNEYS[p.en] ? journeyCard(p) : productCard(p));
```

So a product with no journey renders as an ordinary card on both pages, and
`index.html` cannot accidentally inherit the band.

### Decisions worth knowing

**The band does not lift on hover.** `.pcard:hover` raises a tile 7px, which
reads as a mistake at 1126px wide — and there is no longer one thing to click.

**Below 1100px the strip becomes a swipeable rail, not a wrap.** A 2×3 wrap
loses the sense of one thing following another, which is the entire point of
showing it as a sequence. Measured at 390px: strip scrolls 1540px inside 337px,
page overflow 0.

**The clip is created on scroll, not in the markup.** A band this wide should
not cost a video decode the moment the grid renders on a phone. The `<video>`
is built and played only when its tile is ≥50% in view, and paused when it
leaves — the same rule the overlay uses.

**`showGroup()` re-attaches the observer.** It is the one place the grid is
ever rebuilt, so it is the one place that can do this. The first cut called
`watchFilm()` once at load, which ran *before* the grid existed and silently
observed nothing — the clip never appeared. Verified after a shelf change:
observer re-attached, clip loads and plays.

### Contrast, measured

`--sage-soft` is 4.84:1 on white, which is what the ordinary card sits on. This
band is a gradient that **ends on `--sand`**, where the same ink falls to
**3.93:1** — under AA. The three inks that sit low in the band (the product
line, the tile captions, the foot) went to `--sage`, 5.02:1. `--gold-dk` on the
numbers and time chips already clears it.

### Checked

1440×1000 and 390×844: six tiles, clip plays in place and pauses when it leaves,
a tile and the foot link both open the overlay, Escape closes it, the Spices
filter keeps the band and re-attaches the observer, Pulses drops it and renders
two ordinary cards, no horizontal overflow, **zero console errors or warnings**.
`index.html` re-checked in the same session: no band, badge still there, 21 cards.

### Open

Only Turmeric has a journey, so only Turmeric becomes a band. With four or five
of them the range section gets very tall and the bands stop feeling special —
at that point the honest options are to show the band only on the shelf's first
product, or to move the bands out of the grid into their own section.

---

## `card.html` — the whole journey inside one tile (21 Sep 2026)

`inline.html` is unhidden but it does not scale. One full-width band reads well;
five of them is no longer a range, it is five essays. So this version keeps the
turmeric tile **exactly the size of the twenty beside it** and puts the six
stages inside its own square.

### Three ways to show the same six stages

| Page | Turmeric card | Stages |
|---|---|---|
| `index.html` | ordinary tile + gold badge | behind one click |
| `inline.html` | full-width band, spans the grid row | all six, side by side |
| **`card.html`** | **ordinary tile, in its grid slot** | **cycling in the picture area** |

### What it is

The card's picture area becomes a six-stage film. Each stage crossfades in with
its number, its elapsed time and its title over the photograph; a six-segment
rail across the top shows where you are. Stage 06 is the stone-grinder clip and
plays when the cycle reaches it. Below, the ordinary product body plus one quiet
link to the full-screen version.

Measured at 1440px: **card 517px, its neighbour 517px, same row.** It does not
disturb the grid.

### Decisions worth knowing

**3000ms a stage, the same beat as the hero.** `CARD_DELAY` sits beside
`SH_DELAY` so the two never drift apart.

**Hovering pauses it.** Hovering is reading, and moving the thing being read is
rude. Focus does the same, so a keyboard user is not chased down the sequence.

**The rail segments are buttons, not decoration.** With `prefers-reduced-motion`
the cycle never starts, and they become the only way through — so they have to
be operable. Clicking one also restarts the clock, so the stage you chose gets a
full beat rather than whatever was left of the last one.

**Only the visible stage's clip runs.** The others are paused, not merely hidden.

**`showGroup()` starts the films**, the same hook the inline strip uses, because
it is the one place the grid is ever rebuilt.

### Contrast, measured

Worst case is stage 03 — a studio shot **on white** — and the cycle lands on it.

| Ink | First ramp | After | |
|---|---|---|---|
| title, cream | 6.07:1 ✓ | 9.42:1 | — |
| meta line, `--gold-lt` at 9.6px | **2.08:1** ✗ | 5.41:1 | the meta sits higher in the caption, where the gradient was still thin |

The ramp now reaches `.82` by 74% — above where the caption starts on a square
tile — and holds `.93` at the foot.

**A bug the screenshot caught:** the veg mark vanished. `satva.css` positions
`.veg` against `.pthumb`, and this container is `.jcard-film`, so it arrived
unstyled and invisible. It is now positioned explicitly, at `top:30px` to clear
the rail.

### Checked

1440×1000 and 390×844: six slides, six rail segments, cycle advances, hover and
focus pause it, a rail click jumps and restarts the clock, the clip plays only on
its own stage and the others stay paused, veg mark visible, card height matches
its neighbour, no horizontal overflow, **zero console errors or warnings**.
Re-checked in the same session: `index.html` renders the badge and no band,
`inline.html` renders the band and no cycling card. The three modes do not leak.

### Open

`CARD_DELAY` is 3000ms, which gives 18 seconds for the full loop. Nobody watches
a card for 18 seconds, so most visitors will see two or three stages, not six —
this version trades completeness for not disturbing the grid, where `inline.html`
trades the opposite way. That is the actual choice between them.

---

## "How we make", per product (card.html, 21 Sep 2026)

> "implement this how we make card in this section and put all the spices in
> the spices tab"

The four-shelf version said *"Spices: stone-ground slowly, or left whole for the
tadka"* and stopped. Now the tabs choose a **shelf** and the coverflow carries
that shelf's **products**:

| Tab | Cards |
|---|---|
| Spices | **12** — Turmeric, Chilli Powder, Coriander Powder, Coriander Seeds, Cumin, Mustard, Black Pepper, Garam, Biryani, Meat, Sambar, Chatpat |
| Pulses | 2 |
| Seeds | 4 |
| Healthy Essentials | 3 |

**Turmeric's front face is the six-stage journey, cycling** — the treatment this
page is named for. Every other card keeps the ordinary front/back flip.

### Every product now carries its own process line

A new `make` field on all 21 products, written from what actually happens to
that product — not a shelf generalisation. A few:

- *Sambar Masala* — "The dals are roasted with the chillies before grinding. That is what makes it sambar."
- *Toor Dal* — "Cleaned, graded and split. Never polished with oil or water to make it shine."
- *Black Pepper* — "Picked green, blanched, then sun-dried until the skin wrinkles black."
- *Coconut Sugar* — "Sap from the flower, boiled down and dried. Nothing refined out of it."

### Media honesty, kept

An optional `mfilm` field names footage **of that product**. Six products have
it (turmeric, chilli, coriander powder, chia, flax, pink salt) and it re-uses
`proc-chilli.mp4` and `proc-dhaniya.mp4`, which had been sitting unused since
17 Sep. **A product with no film of its own shows its own photograph** — it never
borrows another product's footage. The note under the carousel counts this out
loud per shelf: *"12 on this shelf. 3 have film of the process; the rest show the
product itself until we shoot our own."*

### How it is switched on

The original block is now `if (mTrack && !CARDMODE)`, and the new one is
`if (mTrack && CARDMODE)`. `index.html`, `inline.html` and `a3.html` keep the
four-shelf coverflow byte for byte — re-verified after this change: 4 cards,
plain shelf tabs, no journey face, original note.

### Decisions worth knowing

**Held at three cards on screen.** `satva.css` hides `--abs:3`, which leaves
five — but that was tuned for a four-card row where `[data-count="4"]` *also*
hid `--abs:2`, so only three ever showed. A twelve-card shelf re-exposed the
`--abs:2` pair and they ran off both edges. The extra cards are behind, not gone.

**The stage cycle is slower than the card.html range tile** — 2600ms here
against 3000ms there, but the card also flips every 4600ms. Two fast rhythms on
one object reads as a fault rather than a sequence.

**Only the centre card's media runs.** With twelve cards under Spices that is
the difference between one video decode and twelve.

### Contrast, measured

The stage caption sits at the **top** of the card, because `.mcopy` already holds
the product name and the make line at the foot — two blocks of type at the bottom
of one card would fight.

| Ink | Before | After |
|---|---|---|
| "10–15 DAYS", `--gold-lt` at 9.3px | **3.75:1** ✗ | 6.69:1 |
| stage title, cream | 6.52:1 ✓ | 11.6:1 |

The caption's ramp faded from .86 to .72 by 58%, but the text occupies 58–90% of
that band. It now holds .88 to 80% and releases only at the foot.

### Checked

All four tabs build and rebuild, 12/2/4/3 cards, arrows step and return, the note
pluralises correctly ("1 **has** film", not "1 have"), the journey face cycles
its six stages, no horizontal overflow, **zero console errors or warnings**.

### Open

Six products have film; fifteen show a photograph. The five with neither their
own photo nor a film fall back to the shelf picture — Coriander Seeds, Black
Pepper, Sambar Masala, Coconut Sugar and Monk Fruit Sweetener are the ones to
photograph first.

### A taller card, so the picture has a middle (21 Sep 2026)

> "I'm not able to see the picture inside the card clearly. Make the card little
> longer and the letters aligned to the top and bottom so that the process is
> clearly seen."

The selected card was **5:4 landscape** — wide and short — with the stage caption
pinned to its top and `.mcopy` to its bottom. Both are sized by their own content,
so on a short card they met in the middle and the photograph became a strip
between two captions.

The fix is the card's shape, not the scrims. Because neither text block grows
with the card, **every pixel of added height goes to the clear band**:

| | Card | Clear band | Share of card |
|---|---|---|---|
| Desktop, before | 570 × 456 (5:4) | ~250px | 55% of a short card |
| Desktop, after | **440 × 528 (5:6)** | **275px** | 52% of a much taller one |
| Phone, before | 281 × 337 | **75px** | **22%** |
| Phone, after | **328 × 459 (5:7)** | **196px** | **43%** |

75px of picture is not a photograph, it is a gap between two captions. The phone
card had 180px of unused stage sitting under it, so it took it.

**Neither scrim was touched**, so the contrast figures already recorded for
`.mcopy` and for the stage caption still hold. The caption's top padding came
down from 58px to 42px — the "How it is made" tag ends at 34px, so 42 clears it
with a hair to spare and the caption sits harder against the top edge.

**The stage follows the card.** At 66vh it stood 132px taller than the card and
opened a dead gap above the tabs; 58vh leaves 26px top and bottom.

**The side cards came down a step.** The selected card used to be the only
landscape one in a row of portraits, which is how it announced itself. Now that
it is portrait too, size and the gold edge have to do that job alone.

Checked at 1440×1000 and 390×844: card fits the stage at both, clear band 275px
and 196px, no horizontal overflow, zero console errors. `index.html` re-verified
after the change — still 4 cards at 5:4, stage 480px, untouched.

---

## Eight more journeys (21 Sep 2026)

> "same like turmeric, in this place, find stunning pictures of the processes
> for all the items here and place them in the card"

**Nine of twenty-one products now have one. Thirteen do not, and cannot yet.**

### What was searched

Wikimedia Commons and the Openverse API, ~40 query sets, commercial use only.
The result is the same shape as the turmeric finding: the free-licence pool is
deep for a few crops and empty for most.

| Built | Stages | Strength |
|---|---|---|
| Turmeric | 6 | the reference |
| **Chilli Powder** | 4 | strong — field, an aerial drying yard, baskets |
| **Mustard Seeds** | 3 | strong — a full yellow field, black seed macro |
| **Flax Seeds** | 3 | strong — blue flower, a field of bolls |
| **Quinoa** | 3 | strong — purple seed heads |
| **Monk Fruit Sweetener** | 3 | strong — gourd, dried fruit, powder |
| **Coriander Powder** | 3 | good — flower macro, powder |
| **Toor Dal** | 3 | fair — the dal shot is busy |
| **Coriander Seeds** | 3 | fair — shares two stages with the powder |

### What could not be built, and why

| Product | What the pool returned |
|---|---|
| Cumin Seeds | Egyptian museum artefacts and 16th-century botanical plates. No crop, no process. |
| Methi Seeds | Plant photographs exist; **every download failed** to Wikimedia throttling. Retry — this one is recoverable. |
| Chana Dal | Unlabelled USDA bean photographs; nothing identifiable as chana. |
| Chia Seeds | Only *Salvia columbariae*, a wild American cousin, not *S. hispanica*. |
| Himalayan Pink Salt | Only the **Turda** mine in Romania. Using it would say "Himalayan" over a Romanian photograph. Refused. |
| Coconut Sugar | Zero results on every query. |
| Black Pepper | One usable frame (peppercorns). The drying-yard photograph turned out to be banana trees and a shed. One frame is not a journey. |
| Garam · Biryani · Meat · Sambar · Chatpat | Blends. Their process is roast-and-grind, and only generic spice-bowl stock exists. A shared generic sequence across five products would be filler. |

### Decisions worth knowing

**These are shorter than turmeric on purpose.** Turmeric has six stages because
six good photographs of the turmeric process exist. Padding the others to six
would mean a dull or borrowed picture to hit a number — the exact thing this
block is meant to prove we don't do. Three real stages beat six with two lies.

**Every card starts on a different stage.** Coriander Powder and Coriander Seeds
share their first two stages — same plant, same photograph — so in lockstep they
sat side by side in the grid showing an identical frame and read as one
duplicated card. The offset is by grid position, so it fixes every such pair.

**"Film" became the wrong word.** The shelf note counted journeys as film; most
of these are photographs of the process, not footage. It now reads "5 show how
they are made, step by step" — and agrees in number ("1 shows how it is made").

**This changes `index.html` too, by design.** `JOURNEYS` drives all three
treatments, so index went from one gold badge to **nine**, inline can band any of
them, and card.html cycles nine tiles. Nothing was edited on those pages.

### Checked

27 stage images requested, **zero broken**. 9 cycling tiles in the range, 9
across the four shelves in "How we make", the full-screen overlay opens for a
non-turmeric product with its credits intact (Chilli Powder: 6 panels, 3
credits), Escape closes and cleans up, no horizontal overflow, **zero console
errors or warnings**. `index.html` re-verified: 9 badges, no band, no cycling
tile, original 4-card make section.

### Open

- **Methi is the cheapest win left** — the photographs exist on Commons
  (`Trigonella foenum graecum-1-bangalore-India.jpg`, `Fenugreek Seeds 01.jpg`);
  only the download failed. Retry when Wikimedia is not throttling.
- **Black pepper needs one more frame** — a vine or a real drying yard, and it
  becomes a three-stage journey immediately.
- The rest need photographs that do not exist under a free licence. They are the
  argument for the owner's own camera: a phone, a sunny afternoon and the actual
  mill would beat everything in this table.

---

## Correction: seven more journeys, and why the last entry was wrong (21 Sep 2026)

**The "these cannot be built" table in the entry above was wrong.** Sixteen of
twenty-one products now have a journey. Only the five masala blends do not.

### What actually happened

Partway through the session `commons.wikimedia.org` began **failing its TLS
handshake** from this machine — `curl` exit 35, HTTP 000, instantly. The search
script caught the exception, retried three times, and returned an empty list.

So "Cumin: zero results. Chana: zero results. Chia: zero. Salt: zero. Coconut
sugar: zero." did not mean the photographs do not exist. **It meant the queries
never reached Wikimedia.** I read a network failure as a fact about the world and
wrote it into the change log as one.

The tell was there and I missed it: *five consecutive categories returning
exactly zero* is not what a sparse archive looks like. A sparse archive returns
junk — Egyptian museum artefacts, botanical plates, the wrong species. Silence
means the pipe is broken.

### The route round it

Two hosts, checked separately:

| Host | State |
|---|---|
| `commons.wikimedia.org` | TLS failure, total |
| `upload.wikimedia.org` | **up** (301/200) |
| `api.openverse.org` | **up** (200) |

Openverse indexes Commons, so the searches were re-run there. Downloads go
direct to `upload.wikimedia.org` with hand-built `/thumb/` paths — that host
rejects arbitrary widths (`HTTP 400: Use thumbnail sizes listed on…`), so the
fetcher tries 1280, then 1024, then 1920.

### What came back

Every category I had written off:

| Product | Stages | What was found |
|---|---|---|
| **Himalayan Pink Salt** | 3 | the **Khewra mine in the Salt Range** — the actual source. Earlier I had only found the Turda mine in Romania and refused it. |
| **Chia Seeds** | 3 | real *Salvia hispanica* in flower, leaf, and a seed macro |
| **Cumin Seeds** | 3 | a cumin field in white flower, by Raju Odedra |
| **Methi Seeds** | 3 | plant and seed — the downloads had failed, not the search |
| **Black Pepper** | 3 | a true *Piper nigrum* vine on its support tree |
| **Coconut Sugar** | 3 | the flower spike, and sap pots strapped to the trunk |
| **Chana Dal** | 3 | a chickpea field; the dal stages reuse `cat-pulses.jpg` |

Two near-misses avoided: *Nekemias arborea* and "pepper vine leaves in autumn"
are a North American ornamental, not black pepper. Both were excluded by name in
the fetch list.

### Where it stands

| Shelf | Documented |
|---|---|
| Spices | 7 of 12 |
| **Pulses** | **2 of 2** |
| **Seeds** | **4 of 4** |
| **Healthy Essentials** | **3 of 3** |

The shelf note now reads "2 show how they are made, step by step." with no
trailing clause when a shelf is complete.

**Only the five masalas are left**, and they are a real exception rather than a
sourcing failure: Garam, Biryani, Meat, Sambar and Chatpat are blends whose
process is roast-and-grind. One generic sequence shared across five products
would be filler. They need the owner's own photographs of the owner's own
roasting pan — which is the only honest version anyway.

### Checked

44 stage images requested, **zero broken**. 16 cycling tiles in the range, all
four shelves in "How we make" rebuild correctly, no horizontal overflow, **zero
console errors or warnings**.

---

## Every stage is now a real photograph of that thing (21 Sep 2026)

> "I want the real pictures of the plants and things in it"

Fair, and the audit backed it up. **Nine of the sixteen journeys had at least one
stage that was not a real photograph of that stage** — either the same file shown
twice, or a stock spice-bowl composite, or the generic shelf picture standing in.

| Product | Was | Now |
|---|---|---|
| Coriander Seeds | stages 2 and 3 the **same file** | whole seed in a brass mortar (CC0) |
| Cumin Seeds | stages 2 and 3 the **same file** | threshed seed, then a seed macro |
| Methi Seeds | stages 2 and 3 the **same file** | the crop growing in soil |
| Chana Dal | stages 2 and 3 both `cat-pulses.jpg` | a chickpea plant in flower, then split gram |
| Chilli Powder | `p-mirchi.jpg`, a stock composite | the site's own chilli-powder photograph |
| Flax Seeds | `p-flax.jpg`, stock | a flax seed macro |
| Quinoa | `p-quinoa.jpg`, stock | coloured quinoa from the INIA Juliaca genebank |
| Black Pepper | `p-pepper.jpg`, stock | peppercorns in a mortar |
| Coconut Sugar | stages 2 and 3 the **same file** | **cut to two stages** — see below |

**Coconut Sugar is two stages now, not three.** The boiling-down step is real and
is described on the closing card, but no usable photograph of it exists: the only
candidate was a *museum display* of jaggery tools behind glass with a "do not
touch" sign. Repeating the sap photograph to reach three was the dishonest
option, so it has two stages and says the third in words.

### Two things that were nearly shipped and should not have been

**A competitor's retail packet.** The highest-resolution "Red chilli powder" on
Commons (6158×8399) is a photograph of a branded 100g pouch — another company's
logo, artwork and net weight, front and centre. Deleted.

**A herbarium sheet.** The best "fenugreek pods" result was a pressed botanical
specimen mounted on card — accurate, and completely wrong for a card that is
meant to show a living crop. Replaced with the plant in soil.

Also excluded by name in the fetch list: *Nekemias arborea* and "pepper vine
leaves in autumn", both a North American ornamental rather than *Piper nigrum*.

### Audit

A script now walks `JOURNEYS` and flags any stage image that is a duplicate
within its own product, a `cat-*` shelf photo, or a `p-*` stock photo. **It
reports zero.** Worth re-running whenever a journey is added.

### Known soft spot

`arch-spices-chilli-powder.jpg` is 680×680 — it was cut for the small hero arch,
not for a full-bleed card. Sharp enough at the range tile (260px) and the make
card (440px); visibly soft in the full-screen overlay, which goes to 1440px. It
is the only genuine chilli-powder photograph on hand that is not someone else's
packaging, so it stays until a better one turns up.

### Checked

48 unique stage images across 16 journeys, **zero broken**, zero duplicates, zero
stand-ins, zero console errors.

---

## Grinding films for the five masalas (21 Sep 2026)

> "find some videos where there grind these masalas and add some stunning videos
> of grinding those whole ingredients and make them into powder"
> …"i meant this grinding only for the masala part"

**Scope: the five blends only.** Garam, Biryani, Meat, Sambar and Chatpat were
the last products without a journey, and they are a different problem from a
single spice — a masala has no field and no harvest of its own. Its process *is*
roasting and grinding, which is why footage was the right ask.

The other sixteen products are unchanged and carry photographs only. Turmeric's
stone-grinder clip predates this entry.

### Five distinct films, one per blend

| Blend | Film | Source |
|---|---|---|
| Garam Masala | a pestle working spice powder in a mortar | `proc-seeds.mp4`, Pexels |
| Biryani Masala | a sil-batta, the flat Indian grinding stone | `proc-dhaniya.mp4`, Pexels |
| Meat Masala | a wooden mortar and pestle | `proc-salt.mp4`, Pexels |
| **Sambar Masala** | **a water-driven atta chakki, the stone turning** | `proc-chakki-stone.mp4`, **new** |
| **Chatpat Masala** | **the same mill, flour lifted off the stone** | `proc-chakki-flour.mp4`, **new** |

The first three are Pexels clips that were already sitting unused in `assets/`
(free commercially, no attribution). No two cards show the same film.

### The two new clips

Cut from **"Flour mill running on water in Tawang district"** — CC BY-SA 4.0,
Research Institute of World's Ancient Traditions, Cultures and Heritage — a
traditional water-driven stone mill at Sakyur village, Arunachal Pradesh.

Cut to the site's existing recipe: **6s, square, 720px, silent, H.264 CRF 31**,
with a poster frame each. 440 KB and 212 KB. `ffmpeg` came from the
`imageio-ffmpeg` static binary, the same route the original six clips used.

**Said plainly on the card:** that mill is grinding **millet**, not our masala,
and it is not our mill. Each stage's credit line says so rather than letting the
picture imply otherwise.

### Two clips rejected first

`Water wheel powered flour mill … 02` and `03` were downloaded and sampled before
use — both show the **water wheel outside**, the power source, not the stones. A
spinning wheel on a masala card is off-topic. Only the clip whose frames actually
show the millstone and the flour was cut.

### Two stages each, not three

A blend genuinely has two steps we can show — what goes in, and the grinding.
No roasting photograph exists in the free pool that is not a cooked dish, and
padding with one would repeat the mistake the earlier entries were pulled up for.

### Where it stands

**All 21 products now have a journey.** Every shelf note reads complete:
"12 on this shelf. 12 show how they are made, step by step."

### Checked

21 of 21 cards cycling, 6 distinct films across the page, the Sambar clip
confirmed playing at 720×720 in its card, all four shelves complete in "How we
make", no horizontal overflow, **zero console errors or warnings**.

---

## Botanical audit: does each picture show what the card claims? (21 Sep 2026)

> "check every process again and if its the actual fruit or leaf or plant that
> you are saying for each one"

Every one of the 55 stages was pulled out with its claim and its image and
checked side by side. **Eight stages claimed something the photograph did not
show.** All eight are fixed.

| Product | The claim | What the picture actually showed | Fix |
|---|---|---|---|
| **Coriander Seeds** | "Threshed… nothing is ground" | a frame containing **ground powder** | swapped to the whole seed in a brass mortar |
| **Mustard Seeds** | "Left standing until the **pods** rattle" | threshed seed, no pods | retitled "Brown seed out of a yellow field" |
| **Monk Fruit** | "A small melon **on a vine**" | picked fruit in a pile | retitled "A small melon, picked hard" |
| **Methi Seeds** | "**Slim pods**, hard yellow seed" | leaves, no pods visible | retitled "It grows low, and close together" |
| **Chia Seeds** | "Cut when the **heads dry**" | green leaf, nothing dry | retitled "Square stems, and a mint's leaf" |
| **Chana Dal** | "Dried on the plant, **brown and brittle**" | a **green plant in pink flower** | **stages swapped** |
| **Chana Dal** | "A short, dry-season crop" | a brown, dried-off field | **stages swapped** |
| **Coconut Sugar** | coconut sap tapping | **date palms**, not coconut | labelled as date palms, in the copy and the credit |

### The chana fix is the interesting one

Its two frames were simply **in the wrong order**. The green flowering plant sat
under "brown and brittle", and the dried-off brown field sat under "a short,
dry-season crop". Swapping them made both captions true of their own picture and
needed no new photography — the material was right, the pairing was wrong.

### Two stages now say out loud what they are not

- **Coconut Sugar, "Cut, and collected"** — the palms are *date* palms. The
  tapping is the same job done the same way, and the card says so rather than
  letting the picture pass as coconut.
- **Turmeric, "Boiled, within two days of lifting"** — the frame is a root cut
  open beside its powder, not a boiling vat. No photograph of turmeric being
  boiled exists under a free licence; the card now says that instead of leaving
  it to the earlier README note where a visitor would never see it.

### What was checked and passed

The other 45 stages match their claim, including every species identification:
*Coriandrum sativum* in flower, *Brassica juncea* in field, *Cajanus cajan* with
flowers and pods together, *Linum usitatissimum* blue flower and bolls,
*Chenopodium quinoa* seed heads, *Salvia hispanica* (real chia, not the American
*S. columbariae*), *Piper nigrum* on its support tree, *Cicer arietinum* in pink
flower, *Trigonella foenum-graecum*, *Siraitia grosvenorii*, and the Khewra mine
in the Salt Range.

### Checked

52 unique stage images, **zero broken**, zero duplicates within a product, zero
generic or stock stand-ins, 21 of 21 cards cycling, the corrected Chana Dal
journey verified end to end in the full-screen panel, **zero console errors**.

---

## "Cook something for someone", after Seedlip (card.html, 21 Sep 2026)

> "I want the cook for everyone part to be of this background colour and
> arranged like this" — seedlipdrinks.com/en-us

### Measured, not eyeballed

Their stylesheet was pulled (`/_next/static/immutable/chunks/1a8q11noxsezb.css`)
and the two colours read straight off it rather than guessed from the screenshot:

| | |
|---|---|
| ground | **`#fff1e4`** — a warm cream with a pink cast |
| green | `#154734` — their bottle green |

Those two against each other measure **9.56:1**.

### What was borrowed, and what was not

**Borrowed:** the ground, and the arrangement — a centred small-caps kicker over
a centred serif headline, then four **tall portrait** photographs with squared
corners, the dish name under each in caps and the product under that in italic.

**Not borrowed: their green.** We keep `--ink` and `--band`, which on `#fff1e4`
measure **13.3:1** and **7.90:1** — both better than Seedlip's own pairing, and
still our brand rather than theirs. The ask was the background and the layout.

### Three things this undoes

- **The mint gradient**, which this block has carried since 18 Sep. Two older
  `.recipes` rules in `satva.css` both set a background, so the new file sets
  `background-image:none` explicitly rather than trusting the cascade.
- **The squircle "bowl" crop** taken from sweetgreen. Seedlip's cards are plain
  rectangles, and the height is what gives the row its rhythm — `clip-path:none`,
  `border-radius:0`, `aspect-ratio:2/3`.
- **The per-product accent colour** on the "Made with…" line, which is now one
  italic serif in `--band`.

### The kicker is generated, not marked up

`.rechead::before` supplies "SATVA RECIPES". The markup for this section is
shared with `index.html` and `inline.html`, and adding an element there would
leave a stray unstyled line on both. It is decorative — the `<h2>` underneath
still carries the section's real heading.

### Scope

`card.html` only, via `css/recipes-seedlip.css`. Deleting that one `<link>` puts
the mint back. Re-verified after the change: `index.html` still renders the mint
gradient, left-aligned head, no kicker, and the 1:1 bowl-clipped photographs.

### Checked

1440×1000 and 390×844: ground `rgb(255,241,228)`, no gradient, four cards all
with photographs, 2:3 on desktop and 3:4 one-up on a phone (2:3 is too tall in a
single column), no horizontal overflow, **zero console errors**.

---

## Studio grounds, density, and the dropdown (card.html, 21 Sep 2026)

Four asks in one pass.

### 1. Seedlip's studio grounds behind each dish

> "can you see the background colours inside these 4 images. I want that to be
> in all the boxes that we have and then the dish"

Those are not photographs with a tint — each drink is **cut out** and stood on a
built pastel ground. So that is what was done, properly:

- `rembg` (u2net, ONNX) installed into `scratchpad/pylibs`, run against the
  **originals** in `assets/_orig/` rather than the already-cropped versions.
- Each ground is generated, not sourced: a soft vertical wash with a flat
  "table" band across the lower fifth and a 30px soft seam, plus a blurred
  elliptical contact shadow so the dish stands on the table instead of floating.
- Colours are chosen **against** the dish, the way Seedlip does it — the yellow
  poha gets a cool blue, the orange dal a pink, the near-black vangi a pale
  sage, the beige quinoa a lemon.

`scratchpad/studio.py` regenerates all four; the palette is four tuples at the
top of it.

**One bug caught in the first composite:** the dish was scaled by height only,
so a wide bowl burst out of the canvas. It now scales by whichever dimension
binds, inside a 78% × 60% box.

### 2. The photographs were re-cropped first

> "delete all the different colours in the picture and keep only the dishes"

Before the cutouts, each was cropped tight to the dish — the marble edge, the
grey slate and scattered spices, the pink card table and the red restaurant wall
are all simply out of frame. That crop still matters: it is what `_orig/` is
measured against, and it is the fallback if a cutout is ever redone.

### 3. Density pass — the whole page

> "cut down all the extra space… make the blocks visible block by block"

**Measured first**, at 1440×1000:

| Block | Before | After |
|---|---|---|
| **whole page** | **9971px** | **8809px** |
| range | 3452 | **2298** |
| made | 788 | 731 |
| recipes | 781 | 754 |
| mission · saheli · contact | — | all well inside a screen |
| top · categories · reasons | 919 / 1000 / 1000 | unchanged — already one frame by design |

**The range cannot be a single screen and stay readable**, and it is worth
saying so plainly: 21 cards at four across is six rows, and fitting that into
1000px would mean a 150px card — a thumbnail, not a product. What it got
instead is five columns and ~136px off every card (the picture from 1:1 to 4:3,
and the body padding it did not need). A single shelf tab — Spices, twelve —
now lands much closer to one screen.

### 4. The range dropdown now closes when the cursor leaves

> "once the user goes up with his cursor, then close that extension of spices"

The submenu opens on `:hover` **or** `:focus-within`. Clicking "Our Range"
leaves focus on that anchor, so `:focus-within` held the panel open after the
pointer had gone. A `mouseleave` handler now blurs the focused descendant, which
releases it. Keyboard users never fire `mouseleave`, so tab-through is untouched.

**This one is in `js/satva.js`, not a scoped stylesheet** — it is a bug, not a
design choice, so every page gets it.

### Checked

Recipes 754px in a 1000px viewport, all four composites loading, range ground
`rgb(255,241,228)`, dropdown verified open-on-focus then closed-on-leave with
focus released, no horizontal overflow, **zero console errors**.

### Correction: it still did not fit, and why (21 Sep 2026)

The previous entry claimed the recipes block was fixed at 754px in a 1000px
viewport. **It was not fixed, and the measurement that said so was wrong twice:**

1. **It ignored the sticky header.** The nav floats over the content, so the
   usable height is `100svh − 81px`, not `100svh`. Every "fits" check was
   comparing against 81px it did not have.
2. **It only ever tested a tall window.** Re-measured at **1440×800**, a normal
   laptop: usable 719px, section 750px — **31px over**. That is exactly the
   clipped headline and the cut-off button in the owner's screenshot.

### The fix: size from the height that is left, not from the column width

The photograph was sized by `aspect-ratio` off the column **width**, so it grew
on a wide screen regardless of how short that screen was. It now takes what the
viewport has left:

```css
height: clamp(150px, calc(100svh - 400px), 430px);
```

400px is the measured chrome — head, name, product line, button, padding — plus
the 81px nav. Every spacing value in the block moved from `vw` to `vh/svh` for
the same reason, and the headline's `max-width` widened to 22ch so it stays two
short lines instead of wrapping to three on a narrow column.

`scroll-margin-top:86px` was added so a jump to `#recipes` lands below the
header rather than under it.

### Measured at four heights, scrolled so the section top meets the nav

| Viewport | Section | Photo | Everything on screen |
|---|---|---|---|
| 1366×**720** | 611px | 320px | ✓ |
| 1440×**800** | 703px | 400px | ✓ (button bottom 783 of 800) |
| 1920×**1080** | 774px | 430px | ✓ |
| below **620px** tall | — | 190px fixed | scrolls, deliberately |

Under about 620px of viewport height there is no honest way to show a head, four
photographs and a button at once — the photograph would be a 100px strip. Below
that it scrolls, which is better than an unreadable row.

**Zero console errors, no horizontal overflow at any of the four.**

### The full-height blocks were 81px too tall (21 Sep 2026)

> "Remove this space from here and fill it"

`.cats` ("Something for every shelf") and `.reasons` ("What we will not do") were
built as `min-height:100svh` with their content centred. Later, a note in
`satva.css` records adding `padding-top:max(96px,…)` so the centred content could
not rise behind the sticky nav. **Both changes are individually right and
together they are wrong:** a block that is a whole screen tall, plus 96px of nav
clearance, is 81px taller than the screen has room for.

Measured at 1440×800, scrolled so the section meets the nav:

| | Before | After |
|---|---|---|
| usable height | 719px | 719px |
| section height | **800px** (81px over) | **718px** |
| gap above the kicker | **150px** | **102px** |
| last card fully visible | ✗ clipped | ✓ |
| category picture | 448px | **456px** |

The block is now `100svh − 82px`, the picture is sized from what is left
(`calc(100svh − 344px)`, ceiling 620px so a tall monitor fills instead of sitting
on a 520px picture with slack centred around it), and `padding-top` is at its
floor of 84px — the nav is 81px deep and the kicker needs a few pixels of air.
The remaining 102px is that clearance; it cannot go lower without putting the
heading back under the header.

### A selector bug that made the first attempt a no-op

The first version of this block targeted `.categories`. **That is the id, not a
class** — the element is `<section class="cats" id="categories">`. None of it
applied, and the re-measurement came back byte-identical to before, which is what
caught it. Worth remembering: this section is `.cats` in CSS and `#categories` in
markup, and the two do not match.

`.reasons` is a real class and was fine; it now measures 718px too, with all four
circles visible.

---

## Promoted to the site, variants retired (21 Sep 2026)

> "keep only this http://127.0.0.1:8003/card.html and delete all the other
> sites that are too many and change the address"
> …"keep the original and what we developed now"

**`card.html` is now `index.html`**, so the address is the bare
**http://127.0.0.1:8003/** with no filename.

| | |
|---|---|
| **Kept** | `site-v3/index.html` — was card.html, the chosen design |
| **Kept** | `~/dssatva/site/` on **:8000** — the original, as asked |
| Retired | `inline.html`, `a3.html`, the old `index.html`, `css/journey-inline.css` |
| Stopped | the :8011 comparison-page server |

### The retired pages are in `_retired/`, not deleted

**Nothing in this folder is tracked by git** — `git ls-files site-v3/` returns
zero. Every file here exists only on disk. So the three pages were copied to
`_retired/` before removal rather than thrown away:

```
_retired/index.html           the gold-badge-and-overlay version
_retired/inline.html          the full-width band version
_retired/a3.html              the chilli-and-garlic-on-slate hero
_retired/journey-inline.css   the band's only stylesheet
```

Copy one back beside `index.html` and it works again exactly as it did.

**No git commit was made** — the owner did not ask for one, and committing their
repository is their call, not mine. The `_retired/` copy is the safety net
instead. If this folder matters, it is still worth committing: an accidental
`rm` in here has nothing behind it.

### Nothing was linked between the pages

Checked before deleting: the only mentions of `inline.html`, `a3.html` and
`card.html` anywhere in the HTML, CSS or JS were **comments**. No navigation, no
imports, no scripts. So the removal needed no other edit.

### Two stale headers rewritten

The promoted file still opened with "THE ONE-CARD VARIANT … a copy of index.html"
and "VARIANT C — page 1 of 2", describing a comparison that no longer exists.
Both now describe what the file actually is, and point at `_retired/` for the
alternatives.

### Verified after the move

`http://127.0.0.1:8003/` → 200, and `/card.html`, `/inline.html`, `/a3.html` and
`:8011` all correctly gone (404 / not serving). `:8000` still 200.

On the live root: `body class="jrn-card"`, all seven stylesheets loading,
**21 of 21 cards cycling their journey**, 12 cards on the Spices shelf in "How we
make", recipes ground `rgb(255,241,228)`, four cut-out dishes, **zero console
errors**.

### The studio grounds, lightened (21 Sep 2026)

> "can you make the background of the picture little lighter"

The first set read as solid pastel blocks rather than Seedlip's airier studio
sweeps. Rather than hand-pick eight new colours, `scratchpad/studio.py` now
carries one dial:

```python
LIGHTEN = 0.38     # 0 = the colours as listed, 1 = flat white
def lift(c): return tuple(v + (255 - v) * LIGHTEN for v in c)
```

Every ground is mixed 38% toward white on the way in, so hue and the top-to-
bottom sweep are preserved and only the value rises. Turning one number
re-renders all four consistently; the twelve source colours never change.

**The contact shadow came down with it**, from alpha 92 to 62 and from
`(90,80,70)` to `(122,110,98)`. At the old weight it read as a smudge under a
pale ground instead of a shadow.

File sizes are effectively unchanged (132/110/69/47 KB). Verified on
`http://127.0.0.1:8003/`: four photographs loading, section 703px, zero console
errors.

**To tune again:** edit `LIGHTEN` in `scratchpad/studio.py`, run
`python3 studio.py`, and copy `_light_recipe-*.jpg` over `assets/recipe-*.jpg`.
The originals stay in `assets/_orig/` and are what the script reads, so this is
repeatable without degrading.

---

## Footer rebuilt as the compact rail (22 Sep 2026)

> "I dont like the background part of this part, the pictures which are
> inside.. I want a different framework also" — then, from three options
> compared at `/footers.html`: **"Implements this"** (Option C).

### The background photograph is gone

The footer stood on `assets/footer-collage.jpg` — our own contact sheet of twelve
site photographs, pinned with `background-attachment:fixed` and washed to 92–95%
of the plum. At that wash it was barely a picture and mostly just muddied the
ground. `footer-rail.css` replaces the whole thing with one colour:

```css
background-color:#372e35;
background-image:none;        /* explicit: satva.css sets two image layers */
background-attachment:scroll;
```

**The plum grey the owner chose on 18 Sep is unchanged** — it is only flat now.
Verified with a network filter: `footer-collage.jpg` is no longer requested, so
that is **653KB off every page load**. The file stays on disk in case the old
treatment is ever wanted back.

### The framework

One band of three columns — mark and tagline left, the three link groups across
the middle, WhatsApp and the credit right — then a rule and the legal line.

| | Before | After |
|---|---|---|
| desktop height | ~940px | **359px** |
| phone height (390px) | — | 886px |
| background requests | 1 (653KB) | **0** |

### What moved, and the one thing that was cut

- The WhatsApp button, the per-gram note and the flax credit left the brand
  block for their own right-hand column. The credit's long comment about *why*
  it must stay went with it, unchanged.
- **The long blurb came down to its last clause** — "Clean, authentic and
  untouched by harmful chemicals." That was in the option as shown and approved,
  but it is the one place content was removed rather than moved: the full
  sentence about ground spices, unpolished pulses and nutrient-dense seeds is
  no longer in the footer. It still appears in the mission and the hero. Say the
  word and it comes back.
- Both `TO FILL` notes survived — FSSAI licence number, and Instagram / Google
  Business links.

### Two spacing bugs found by measuring rather than looking

1. **`.fcol ul` is a grid with `gap:10px`** in `satva.css`. A `margin` on the
   `li` stacks on top of that, so asking for 7px produced 17px. Setting the
   grid's own gap is the only thing that controls it.
2. **The single-column breakpoint was at 460px**, which at 390px stacked all
   fourteen links and made the footer 1018px tall. Moved to 360px — two columns
   hold down to roughly there, where "Healthy Essentials" finally needs the full
   width. 886px now.

### Contrast, unchanged and still measured

Every ink is one already recorded for this ground: `--cream` 9.65:1,
`--gold-pale` 9.77, `--f-muted` 7.04, `--gold-lt` hover 6.74. The credit line is
the one new value, `#b3a891` at **5.52:1** — deliberately quieter than the note
above it, still clear of AA.

### Housekeeping

`/footers.html`, the three-option comparison page, has been deleted. The site is
one page again.

---

## `split.html` — the cream-over-green footer, as a second page (22 Sep 2026)

> "Keep this colour combination in the end after the site with the same colour
> combination. Add after cook for someone and give me a new website. and keep
> the old one like itself."

Option B from `/footers.html`, built on **its own page**. `index.html` is
untouched and still carries the compact plum rail — verified after the change:
footer 359px, `rgb(55,46,53)`, `.frail` present, `.fsplit-top` absent,
`footer-rail.css` still the only footer stylesheet it loads.

| | `index.html` | `split.html` |
|---|---|---|
| Footer | compact rail, flat plum | **cream band over green** |
| Height (desktop) | 359px | 878px |
| Stylesheet | `footer-rail.css` | `footer-split.css` |
| Everything above the footer | identical | identical |

### The colour logic

The cream is **`#fff1e4`** — the same ground the recipes and the range already
carry, so the page **closes in the colour it has been using** rather than
introducing a new one. The green below is `--green` `#2c4220`, which puts real
weight at the foot. Both flat; the collage photograph is gone here too.

It sits directly after "Cook something for someone", which is what makes the
cream read as continuous rather than as a new band.

### Contrast, measured on both grounds

| Ink | On | |
|---|---|---|
| `--ink` headline | `#fff1e4` | 13.3:1 |
| `--band` paragraph | `#fff1e4` | 7.90:1 |
| `--cream` links | `--green` | 8.11:1 |
| `--gold-lt` headings | `--green` | 5.67:1 |
| `--gold-pale` hover | `--green` | 9.14:1 |
| `#bcb29b` credit | `--green` | 6.13:1 |

### Two things worth knowing

**The cream band is a direct child of `<footer>`, not of `footer > .wrap`.** It
has to run edge to edge, and a `.wrap` would have capped it at 1280px with green
either side. Its own inner `.wrap` centres the content. The markup had to be
lifted out after the first build for exactly this reason.

**The same two traps as the rail footer, caught again:** `.fcol ul` is a grid
with `gap:10px` in `satva.css`, so the gap is set rather than a margin on the
`li`; and the single-column breakpoint started at 420px, which collapsed a 390px
phone and made the footer 1152px. Moved to 360px — 899px now.

### Checked

1440×900 and 390×844: cream band full-bleed at both, four columns on desktop and
two on the phone, 15 links, no horizontal overflow, **zero console errors**.

---

## Recipes ground → #dbd9db (22 Sep 2026)

> "Put this in the website for cook for someone."

Picked from eight tints of the footer's plum `#372e35` shown at `/tints.html`.
`#dbd9db` is that plum mixed **82% toward white** — a true neutral grey, where
the `#fff1e4` it replaces was a warm cream.

### A correction to the comparison page

`tints.html` tested the kicker as `--gold-dk` and warned that this tint would
need it switched to `--band`. **That warning was wrong.** The kicker on this site
has been `--band` all along — the `--gold-dk` in the comparison page was my
assumption, not the live value. Nothing needed switching; it measures 6.23:1 on
the new ground. The four "kicker switched" notes on that page describe a change
that was never required.

### Measured on #dbd9db

| Ink | |
|---|---|
| `--ink` heading | 10.48:1 |
| `--band` kicker and italic line | 6.23:1 |
| `--green` button label | 9.34:1 *(on the button's own face, `#edeced` — white at .5 over the ground)* |

### One thing the change broke, and the fix

The "Ask for a recipe" button's border is `--clay`, chosen for warm grounds. On
this grey it measures **1.07:1** — the outline would have disappeared entirely
and left the label floating. WCAG 1.4.11 asks 3:1 for a control's boundary.

| | |
|---|---|
| `--clay` | 1.07:1 ✗ |
| `--sage-soft` | 3.45:1 |
| **`--sage`** | **4.40:1** ← used |
| `--band` | 6.23:1 — read too heavy beside the italic line |

### Scope

The change is in `css/recipes-seedlip.css`, which **both `index.html` and
`split.html` link**, so both pages now carry the grey.

**Worth knowing for `split.html`:** its cream footer band was chosen precisely
because it matched the recipes cream, so the page would "close in the colour it
has been using". That argument no longer holds — the recipes are grey and the
footer is cream. Either the footer band follows to `#dbd9db`, or that page's
rationale needs restating. Flagged, not decided.

### Checked

Section 744px, still inside one screen, four photographs loading, no horizontal
overflow, **zero console errors**.

---

## The grey on the original site, and one card held back (22 Sep 2026)

### `~/dssatva/site` (port 8000) now carries the grey too

> "i want it in the other site also … one is the original site. the other is
> the sitee where we added green colour footer"

`split.html` already had it — the recipes styling lives in one shared stylesheet,
so it landed there the moment `index.html` got it. The gap was the **original
site**, which is a separate codebase with its own `satva.css`.

**This is the first change to that file since 18 Sep**, when the instruction was
to leave the original alone. Made on the owner's explicit say-so. A timestamped
copy sits beside it as `css/satva.css.bak-1453`, and the change is one contiguous
appended block rather than an edit in place, so reverting is a delete.

**Measured against `#dbd9db` before changing anything** — that site's recipe
labels are `color-mix(acc 62%, --ink)`, tuned for its sage-mist ground:

| | |
|---|---|
| `--ink` heading | 10.48:1 |
| `--band` lede | 6.23:1 |
| all four `.ruses` labels | 5.59 – 6.01:1 |

None needed touching. The only casualty was the same one as on the new site:
`.btn-ghost`'s `--clay` border at **1.07:1**, moved to `--sage` at 4.40:1.

### Coriander Seeds is held back from "Everything"

> "can we take off this corainder seeds card alone in this everything category
> so that i dont have one more left hanging down"

At five columns, twenty-one cards is four full rows **plus one card alone on a
fifth**. Twenty is four clean rows.

It is **not removed from the range**. A new `hideInAll:true` flag on the product
is honoured only by the "Everything" view; tap **Spices** and it is there among
the twelve, with its journey intact.

**The counts had to be made honest.** The subhead was `list.length`, which would
now have read "20 staples, across four shelves" and under-reported what is
actually sold. It counts `PRODUCTS` instead, and **names whatever is held back**
so the number and the cards on screen cannot quietly disagree:

> 21 staples, across four shelves — Coriander Seeds is on the Spices shelf.

The Everything tab still reads **21**, because that is the size of the range.

### Checked

:8003 — Everything: 20 cards, 5 columns, **4 rows, nothing hanging**; Spices: 12
cards with Coriander Seeds present. :8000 — recipes ground `rgb(219,217,219)`,
button border `rgb(78,104,72)`, four recipe cards. **Zero console errors on
both.**

---

## `still.html` — one picture, the sequence behind the button (22 Sep 2026)

> "Keep only one picture in these pictures and make all these visible when we
> click 'How its made' and in a different link and dont change anything in this
> website link, as I want everything here just as it is."

A copy of `index.html` where the product cards **hold a single photograph**
instead of cycling their stages. The whole sequence opens from the button.

| | `index.html` | `still.html` |
|---|---|---|
| Card picture | six stages, cycling | **one, held still** |
| Cycling films in the grid | 20 | **0** |
| Journey | in the card *and* full screen | **full screen only** |
| Button | "See it full screen" | **"How it is made"** |
| Everything else | — | identical |

### Which picture

**The journey's first stage** — the crop in the field — not `p.img`. That matters:
`p.img` exists for only eight of the twenty-one products, so the rest would have
fallen back to the coloured glyph tile. The first stage is a real photograph for
every one of them, and all twenty on the Everything view are **different
pictures** (verified: 20 unique sources, none broken).

### `index.html` was not touched

Re-checked after the change, on the live page: `body class="jrn-card"`, **20
cycling films, 58 slides**, zero still cards, the same subhead, recipes ground
`rgb(219,217,219)`, footer 359px, the same eight stylesheets. Byte-identical in
behaviour.

The whole difference is `<body class="jrn-still">` plus
`css/journey-still.css` **in place of** `css/journey-card.css`, and a `STILL`
branch in `showGroup()` that sits beside the existing `CARDMODE` and `INLINE`
ones. No existing renderer was modified.

### One thing carried over from building the cycling card

`satva.css` positions `.veg` against `.pthumb`, and this card's picture wrapper
is `.still-shot`. The mark arrives unstyled and invisible unless it is
positioned explicitly — the same trap the cycling card hit on 21 Sep, fixed the
same way.

### Checked

20 still cards, 20 unique pictures, none broken, 20 buttons reading "How it is
made". Turmeric's overlay opens with **all eight panels**, seven credits and its
video, Escape closes and cleans up. No horizontal overflow, **zero console
errors** on either page.

### The four pages now

| | |
|---|---|
| `/` | cards cycle their stages |
| `/still.html` | **one picture, sequence on click** |
| `/split.html` | cycling cards, cream-over-green footer |
| `/footers.html` | scratch footer comparison |

---

## Four new hero pictures, and a fifth slide (22 Sep 2026)

> "I like this stunning image of this flax. I want a similar kind of stunning
> pictures with othe slides too based on the topic" … "let the flax be there…
> change the others." … "Also add Satva Saheli as the last slider"

### What made the flax work, written down

A flowering crop running to a treeline under an open sky. Depth, a horizon, and
one colour doing the work. The other three were **close-ups of a single plant**
— no horizon, no sky, no distance — which is why they looked flat beside it.

| Slide | Was | Now |
|---|---|---|
| Spices | one chilli bush, filling the frame | **a mustard field in full yellow flower**, poplars on the horizon |
| Pulses | a stand of pigeon pea foliage | **a pulse crop running green to a treeline**, hills beyond |
| Seeds | the flax | **unchanged, as asked** |
| Healthy Essentials | a path between palms | **coconut palms over open ground**, wide horizon |
| — | — | **Satwa Saheli, new fifth slide** |

Mustard is a spice on that very shelf, so the field is honest as well as the
right shape. The coconut frame was cropped to drop a lone figure standing in it.

### The fifth slide

The tab strip and the rotation are both built from `.shelf` elements and
`data-label`, so the slide joined **without a line of JavaScript**. Five slides,
five tabs, verified.

Copy is the owner's own, cut to the load-bearing half:

> **Empowering Women. Enriching Kitchens.**
> Not a factory supply chain. The women who blend these masalas at home and
> carry them to their own neighbourhoods are trained in FSSAI food safety and
> paid for the work — and each one already reaches thirty families or more.

### The picture on it is a placeholder, and the markup says so

A woman winnowing grain by wind in a village yard — CC BY-SA 4.0 by Subrohit,
credited in the footer. **She is not one of our Sahelis**, and the alt text
describes the work rather than claiming otherwise. Her face is turned away,
which is the only way a photograph of a stranger belongs near this section at
all. A `TO FILL` above it asks for the owner's own photograph, with consent and
a name.

The dark-ink rules written for the first, photograph-less version of this slide
are **kept but unused** — adding `is-saheli` back to the article makes it
readable on its pink ground again if the placeholder is ever pulled before a
real photograph arrives.

### The Saheli section, rewritten from the owner's copy

Five sections of supplied copy came down to what a reader could check: the two
roles (**Satva Maker** / **Satva Promoter**), the FSSAI training, and the 30+
households each Saheli reaches — which replaces one of the three `TO FILL`
figures. The CTA became recruiting ("Apply to become a Saheli"), which is what
that copy is actually for.

**Left out on purpose:** the "movement" and "army of empowered women" language,
which claims more than the figures currently support. The note under the block
now says the programme is running and that the headcount and village are still
to be confirmed, rather than the old blanket "placeholder" disclaimer.

The two roles are a list, not the two boxes of the original — on a phone two
boxes become two stacked cards saying almost the same thing.

### Checked

5 slides, 5 tabs, 5 hero images, **none broken**, footer credit carries both
CC BY pictures, zero console errors.
