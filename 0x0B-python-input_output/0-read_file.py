#!/usr/bin/python3
"""I/O module"""


def read_file(filename=""):
    """print content of a file to stdout"""
    with open(filename, "rt", encoding="utf-8") as f:
        print(f.read())
