# DS Satva website — go-live record

Recorded 23 Oct 2026. The site is live at **https://dssatva.com**.

## Domain
| Item | Value |
|---|---|
| Domain | dssatva.com |
| Registrar | Cloudflare Registrar (account: dssatva@gmail.com, two-step login with Google Authenticator) |
| Registered | 22 Oct 2026 |
| Expires | 22 Oct 2027, auto-renew ON |
| Owner on record | DS Satva Foods Pvt. Ltd. (WHOIS privacy on) |
| Nameservers | adaline.ns.cloudflare.com, jonah.ns.cloudflare.com |
| Not bought | dssatva.in (optional later; Cloudflare doesn't sell .in) |

## DNS (Cloudflare → dssatva.com → DNS → Records), all "DNS only" (grey cloud)
| Type | Name | Content |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | dssatva.github.io |

The cloud must stay grey. Orange (proxied) breaks GitHub's HTTPS certificate.

## Hosting
| Item | Value |
|---|---|
| Host | GitHub Pages, free |
| Repository | github.com/dssatva/satva-site (public), branch `main`, folder `/` |
| Custom domain | dssatva.com (file `CNAME` in the repo) |
| HTTPS | Let's Encrypt certificate via GitHub, issued 22 Oct 2026, renews by itself; Enforce HTTPS ON |
| GitHub account | dssatva (login dssatva@gmail.com) |

## How a change goes live
1. Edit the working copy `~/dssatva/ports/8002` (preview http://127.0.0.1:8002; styles/scripts/pictures live in `~/dssatva/site-v3`).
2. Check it at 1245×657 (desktop, one section per screen) and at 390 / 360 px (phone).
3. Copy the changed files into `~/satva-live` (clean copy: no backups, no review pages, compressed photos).
4. Bump the `?v=` tag on css/js links in index.html so phones load the new files.
5. In `~/satva-live`: `git add -A`, `git commit`, `git pull --rebase origin main`, `git push origin main` (gh logged in as **dssatva**).
6. Live in 1–2 minutes. Every version is kept in GitHub, so any change can be undone.

## Timeline
| Date | What happened |
|---|---|
| 3 Sep 2026 | Domain study (.in vs .com) — `Domain-Setup-in-vs-com.md` |
| 6 Sep – 20 Oct 2026 | Website designed and refined on the :8002 working copy |
| 22 Oct 2026 | dssatva.com bought on Cloudflare; GitHub repo dssatva/satva-site created; site uploaded (102 MB → 54 MB clean copy); DNS records added; GitHub Pages switched on; certificate approved; HTTPS enforced |
| 22 Oct 2026 | Changes published: How it's made moved last in Why SATVA menu; Saheli "Connect with us to become a Satva Saheli" pop-up; Grocery Kit slide title, "kitchen essentials", footer-green button |
| 22–23 Oct 2026 | Phone fixes published: Saheli story pop-up one column with full photo; no blank gap under hero slides; How it's made card fits; Why SATVA arches 2×2; kit pouch shown on phones; version tags on css/js |

## Content decisions recorded on the site
- No numbers in counts or step markers across the site (kept: phone, pack sizes, recipe steps, factual claims).
- No Hindi words on the hero slides.
- Quinoa removed everywhere; Coriander Seeds on the Seeds shelf.
- WhatsApp / phone everywhere: +91-9689888822.
- Monk fruit: "zero glycemic index".
- Chilli Powder card opens four varieties: Teja, 341 (owner's photos), Byadgi, Kashmiri; same four in Customise your kit.

## Done on 23 Oct 2026
- Speed: WebP copies of every photo; phone first load ~10 MB → ~6 MB (`~/dssatva/publish-live.py` builds the live copy).
- Footer: FSSAI Lic. No. 21526044005691 · GSTIN 27AANCD0378A1ZT; full address Plot No. 31W, MIDC Chikalthana, Chhatrapati Sambhajinagar, Maharashtra 431001.
- Privacy policy at https://dssatva.com/privacy.html (PDF: DS-Satva-Privacy-Policy.pdf).
- Search: noindex removed; canonical, sharing (OG/Twitter) tags, business details (LocalBusiness), robots.txt, sitemap.xml, 404 page, icons.
- Google Search Console (account dssatva@gmail.com): domain verified through Cloudflare, sitemap processed (4 pages), home page indexed, indexing requested.
- Products: Chatpat Masala renamed "Chatpat / Kanda Lasun Masala"; Meat Masala replaced by Chaat Masala.

## Pending — waiting on the client
| # | Step | Question for the client |
|---|---|---|
| 5 | Google Business Profile (Google Maps) | Can customers walk in at Plot No. 31W, MIDC Chikalthana (show address on Maps), or delivery only (hide address, list service area)? Which phone gets Google's verification code? Opening hours? 3–5 photos? |
| 6 | Visitor count (Cloudflare Web Analytics, free, no cookie banner) | OK to add? Who should see the numbers? |
| 7 | Business email hello@dssatva.com (free forwarding to dssatva@gmail.com via Cloudflare Email Routing) | Which address name (hello@ / orders@ / info@)? Forward to which inbox? |

Also: change the dssatva GitHub password (typed in chat on 22 Oct) and turn on GitHub two-step login. dssatva.in redirect if wanted.

## Where everything is kept
| What | Where |
|---|---|
| Live site files | github.com/dssatva/satva-site |
| Website + design work (working copy, site-v3, stickers, packaging) | github.com/Ruth-Jasmine/ds-satva, branch `dssatva2` (private) |
| Business research, plans, surveys, logos, print stickers | github.com/Ruth-Jasmine/ds-satva-business (private) |
