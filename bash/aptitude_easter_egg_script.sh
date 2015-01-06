#!/bin/bash
i=0
vees='-v'
for i in {1..6..1}
do
    echo "aptitude $vees moo"
    aptitude $vees moo
    vees="${vees}v"
done

