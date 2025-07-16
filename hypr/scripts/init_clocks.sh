#!/bin/bash

for i in {11..15}; do
    hyprctl dispatch workspace $i 
    # the hyprctl dispatch workspace doesn't do what we want in this case
    hyprctl dispatch exec "foot tty-clock -c"
done
