#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    """open, read a utf-8 file and print to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
