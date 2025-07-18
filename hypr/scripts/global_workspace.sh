#!/bin/bash

# if no TARGET is provided, bail out!
if [ $# -eq 0 ]; then
    exit
fi

TARGET=$1
MAX_WORKSPACE=${2:-5}


# Wrap-around for 1 to MAX_WORKSPACE
if (( TARGET > MAX_WORKSPACE )); then
    TARGET=1
elif (( TARGET < 1 )); then
    TARGET=$MAX_WORKSPACE
fi

MONITOR_COUNT=$(hyprctl monitors | grep '^Monitor' | wc -l)

for ((i = $(( MONITOR_COUNT-1)); i >= 0; i--)) ; do
    workspace=$(( TARGET + i * 10))
    hyprctl dispatch focusmonitor "$i"
    hyprctl dispatch workspace "$workspace"
done

# change wallpaper
${XDG_CONFIG_HOME:-${HOME}/.config}/hypr/scripts/set_wallpaper.sh "$TARGET"
