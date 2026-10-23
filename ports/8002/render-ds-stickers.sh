#!/bin/sh
# Renders ds-sticker-variations.html stickers to ds-sticker-variations/NN.png at 2160x2160
# (2x, for print). Needs the :8002 server. #8 is round, so its corners are transparent. 21 Oct 2026.
cd "$(dirname "$0")"; mkdir -p ds-sticker-variations
for n in $(seq 1 10); do
  google-chrome --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --default-background-color=00000000 --window-size=1080,1080 --virtual-time-budget=8000 \
    --screenshot="$PWD/ds-sticker-variations/$(printf %02d $n).png" "http://localhost:8002/ds-sticker-variations.html?only=$n" 2>/dev/null
done
