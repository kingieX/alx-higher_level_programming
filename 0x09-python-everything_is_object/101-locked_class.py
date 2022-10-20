#!/usr/bin/python3
class LockedClass:
    """A locked class with no class or object attribute, that only lets the user dynamically create new instance
   except if the new instance attribute is called 'first_name'"""

    __slots__ = ['first_name']
