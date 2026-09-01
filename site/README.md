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

## Adding the 4 missing product photos

Four products currently show a designed colour tile with a "Photo coming" pill, because
there is no real photo of them yet. To swap in a real photo, save a **square** image
(680×680 or larger) at exactly this path — nothing else to edit, the page picks it up:

| Product | Save the photo as |
|---|---|
| Kanda Lasun Masala | `assets/p-kandalasun.jpg` |
| Groundnut Chutney | `assets/p-shengdana.jpg` |
| Javas Chutney | `assets/p-javas.jpg` |
| Karala Chutney | `assets/p-karala.jpg` |

Until then the browser console logs a harmless 404 for each missing file. Visitors never
see it.

The other four (`p-haldi`, `p-mirchi`, `p-dhane`, `p-kala`) are real crops of the spice
photograph on the sticker.

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
