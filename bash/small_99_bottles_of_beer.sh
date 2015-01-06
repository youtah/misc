#!/bin/bash
BOTTLES=99
while [ $BOTTLES -gt 0 ]; do
    echo $BOTTLES" bottles of beer on the wall"
    sleep 1.5
    echo $BOTTLES" bottles of beer"
    sleep 2
    echo "take one down, put it back up..."
    sleep 1.5
    echo -e $BOTTLES" bottles of beer on the wall!\n"
    sleep 3
done

