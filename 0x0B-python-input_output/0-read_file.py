#!/usr/bin/python3
"""I/O module"""


def read_file(filename=""):
    """print content of a file to stdout"""
    with open(filename, "r") as f:
        print(f.read())
