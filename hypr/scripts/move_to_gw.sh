#!/bin/bash

TARGET=$1


# Global workspaces are encoded as a two-digit number:
#
#   [ tens ][ units ]
#     │        │
#     │        └─── Global workspace index (1–9)
#     └──────────── Monitor index (0 = primary, 1 = secondary, etc.)
#
# So we extract the monitor index from CURRENT_WORKSPACE (tens digit),
# and replace the global index (units digit) with TARGET.

CURRENT_WORKSPACE=$(hyprctl activewindow | awk '/workspace/ {print $2}')
MONITOR_INDEX=$(( CURRENT_WORKSPACE / 10 * 10 ))
COMBINED_INDEX=$(( MONITOR_INDEX + TARGET ))

hyprctl dispatch movetoworkspacesilent "$COMBINED_INDEX"
