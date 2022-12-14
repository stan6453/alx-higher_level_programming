#!/usr/bin/python3
"""
Testing Python Docstrings
"""


class Square:
    """
    defines a square where:
    size: size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if wrong_pos_data(position):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position
        self.__size = size

    @property
    def size(self):
        """int: returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: return the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):

        if wrong_pos_data(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """int: returns the size of the square"""
        return self.__size ** 2

    def my_print(self):
        """print a visual representation of the square and its position"""
        i = 0
        if self.__size > 0:
            while i < self.__position[1]:
                print()
                i += 1

        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            for j in range(self.__size + self.__position[0]):
                if j < self.__position[0]:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()


def wrong_pos_data(position):
    """
    returns true if position data is the wrong format
    """
    if type(position) is not tuple:
        return True
    if len(position) != 2:
        return True
    if type(position[0]) is not int or type(position[1]) is not int:
        return True
    if position[0] < 0 or position[1] < 0:
        return True
