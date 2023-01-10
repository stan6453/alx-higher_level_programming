#!/usr/bin/python3
"""JSON module"""
import json


def load_from_json_file(filename):
    """Create an Object from a “JSON file”"""
    with open(filename) as f:
        return json.loads(f.read())
