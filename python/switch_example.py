#!/usr/bin/env python

def a(s):
    print s
def switch(ch):
    try:
       {'1': lambda : a("one"),
        '2': lambda : a("two"),
        '3': lambda : a("three"),
        'a': lambda : a("Letter a")
       }[ch]()
    except KeyError:
        a("Key not found")
 
switch('1')
switch('a')
switch('b')
