#!/usr/bin/env python
import math as m
import sys
 
def main(argv):
    # Creating two lists as points
    # Example args for Salt Lake to Miami would be:
    # 40.7665 -111.912 25.81708 -80.12088
    # As the args, with 25.81708, -80.12088 being for Miami
    # and 40.7665 -111.912 being for Salt Lake City.
    
    pointa = [float(argv[1]), float(argv[2])]
    pointb = [float(argv[3]), float(argv[4])]

    print distance(pointa, pointb)
 
#To calculate the distance between two points (lat & long) - result is in miles (as the crow flies.)
def distance(p1, p2):
    d = m.acos(m.cos(m.radians(90-p1[0]))*\
        m.cos(m.radians(90-p2[0]))+\
        m.sin(m.radians(90-p1[0]))*\
        m.sin(m.radians(90-p2[0]))*\
        m.cos(m.radians(p1[1]-p2[1])))*\
        3958.756
    return d
 
if __name__ == "__main__":
    main(sys.argv)
