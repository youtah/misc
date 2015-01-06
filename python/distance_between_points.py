#!/usr/bin/env python
from math import sqrt
 
def distance(p1, p2):
    return sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
 
p1 = [1, 4]
p2 = [4, 0]
 
print distance(p1,p2)

