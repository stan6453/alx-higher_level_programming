#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Blueprint for rectangle objects"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle class.
        Base class will assign Rectangle an id"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """Setters and Getters"""
    @property
    def width(self):
        """Gets the value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value for width"""
        validate_int("width", value)
        validate_dimension("width", value)
        self.__width = value

    @property
    def height(self):
        """Gets the value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value for height"""
        validate_int("height", value)
        validate_dimension("height", value)
        self.__height = value

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value for x"""
        validate_int("x", value)
        validate_position("x", value)
        self.__x = value

    @property
    def y(self):
        """Gets the value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value for y"""
        validate_int("y", value)
        validate_position("y", value)
        self.__y = value

    """instance methods"""

    def area(self):
        return self.width * self.height

    def display(self):
        for unit in range(self.y):
            print()
        for length in range(self.height):
            for unit in range(self.x):
                print(end=" ")
            for breadth in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {"id": self.id, "width": self.width, "height": self.height, "x":
                self.x, "y": self.y}

    """Special methods"""

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)


"""validation functions"""


def validate_int(name, value):
    if value.__class__ is not int:
        raise TypeError("{} must be an integer".format(name))


def validate_dimension(name, value):
    if value <= 0:
        raise ValueError("{} must be > 0".format(name))


def validate_position(name, value):
    if value < 0:
        raise ValueError("{} must be >= 0".format(name))
