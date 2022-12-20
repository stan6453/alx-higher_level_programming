#!/usr/bin/python3
class Square:
    def __init__(self, size = 0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(psition) is not tuple or len(position) != 2 or type(tuple[0]) is not int or type(tuple[1]) is not int or tuple[0] < 0 or tuple[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        selft.__position = position
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
        if type(psition) is not tuple or len(position) != 2 or type(tuple[0]) is not int or type(tuple[1]) is not int or tuple[0] < 0 or tuple[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end = "")
            print()
