#!/usr/bin/python3
"""A module"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text (new_string) to a file,
    after each line containing a specific string (search_string)"""
    buf = ""
    with open(filename) as fread:
        for line in fread:
            buf += line
            if search_string in line:
                buf += new_string
    with open(filename, "w") as fwrite:
        fwrite.write(buf)
