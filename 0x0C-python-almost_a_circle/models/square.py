#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle, validate_int, validate_dimension


class Square(Rectangle):
    """Blueprint for square objects"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square class."""
        """Rectangle class will assign Square class
        an id, width, height, x, and y attributes"""
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    """Getters and Setters"""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        validate_int("width", value)
        validate_dimension("width", value)
        self.width = value
        self.height = value
        self.__size = value

    """Instance methids"""
    def update(self, *args, **kwargs):
        if args:
            attributes = ["id","size","x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    """Special methods"""
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
