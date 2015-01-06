#!/bin/bash
echo "don't clear this"
while [ 1 -eq 1 ] ; do
    printf "$(date +%T)"
    sleep 1
    printf "\b\b\b\b\b\b\b\b"
done

