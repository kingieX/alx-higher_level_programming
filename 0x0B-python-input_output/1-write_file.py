#!/usr/bin/python3
"""
function that writes to a text file
"""


def read_file(filename=""):
    """write to a utf-8 file and return num of characters"""
    with open(filename, "r", encoding="utf-8") as f:
        num = 0
        for line in f:
            num += 1
        return num
