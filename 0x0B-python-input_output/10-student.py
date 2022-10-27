#!/usr/bin/python3
"""
class that defines a student
"""


class Student:
    """Representation of student class"""
    def __init__(self, first_name, last_name, age):
        """initialization of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a student instance
        if attrs is a list of strings, onlt attr names must be retrieved
        otherwise all attr must be retrieved"""
        if (type(attrs) == list and
                all(Type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

