#!/usr/bin/python3
"""
contain the inherited class
"""


def inherits_from(obj, a_class):
    """return true if the object is an instance of a class that is inherited"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class
