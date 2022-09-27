#!/usr/bin/python3
def no_c(my_string):
    new_s = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            new_s += c
    return new_s
