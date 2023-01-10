#!/usr/bin/python3
"""I/O module"""


def read_file(filename=""):
    """print content of a file to stdout"""
    with open(filename) as f:
        print(f.read(), end="")
