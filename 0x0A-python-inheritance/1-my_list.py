#!/usr/bin/python3
"""
Inheritance
"""

class MyList(list):
    """Derived class of list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """print the list"""
        print(sorted(self))
