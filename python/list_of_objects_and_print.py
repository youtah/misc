#!/usr/bin/env python
 
def main():
 
    x = 0
    y = 10
    list_of_things = []
 
    while x < y:
        tmp = thingy(x)
        #print "created thing object "+str(x)
        x = x + 1
        list_of_things.append(tmp)
        #print "added object to list"
 
    print "Printing List"
    for i in list_of_things:
        print str(i.num)
        if i.num == 5:
            i.num = 99
   
    print "Printing Modified List"
    for i in list_of_things:
        print str(i.num)
 
class thingy:
    def __init__(self, num):
        self.num = int(num)
 
    def __str__(self):
        return str(vars(self))
 
if __name__ == "__main__":
    main()
