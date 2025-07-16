#!/bin/bash

for node in $(wpctl status | grep -i 'vol:' | awk '{for(i=1;i<=NF;i++) if ($i ~ /^[0-9]+\.$/) print $i}' | tr -d '.');do 
    wpctl set-volume "$node" 5%"$1" 
done

dunstify -h int:value:$(( $(wpctl get-volume @DEFAULT_SINK@ | awk '{print int($2 * 100)}') )) ""
