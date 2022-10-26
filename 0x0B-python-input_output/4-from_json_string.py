#!/usr/bin/python3
"""
function that returns an obj JSON string
"""


import json


def from_json_string(my_str):
    """returns an obj rep by the JSON string"""
    return json.loads(my_str)
