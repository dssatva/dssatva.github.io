#!/bin/sh
# Renders ds-sticker-v3.html to ds-sticker-v3/NN.png at 2160x2160 (2x, print);
# 09-12 are round with transparent corners. Needs the :8002 server. 21 Oct 2026.
cd "$(dirname "$0")"; mkdir -p ds-sticker-v3
for n in $(seq 1 26); do
  google-chrome --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --default-background-color=00000000 --window-size=1080,1080 --virtual-time-budget=8000 \
    --screenshot="$PWD/ds-sticker-v3/$(printf %02d $n).png" "http://localhost:8002/ds-sticker-v3.html?only=$n" 2>/dev/null
done
