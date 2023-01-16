#!/usr/bin/python3
"""Base class"""
import json
import os


class Base:
    """This is a base class.
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None and type(id) is int:
            self.id = id
            Base.__nb_objects += 1
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """Class methods"""
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dict))

    @classmethod
    def load_from_file(cls):
        """loads the JSON string representation of list_objs from a file"""
        filename = cls.__name__ + ".json"
        list_objs = []
        with open(filename, encoding="utf-8") as file:
            # return a list of dicts that represent the objs we want to
            # create
            list_dict = cls.from_json_string(file.read())
            for a_dict in list_dict:
                # use these dictionaries to create a list of new objects
                list_objs.append(cls.create(**a_dict))
        return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the CSV representation of list_objs to a file"""
        square_attrs = ["id", "size", "x", "y"]
        rect_attrs = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Rectangle":
            cls.save_csv_to_disk(rect_attrs, list_objs)
        elif cls.__name__ == "Square":
            cls.save_csv_to_disk(square_attrs, list_objs)

    @classmethod
    def save_csv_to_disk(cls, attrs, list_objs):
        """writes the CSV representation of list_objs to a file"""
        filename = cls.__name__ + ".csv"
        # set lkist object to an empty list of its value is falsy
        list_objs = list_objs or []
        with open(filename, "w", encoding="utf-8") as file:
            for index, obj in enumerate(list_objs):
                for attr in attrs:
                    file.write(str(getattr(obj, attr)))
                    file.write(",")
                # avoid printing a new line after the last object
                if index != len(list_objs) - 1:
                    file.write("\n")

    @classmethod
    def load_from_file_csv(cls):
        """loads a csv representation of list_objs from a file"""
        square_attrs = ["id", "size", "x", "y"]
        rect_attrs = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Rectangle":
            return cls.load_csv_from_disk(rect_attrs)
        elif cls.__name__ == "Square":
            return cls.load_csv_from_disk(square_attrs)

    @classmethod
    def load_csv_from_disk(cls, attrs):
        """Converts a csv file into a list of objects"""
        import csv
        filename = cls.__name__ + ".csv"
        list_objs = []
        rows = []
        # my goal is to recreate a dictionary representaion of the object
        # and then use the create (a class method) to create the new object
        # from this dictionary
        with open(filename, encoding="utf-8") as file:
            # csv.reader() returns a list containing a list representing the
            # rows of the csv file (list of list of rows)
            rows = csv.reader(file)
            rows = list(rows)
        for row in rows:
            new_dict = {}
            for attr, value in zip(attrs, row):
                # csv.reader() returns row values as strings. since all our
                # attributes are ints, we need to convert all value to int
                new_dict[attr] = int(value)
            list_objs.append(cls.create(**new_dict))
        return list_objs

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance """
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

    @staticmethod
    def draw(list_rectangles, list_squares):
        """open a window and draws all the Rectangles and Squares"""
        import turtle

        my_turtle = turtle.Turtle()
        shape_list = list_rectangles + list_squares
        gap = 70  # distance between shapes
        my_turtle.penup()
        my_turtle.setpos(-550, 150)
        prev_obj_width = 0
        for shape in shape_list:
            # make shapes "gap" distance away from each other
            my_turtle.penup()
            my_turtle.setx(my_turtle.xcor() + gap + prev_obj_width)
            prev_obj_width = Base.draw_quadrilateral(my_turtle, shape, 2)

        input("press enter to exit")

    @staticmethod
    def draw_quadrilateral(brush, quad, scale):
        """Draw a 4 sided shape bases on the object passed in"""
        from random import choice

        colors = ["magenta", "gold", "red", "black",
                  "pink", "purple", "green", "orange", "blue"]
        brush.pencolor(choice(colors))
        brush.fillcolor(choice(colors))
        brush.begin_fill()
        brush.pendown()
        brush.forward(quad.width * scale)
        brush.right(90)
        brush.forward(quad.height * scale)
        brush.right(90)
        brush.forward(quad.width * scale)
        brush.right(90)
        brush.forward(quad.height * scale)
        brush.right(90)
        brush.end_fill()
        brush.write(quad.__class__.__name__, font=("Arial", 6 * scale, "bold"))
        return quad.width * scale
