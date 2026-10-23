#!/bin/sh
# Screenshots each picture on social-profile-pics.html to social-profile-pics/NN.png (1080x1080).
# Needs the :8002 server running. 21 Oct 2026.
cd "$(dirname "$0")"
for n in $(seq 1 15); do
  google-chrome --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
    --window-size=1080,1080 --virtual-time-budget=6000 \
    --screenshot="$PWD/social-profile-pics/$(printf %02d $n).png" \
    "http://localhost:8002/social-profile-pics.html?only=$n" 2>/dev/null
done
