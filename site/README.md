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
**Tiro Devanagari Marathi** (the Marathi names).

## Product photos

The range is listed in `PRODUCTS` at the top of `js/satva.js`. A card shows a real
photo if the file at its `img` path exists, and a designed colour tile with a
"Photo coming" pill if it does not — so adding a photo is a file drop, no code edit.
Save a **square** image, 680x680 or larger.

Already photographed (real crops of the spice photo on the label):

| Product | File | Note |
|---|---|---|
| Turmeric | `assets/p-haldi.jpg` | the actual spice |
| Chilli Powder | `assets/p-mirchi.jpg` | the actual spice |
| Coriander Powder | `assets/p-dhane.jpg` | the actual spice |
| Garam Masala | `assets/p-garam.jpg` | a ground brown masala - representative, not a shot of our own pack |
| Biryani Masala | `assets/p-biryani.jpg` | whole cardamom and cinnamon - the ingredients, not the ground blend |

Replace those last two first when you have real pack shots.

Still needed:

| Product | Save the photo as |
|---|---|
| Kanda Lasun Masala | `assets/p-kandalasun.jpg` |
| Meat Masala | `assets/p-meat.jpg` |
| Pav Bhaji Masala | `assets/p-pavbhaji.jpg` |
| Chaat Masala | `assets/p-chaat.jpg` |
| Chatpat Masala | `assets/p-chatpat.jpg` |

Until then the browser console logs a harmless 404 for each missing file. Visitors
never see it.

## Adding another masala

The range is not fixed at any number. Everything on the page that lists products —
the cards, and the spice-colour rule above the pillars and above the footer — is
generated from the single `PRODUCTS` array at the top of `js/satva.js`. Add an entry
and both update:

```js
{ acc:"var(--turmeric)", ink:"#9a6b06", mr:"<Marathi name>", en:"<English name>",
  glyph:"<first Devanagari letter or two>",
  d:"<one line about how it is used>",
  img:"assets/p-<id>.jpg",
  tint:"linear-gradient(150deg,#<light>,#<darker>)" }
```

- `acc` is the bright spice colour (the card's colour bar, the rule segment, the
  hover border). Reuse one of the tokens in `satva.css` or add a new one.
- `ink` is a darkened version of the same hue, used for the Marathi name so it stays
  legible on white. Keep it at 4.5:1 or better against `#fff`.
- `tint` is only used until a real photo exists at `img`.

No copy anywhere says how many masalas there are, so nothing goes stale.

## The two places only you can fill in

**A personal memory in Our Story.** Everything in that section is true of the venture
as it stands - nothing is invented, and there is deliberately no made-up grandmother
or childhood scene in it. The one thing that would make it unanswerable is a real,
specific memory: a particular kitchen, a particular person, a particular afternoon.
Drop it in as a second `<p>` in the story column and the whole section lifts. There is
a `TO FILL` comment marking the spot.

**Real tester quotes.** The "three questions we actually ask" section currently shows
the questions, plus one dashed card saying real answers are coming. As feedback lands
in the Responses sheet, replace the dashed card with actual quotes - `.vcard` blocks.
Keep the unflattering ones; they are the reason anyone will believe the good ones.

## Where the story's facts come from

The claims in Our Story are drawn from `../India-Masala-Consumption-Research.md`:
loose and unbranded spice is roughly 60% of the Indian market by value (hence "six
rupees in every ten"), and the April 2024 ethylene-oxide episode - recalls in Hong
Kong and Singapore, FSSAI running nationwide checks - is a matter of public record.
If you change those lines, keep them checkable.


## Still to fill in

- **FSSAI licence number** — there is a marked comment in the footer of `index.html`.
- **Pack sizes and prices** — deliberately not on the page; every product says
  "Ask price on WhatsApp" instead.
- **Instagram / Google Business links** — not added yet.

## Regenerating the image assets

Every file in `assets/` was cut from `~/Downloads/DS_STICKER.pdf`: the logo is keyed out
of a 600 dpi vector render, the photos are crops of the embedded spice photograph, and
`leaf-mask.png` is the label's leaf watermark turned into a CSS mask (the mask must keep
its **alpha** channel — a plain greyscale PNG renders as a solid block).
