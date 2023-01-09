#!/usr/bin/python3
"""Myint module"""


class MyInt(int):
    """Myint class"""
    def __eq__(self, other):
        return self.real != other.real

    def __ne__(self, other):
        return self.real == other.real
