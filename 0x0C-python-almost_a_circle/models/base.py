#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """This is a base class.
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
            Base.__nb_objects += 1
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """Class methods"""
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__+".json"
        list_dict=[]
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf-8") as file:
            if list_dict:
                file.write(json.dumps(list_dict))
            else:
                file.write("[]")

    @classmethod
    def load_from_file(cls):
        """loads the JSON string representation of list_objs from a file"""
        filename = cls.__name__ + ".json"
        list_objs = []
        with open(filename, encoding="utf-8") as file:
            #return a list of dicts that represent the objs we want to create
            list_dict = cls.from_json_string(file.read())
            for a_dict in list_dict:
                #use these dictionaries to create a list of new objects
                list_objs.append(cls.create(**a_dict))
        return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the CSV representation of list_objs to a file"""
        square_attrs = ["id","size","x", "y"]
        rect_attrs = ["id","width","height","x", "y"]
        if cls.__name__ == "Rectangle":
            cls.save_csv_to_disk(rect_attrs, list_objs)
        elif cls.__name__ == "Square":
            cls.save_csv_to_disk(square_attrs, list_objs)

    @classmethod
    def save_csv_to_disk(cls, attrs, list_objs):
        """writes the CSV representation of list_objs to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", encoding="utf-8") as file:
            for obj in list_objs:
                for attr in attrs:
                    file.write(str(getattr(obj, attr)))
                    file.write(",")
                file.write("\n")


    @classmethod
    def create(cls, **dictionary):
        new_quadrilateral = cls(**dictionary)
        new_quadrilateral.update(**dictionary)
        return new_quadrilateral

    """Static methods"""
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation of json_string.
        json_string is a string representing a list of dictionaries"""
        if json_string:
            return json.loads(json_string)
        return []

