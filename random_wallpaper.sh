#!/bin/bash
DIR="animated-wallpapers-dirctory"
killall mpv
sleep 0.3
# Select a random file from the directory
RAND_FILE="$(find "$DIR" -maxdepth 1 -type f -name '*.mp4' | shuf -n 1)"
echo "Random file selected: $RAND_FILE"

# Replace .mp4 with .jpeg for the thumbnail
BASENAME="$(basename "$RAND_FILE" .mp4).jpg"

# Launch xwinwrap with mpv playing the selected video
xwinwrap -g 1920x1280 -s -b -fs -st -sp -nf -ov -fdt -- mpv -wid WID --really-quiet --framedrop=vo --no-audio --loop --panscan="1.0" --no-osc "$RAND_FILE" > /dev/null 2>&1 &

# Set the wallpaper to the corresponding thumbnail image
wal -i "$DIR/thumpnails/$BASENAME"> /dev/null 2>&1
echo "Wallpaper set to $DIR/thumpnails/$BASENAME"
