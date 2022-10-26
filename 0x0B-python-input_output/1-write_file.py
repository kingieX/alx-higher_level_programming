#!/usr/bin/python3
"""
function that writes to a text file
"""


def write_file(filename="", text=""):
    """write to a utf-8 file and return number of characters"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
