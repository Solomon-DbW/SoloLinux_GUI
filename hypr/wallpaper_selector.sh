#!/usr/bin/env bash

WALLPAPER_DIR="$HOME/.config/hypr/wallpapers"
HYPR_WP_SCRIPT="$HOME/.config/hypr/set_wallpaper.sh"

# Check dependencies
if ! command -v yad &>/dev/null; then
    echo "yad not installed. Install with: sudo pacman -S yad"
    exit 1
fi

if ! command -v swww &>/dev/null; then
    echo "swww not installed. Install with: sudo pacman -S swww"
    exit 1
fi

# Create a temporary list of wallpapers
TMPFILE=$(mktemp)
for img in "$WALLPAPER_DIR"/*.{jpg,jpeg,png,webp}; do
    [ -f "$img" ] && echo "$img" >> "$TMPFILE"
done

# Open YAD image grid
SELECTED=$(yad --title="Select Wallpaper" \
    --window-icon=preferences-desktop-wallpaper \
    --width=400 --height=400 \
    --image-on-top \
    --iconsize=200 \
    --text="Choose a wallpaper:" \
    --list --column="Preview:IMG" --column="File:TEXT" \
    $(while read -r img; do echo "$img" "$img"; done < "$TMPFILE") \
    --print-column=2 \
    --separator="")

# If a wallpaper was selected, set it using swww
if [ -n "$SELECTED" ]; then
    swww img "$SELECTED" --transition-type any
fi

rm "$TMPFILE"

