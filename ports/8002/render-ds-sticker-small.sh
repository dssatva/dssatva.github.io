#!/bin/sh
# Renders ds-sticker-small.html to ds-sticker-small/NN.png at 2x, transparent outside the die-cut.
# Needs the :8002 server. 21 Oct 2026.
cd "$(dirname "$0")"; mkdir -p ds-sticker-small
set -- 900,900 900,900 1200,720 780,1000 1200,640
n=1; for s in "$@"; do
  google-chrome --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --default-background-color=00000000 --window-size=$s --virtual-time-budget=8000 \
    --screenshot="$PWD/ds-sticker-small/0$n.png" "http://localhost:8002/ds-sticker-small.html?only=$n" 2>/dev/null
  n=$((n+1)); done
