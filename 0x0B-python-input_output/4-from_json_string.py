#!/usr/bin/python3
"""JSON module"""
import json


def from_json_string(my_str):
    """returns a python object representaion of a JSON sring"""
    return json.loads(my_str)
