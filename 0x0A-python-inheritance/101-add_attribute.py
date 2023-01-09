#!/usr/bin/python3
"""New attribute module"""


def add_attribute(obj, attr, value):
    """add a new attribute to an object"""
    if hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
