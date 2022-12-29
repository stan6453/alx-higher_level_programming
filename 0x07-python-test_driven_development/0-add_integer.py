#!/usr/bin/python3
"""add module."""


def add_integer(a, b=98):
    """Add two integers."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b


if __name__ == "__main__":
    print(add_integer(7, 9))
