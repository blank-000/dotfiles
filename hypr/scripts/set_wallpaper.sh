#!/bin/bash

one=${HOME}/Pictures/Wallpapers/bear_colors/one.png
two=${HOME}/Pictures/Wallpapers/bear_colors/two.png
three=${HOME}/Pictures/Wallpapers/bear_colors/three.png
four=${HOME}/Pictures/Wallpapers/bear_colors/four.png
five=${HOME}/Pictures/Wallpapers/bear_colors/five.png
ratio_one=${HOME}/Pictures/Wallpapers/bear_colors/one_1610.png
ratio_two=${HOME}/Pictures/Wallpapers/bear_colors/two_1610.png
ratio_three=${HOME}/Pictures/Wallpapers/bear_colors/three_1610.png
ratio_four=${HOME}/Pictures/Wallpapers/bear_colors/four_1610.png
ratio_five=${HOME}/Pictures/Wallpapers/bear_colors/five_1610.png

case "$1" in
1)
    selected="$one"
    ratio="$ratio_one" ;;
2)
    selected="$two"
    ratio="$ratio_two" ;;
3)
    selected="$three"
    ratio="$ratio_three" ;;
4)
    selected="$four"
    ratio="$ratio_four" ;;
5)
    selected="$five"
    ratio="$ratio_five" ;;
*)
    selected="$one"
    ratio="$ratio_one" ;;
esac

hyprctl hyprpaper wallpaper "HDMI-A-1,$selected"
hyprctl hyprpaper wallpaper "eDP-1,$ratio"
