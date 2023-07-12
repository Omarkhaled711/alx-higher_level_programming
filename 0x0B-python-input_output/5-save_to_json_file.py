#!/usr/bin/python3
import json

"""
This module is part of alx python tasks.
It contains only one function: save_to_json_file(my_obj, filename)
"""


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
