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

        is_not_tuple = type(position) is not tuple
        len_not_two = len(position) != 2
        not_int = type(position[0]) is not int or type(position[1]) is not int
        conatin_negavive_value = position[0] < 0 or position[1] < 0
        if is_not_tuple or len_not_two or not_int or conatin_negavive_value:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position
        self.__size = size

    @property
    def size(self):
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
        return self.__position

    @position.setter
    def position(self, value):

        is_not_tuple = type(value) is not tuple
        len_not_two = len(value) != 2
        not_int = type(value[0]) is not int or type(value[1]) is not int
        conatin_negavive_value = value[0] < 0 or value[1] < 0
        if is_not_tuple or len_not_two or not_int or conatin_negavive_value:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        i = 0
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
