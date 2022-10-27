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
        """retrieves a dictionary representation of a student instance"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = self.__dict__[i]
            except FileNotFoundError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """replace all attributes of the student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
