#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle, validate_int, validate_dimension


class Square(Rectangle):
    """Blueprint for square objects"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square class."""
        """Rectangle class will assign Square class
        an id, width, height, x, and y attributes"""
        super().__init__(size, size, x, y, id)
        self.size = size

    """Getters and Setters"""
    @property
    def size(self):
        """Gets the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        validate_int("width", value)
        validate_dimension("width", value)
        self.width = value
        self.height = value
        self.__size = value

    """Instance methids"""

    def update(self, *args, **kwargs):
        """Updates attributes of an instance"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    """Special methods"""

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
