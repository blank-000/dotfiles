#!/bin/bash

# if no target is provided, bail out!
if [ $# -eq 0 ]; then
    exit
fi

target=$1

# Wrap-around for 1 to maxWorkspace
if (( target > 5 )); then
    target=1
elif (( target < 1 )); then
    target=5
fi
# Get monitor names
main=$(hyprctl monitors | awk '/ID 0/ {print $2}')
secondary=$(hyprctl monitors | awk '/ID 1/ {print $2}')

# Create a paired workspace for the workspaces [ 1 - 9 -> 11 - 19 ]
paired_workspace=$(( "$target" + 10 ))

# switch the secondary monitor's workspace to the paired number
hyprctl dispatch focusmonitor "$secondary"
hyprctl dispatch workspace "$paired_workspace"

# switch the main monitor to the original target
hyprctl dispatch focusmonitor "$main"
hyprctl dispatch workspace "$target"

/home/bear/.config/hypr/scripts/set_wallpaper.sh "$target"
