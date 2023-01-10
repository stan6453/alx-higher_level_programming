#!/usr/bin/python3
"""I/O module"""
import json


def to_json_string(my_obj):
    """return a JSON representation of an object"""
    return json.dumps(my_obj)
