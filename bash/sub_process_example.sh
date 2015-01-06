#!/bin/sh
itr=$1
 
for (( i=1; i<=$itr; i++ ))
do
    printf "\rSeconds passed: $i"
    sleep 1
done
printf "\n"

