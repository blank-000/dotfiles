#!/bin/bash

# if no TARGET is provided, bail out!
if [[ $# -eq 0 ]]; then 
    exit
fi

TARGET=$1

# if we are at the target workspace, bail out!
CURRENT_WORKSPACE=$(hyprctl monitors | awk '/workspace/ {print $3}' | head -n1)
CURRENT_WORKSPACE=$(( $CURRENT_WORKSPACE % 10 ))
if [[ "$TARGET" == "$CURRENT_WORKSPACE"  ]]; then
    exit
fi

# this is to support scrolling when we pass something outside of the range 
# 1 - 5 (in this case) 
# it will go to the opposite value, 
# so if we pass for instance 6 it will switch to workspace 1

WRAP_AROUND_AT=5 # change to how many workspaces you want to have

if (( TARGET > WRAP_AROUND_AT )); then
    TARGET=1
elif (( TARGET < 1 )); then
    TARGET=$WRAP_AROUND_AT
fi

# count how many monitors are present
MONITOR_COUNT=$(hyprctl monitors | grep '^Monitor' | wc -l)

# Global workspaces get encoded as a two-digit number:
# the monitor ID and the Global Workspace
# 
# except when there is a zero in the tens place 
# 
# This is an example mapping, of a four monitor setup
# ┌──────────────┬──────────────────────┬───────────────────────┐
# │ Monitor      │ GWorkspace->"TARGET" │ Hyprland Workspace ID │
# ├──────────────┼──────────────────────┼───────────────────────┤
# │     0        │         1            │           1           │
# │     1        │         1            │          11           │
# │     2        │         1            │          21           │
# │     3        │         1            │          31           │
# ├──────────────┼──────────────────────┼───────────────────────┤
# │     0        │         2            │           2           │
# │     1        │         2            │          12           │
# │     2        │         2            │          22           │
# │     3        │         2            │          32           │
# └──────────────┴──────────────────────┴───────────────────────┘


for ((i = $(( MONITOR_COUNT-1)); i >= 0; i--)) ; do
    workspace=$(( TARGET + i * 10))
    hyprctl --batch "dispatch focusmonitor $i; dispatch workspace $workspace"
done

# change wallpaper
${XDG_CONFIG_HOME:-${HOME}/.config}/hypr/scripts/set_wallpaper.sh "$TARGET"
