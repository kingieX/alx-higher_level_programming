#!/usr/bin/python3
#program that prints the ASCII alphabet in lowercase.
for a in range(ord('a'), ord('z') + 1):
    print("{:c}".format(a), end = " ")
