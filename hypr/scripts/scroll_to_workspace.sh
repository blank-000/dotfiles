#!/bin/bash

# Check if argument is +1 or -1, else exit
if [[ "$1" != "+1" && "$1" != "-1" ]]; then
    echo "Invalid argument. Use +1 or -1."
    exit 1
fi

# Get current workspace number
CURRENT_WORKSPACE=$(hyprctl monitors | awk '/active workspace/ {print $3}' | head -n1)

# Calculate new workspace
NEW_WORKSPACE=$(( CURRENT_WORKSPACE + $1 ))

# Call global workspace script with new workspace number
${XDG_CONFIG_HOME:-${HOME}/.config}/hypr/scripts/global_workspace.sh "$NEW_WORKSPACE"

