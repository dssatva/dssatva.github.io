#!/usr/bin/env python3
"""Build the live copy of dssatva.com from the working copy.  23 Oct 2026.

  ~/dssatva/ports/8002  (working copy, css/js/assets symlinked into site-v3)
      -> ~/satva-live    (git repo dssatva/satva-site, served by GitHub Pages)

Steps: copy pages + css + js (real files, no symlinks), copy only the pictures
the pages/scripts actually use, drop backups, shrink big photos, add a WebP copy
of every photo and point the pages/scripts at it, stamp a fresh ?v= on css/js
links so phones reload them. Originals stay beside the WebP files, so anything
the rewrite misses still loads.

Usage:  python3 ~/dssatva/publish-live.py      then commit + push in ~/satva-live
"""
import os, re, shutil, time
from PIL import Image

SRC = os.path.expanduser("~/dssatva/ports/8002")
OUT = os.path.expanduser("~/satva-live")
PAGES = ["index.html", "saheli.html", "credits.html", "privacy.html", "404.html", "robots.txt",
         "sitemap.xml", "site.webmanifest", "favicon.ico"]
# must stay JPG/PNG: share previews, home-screen icons, logo named in search data
KEEP_FORMAT = {"og-dssatva.jpg", "apple-touch-icon.png", "icon-192.png", "icon-512.png",
               "logo-stack-dark.png", "mark-dark.png"}
BACKUP = re.compile(r"\.bak|\.fixed-fit-")

def copy_tree(sub):
    d = os.path.join(OUT, sub)
    os.makedirs(d, exist_ok=True)
    for f in os.listdir(os.path.join(SRC, sub)):
        if BACKUP.search(f):
            continue
        s = os.path.join(SRC, sub, f)
        if os.path.isfile(s):
            shutil.copy2(os.path.realpath(s), os.path.join(d, f))

def main():
    for f in PAGES:
        if os.path.exists(os.path.join(SRC, f)):
            shutil.copy2(os.path.join(SRC, f), os.path.join(OUT, f))
    copy_tree("css"); copy_tree("js")

    # pictures referenced by the pages or scripts (by name, or by the part after a prefix)
    text = ""
    for root in (OUT, os.path.join(OUT, "css"), os.path.join(OUT, "js")):
        for f in os.listdir(root):
            if f.endswith((".html", ".css", ".js", ".webmanifest")):
                text += open(os.path.join(root, f), encoding="utf-8", errors="ignore").read()
    src_assets = os.path.join(SRC, "assets"); out_assets = os.path.join(OUT, "assets")
    os.makedirs(out_assets, exist_ok=True)
    for f in os.listdir(src_assets):
        if BACKUP.search(f) or f.startswith("."):
            continue
        stem = os.path.splitext(f)[0]
        names = {f, stem}
        m = re.match(r"^(rec|recipe|u|j|p|cv|cg|cat|proc|sah-hero|mas-hero)-(.+)$", stem)
        if m:
            names.add(m.group(2))
        if any(n in text for n in names):
            s = os.path.realpath(os.path.join(src_assets, f))
            if os.path.isfile(s):
                o = os.path.join(out_assets, f)
                if not os.path.exists(o) or os.path.getmtime(s) > os.path.getmtime(o):
                    shutil.copy2(s, o)

    # shrink and make WebP copies
    converted = set()
    for f in os.listdir(out_assets):
        p = os.path.join(out_assets, f)
        low = f.lower()
        if not low.endswith((".jpg", ".jpeg", ".png")):
            continue
        if low.endswith((".jpg", ".jpeg")) and os.path.getsize(p) > 260_000 and f not in KEEP_FORMAT:
            im = Image.open(p); im.thumbnail((1600, 1600))
            im.convert("RGB").save(p, quality=76, optimize=True, progressive=True)
        if f in KEEP_FORMAT:
            continue
        w = os.path.splitext(p)[0] + ".webp"
        if not os.path.exists(w) or os.path.getmtime(w) < os.path.getmtime(p):
            im = Image.open(p); im.thumbnail((1600, 1600))
            if im.mode in ("RGBA", "LA", "P"):
                im.convert("RGBA").save(w, "WEBP", quality=80, method=6)
            else:
                im.convert("RGB").save(w, "WEBP", quality=74, method=6)
        converted.add(f)

    # point pages and scripts at the WebP copies
    stamp = time.strftime("%Y%m%d%H%M")
    for root in (OUT, os.path.join(OUT, "css"), os.path.join(OUT, "js")):
        for f in os.listdir(root):
            if not f.endswith((".html", ".css", ".js")):
                continue
            p = os.path.join(root, f); s = open(p, encoding="utf-8").read(); o = s
            for name in converted:
                stem, ext = os.path.splitext(name)
                s = re.sub(r"(?<![\w.-])" + re.escape(name) + r"(?![\w])", stem + ".webp", s)
            # names built in scripts: "assets/rec-" + id + ".jpg"
            if f.endswith(".js"):
                s = re.sub(r'(\+\s*)"\.jpg"', r'\1".webp"', s)
            if f.endswith(".html"):
                s = re.sub(r'((?:href|src)="(?:css|js)/[^"?]+\.(?:css|js))(?:\?v=[0-9a-z]+)?"', r'\1?v=' + stamp + '"', s)
            if s != o:
                open(p, "w", encoding="utf-8").write(s)
    print("pictures:", len(os.listdir(out_assets)), "webp made for", len(converted), "| version", stamp)

if __name__ == "__main__":
    main()
