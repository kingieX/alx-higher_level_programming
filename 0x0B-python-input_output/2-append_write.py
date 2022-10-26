#!/usr/bin/python3
"""
append a string at the end a text file
"""


def append_write(filename="", text=""):
    """append to a utf-8 file and return number of characters"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
