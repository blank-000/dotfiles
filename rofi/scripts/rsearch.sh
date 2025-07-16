#!/bin/bash
input="$(printf '\n' | rofi -dmenu -l 1 -p 'run/search ::')"

#input="$(rofi -dmenu -l 1 -p 'run')"
[ -z "$input" ] && exit

if command -v "$input" >/dev/null 2>&1; then
    exec "$input"
else
    xdg-open "https://search.brave.com/search?q=$(printf '%s' "$input" | jq -sRr @uri)" >/dev/null 2>&1 &
fi

