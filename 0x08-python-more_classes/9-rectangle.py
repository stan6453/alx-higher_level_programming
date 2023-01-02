#!/usr/bin/python3
"""Rectangle module."""


class Rectangle:

    """Class/Static attributes"""
    number_of_instances = 0
    print_symbol = "#"

    """Instance Methods"""
    def __init__(self, width=0, height=0):
        Rectangle.validate_dimention(width, "width")
        Rectangle.validate_dimention(height, "height")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol) or str(Rectangle.print_symbol)
            string += "\n"
        return string[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    """Static/Class methods"""
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def square(cls, size=0):
        return Rectangle(cls, cls)

    def validate_dimention(value, name):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))


if __name__ == "__main__":
    rect1 = Rectangle(5, 0)
    rect2 = Rectangle(1, 1)
    print(Rectangle.bigger_or_equal(1, []))
