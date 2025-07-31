#!/bin/bash

one=${HOME}/Pictures/Wallpapers/bear_colors/one.png
two=${HOME}/Pictures/Wallpapers/bear_colors/two.png
three=${HOME}/Pictures/Wallpapers/bear_colors/three.png
four=${HOME}/Pictures/Wallpapers/bear_colors/four.png
five=${HOME}/Pictures/Wallpapers/bear_colors/five.png

case "$1" in
1) selected="$one" ;;
2) selected="$two" ;;
3) selected="$three" ;;
4) selected="$four" ;;
5) selected="$five" ;;
*) selected="$one" ;;
esac

hyprctl hyprpaper wallpaper ",$selected"
