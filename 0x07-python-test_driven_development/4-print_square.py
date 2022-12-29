#!/usr/bin/python3
"""Print square module."""


def print_square(size):
    """Print a square."""
    """Tests"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    """Business Logic"""
    if size == 0:
        print()
        return
    for height in range(size):
        for width in range(size):
            print("#", end="")
        print()
