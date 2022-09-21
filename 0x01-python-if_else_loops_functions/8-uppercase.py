#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(str) <= ord('z'):
            c = chr(ord(c) - (ord('a') - ord('A')))
        print("{:s}".format(c), end='')
    print("")
