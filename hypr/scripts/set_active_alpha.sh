#!/bin/bash

addr=$(hyprctl activewindow | awk '/Window/ {print $2}')
[ -z "$addr" ] && { echo "No active window."; exit 1; }

hyprctl dispatch setprop "address:0x${addr}" alpha "$1"

