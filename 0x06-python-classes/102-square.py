#!/usr/bin/python3
"""
Testing Python Docstrings
"""


class Square:
    """
    class has a size private instance property
    """

    def __init__(self, size=0):
        if type(size) is not int and type(size) is not float:
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """int: returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        if (self.size == other.size):
            return True
        return False

    def __gt__(self, other):
        if (self.size > other.size):
            return True
        return False

    def __lt__(self, other):
        if (self.size < other.size):
            return True
        return False

    def __le__(self, other):
        if (self.size <= other.size):
            return True
        return False

    def __ge__(self, other):
        if (self.size >= other.size):
            return True
        return False

    def __ne__(self, other):
        if (self.size != other.size):
            return True
        return False
