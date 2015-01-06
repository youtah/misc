#!/bin/bash
 
x=$1
if [ $x -ge 0 ]; then
    for (( c=1; c<=$x; c++ ))
    do
        printf "${c} seconds have passed."
        sleep 1
        printf "\r"
    done
else
    echo "Please enter an integer > 0"
fi
