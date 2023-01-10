#!/usr/bin/python3
"""JSON module"""
import json


def save_to_json_file(my_obj, filename):
    """converts a python object to a JSON sring
    and write the json to a file"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
