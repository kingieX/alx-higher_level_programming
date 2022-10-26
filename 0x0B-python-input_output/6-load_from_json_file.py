#!/usr/bin/python3
"""
function that creates an object from a JSON file
"""


def load_from_json_file(filename):
    """creates an object from json file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
