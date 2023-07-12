#!/usr/bin/python3
import json

"""
This module is part of alx python tasks.
It contains only one function: save_to_json_file(my_obj, filename)
"""


def load_from_json_file(filename):
    """
    a function that creates an Object from
    a “JSON file”
    """
    with open(filename, 'r') as f:
        return json.load(f)
