#!/usr/bin/python3
"""Magic module"""


def magic_string():
    """Magic function"""
    magic_string.counter += 1; return ("BestSchool, " * magic_string.counter)[:-2]


magic_string.counter = 0
