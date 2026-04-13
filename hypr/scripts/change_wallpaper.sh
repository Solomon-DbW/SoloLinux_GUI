#!/bin/bash
image=$(find "$HOME/.config/hypr/wallpapers" -type f | shuf -n 1)
awww img "$image"
