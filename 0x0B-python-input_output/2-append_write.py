#!/usr/bin/python3
"""I/O module"""


def append_write(filename="", text=""):
    """appends more text at the end of a file.
    creates file if it does not exist"""
    with open(filename, "a") as f:
        return f.write(text)
