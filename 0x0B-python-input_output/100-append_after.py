#!/usr/bin/python3
"""A module"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename) as fread:
        with open(filename, "a") as fwrite:
