#!/usr/bin/python3
"""Say my name module."""


def say_my_name(first_name, last_name=""):
    """Print myname."""
    """Tests."""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    """Main logic."""
    print("My name is {} {}".format(first_name, last_name))
