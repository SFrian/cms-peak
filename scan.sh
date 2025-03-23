#!/bin/bash
while read url; do
    echo "Scanning $url"
    printf "y\n" | cmseek -u "$url"
done < targets.txt
