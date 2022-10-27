#!/usr/bin/python3
""""
function that returns dictionary description
"""


def class_to_json(obj):
    """returns dictionary description with simple data structure"""
    return obj.__dict__
