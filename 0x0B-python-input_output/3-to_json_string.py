#!/usr/bin/python3
"""
function that returns JSON rep of an obj
"""


import json


def to_json_string(my_obj):
    """returns the JSON representation"""
    return json.dumps(my_obj)
