#!/usr/bin/python3
"""Rectangle module."""


class Rectangle:
    def __init__(self, width=0, height=0):
        Rectangle.validate_dimention(width, "width")
        Rectangle.validate_dimention(height, "height")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        Rectangle.validate_dimention(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        Rectangle.validate_dimention(value, "height")
        self.__height = value

    def validate_dimention(value, name):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))


if __name__ == "__main__":
    Rectangle(2.0, 0)
