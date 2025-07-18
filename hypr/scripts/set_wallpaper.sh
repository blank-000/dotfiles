#!/bin/bash

one=${HOME}/Pictures/Wallpapers/bear_colors/bear_green.png
two=${HOME}/Pictures/Wallpapers/bear_colors/bear_yellow.png
three=${HOME}/Pictures/Wallpapers/bear_colors/bear_aqua.png
four=${HOME}/Pictures/Wallpapers/bear_colors/bear_orange.png
five=${HOME}/Pictures/Wallpapers/bear_colors/bear_red.png

case "$1" in
    1) selected="$one" ;;
    2) selected="$two" ;;
    3) selected="$three" ;;
    4) selected="$four" ;;
    5) selected="$five" ;;
    *) selected="$one" ;;
esac

hyprctl hyprpaper wallpaper ",$selected"
