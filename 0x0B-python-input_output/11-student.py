#!/usr/bin/python3
"""students module"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
    	"""Initializes a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
    	"""Return a dictionary representaion of the object based on the keys
    	contained in attrs"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key in attrs:
            if key in self.__dict__:
                new_dict[key] = self.__dict__[key]
        return new_dict

    def reload_from_json(self, json):
    	"""Replaces all attributes of the Student"""
        self.__dict__ = json
