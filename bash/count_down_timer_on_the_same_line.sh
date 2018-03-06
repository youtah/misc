#!/bin/bash

# Below is an example of a simple bash countdown timer that keeps everything on the same line
# Please note the \r actually only moves the cursor to the beginning of the line

COUNTER=20

while [ $COUNTER -gt 0 ]; do
    sleep 1
    # -e handles the \'s and the \n removes tailing newline
    echo -en "\rStarting in: $COUNTER      "
    let COUNTER=COUNTER-1
done

#optional
echo -en "                                 \n"

exit 0
