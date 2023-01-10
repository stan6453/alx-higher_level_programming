#!/usr/bin/python3
"""I/O module"""


def write_file(filename="", text=""):
    """wrtite to a file. overwrite file if it already exists"""
    with open(filename, "w") as f:
        return f.write(text)
