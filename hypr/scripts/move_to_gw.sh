#!/bin/bash

TARGET=$1
current=$(hyprctl activewindow | awk '/workspace/ {print $2}')

if [ "$current" -gt 10 ]; then
    TARGET=$((TARGET + 10))
fi
# we use the silent option which doesn't switch to the workspace in order to 
# preserve the global workspace bindings
# this feels fragile, but works for now
hyprctl dispatch movetoworkspacesilent "$TARGET"

