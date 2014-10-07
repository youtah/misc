
#!/usr/bin/env python
import math as m
 
def main():
    # Creating two lists as points
    saltlake = [40.7665, -111.912]
    miamihotel = [25.81708, -80.12088]
 
    print distance(miamihotel,saltlake)
 
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
    main()
