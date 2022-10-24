#!/usr/bin/python3
"""
contain the inherited class
"""


def inherits_from(obj, a_class):
    """true if obj is an instance of a class that is inherited, else false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
