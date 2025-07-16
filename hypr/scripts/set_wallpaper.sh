#!/bin/bash

one=/home/bear/Pictures/Wallpapers/bear_colors/bear_green.png
two=/home/bear/Pictures/Wallpapers/bear_colors/bear_yellow.png
three=/home/bear/Pictures/Wallpapers/bear_colors/bear_aqua.png
four=/home/bear/Pictures/Wallpapers/bear_colors/bear_orange.png
five=/home/bear/Pictures/Wallpapers/bear_colors/bear_red.png

case "$1" in
    1) selected="$one" ;;
    2) selected="$two" ;;
    3) selected="$three" ;;
    4) selected="$four" ;;
    5) selected="$five" ;;
    *) selected="$one" ;;
esac

hyprctl hyprpaper wallpaper ",$selected"
