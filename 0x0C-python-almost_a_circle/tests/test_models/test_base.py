#!/usr/bin/python3
"""Test for the Base class to make sure it functions as expected"""

from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json

class TestBase(TestCase):
    """Unit test for Base class"""
    def test_id(self):
        obj = Base()
        self.assertEqual(obj.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)
        obj3 = Base(7)
        self.assertEqual(obj3.id, 7)

    def test_to_json_string(self):
        """Test for the to_json_string() fn"""
        list_dicts = [
                        {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}, 
                        {"id": 6, "width": 3, "height": 1, "x": 4, "y": 8}
                    ]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(type(json_string), str)
        self.assertEqual(type(json.loads(json_string)), list)
        self.assertEqual(type(json.loads(json_string)[0]), dict)
        self.assertEqual(list_dicts, json.loads(json_string))

        """assuming list of dictionaries is empty"""
        list_dicts = []
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(type(json_string), str)
        self.assertEqual(type(json.loads(json_string)), list)
        self.assertEqual(list_dicts, json.loads(json_string))

        """assuming list of dictionaries is None"""
        list_dicts = None
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(type(json_string), str)
        self.assertEqual(type(json.loads(json_string)), list)
        self.assertEqual([], json.loads(json_string))


    def test_save_to_file(self):
        """test for the save_to_file() fn"""

        """test saving list of rectangle objects"""
        list_rects = [Rectangle(1, 2, 3, 4, 5), Rectangle(4, 5, 6, 7, 8)]
        Rectangle.save_to_file(list_rects)
        with open("Rectangle.json", encoding="utf-8") as file:
            read_list_dict = json.loads(file.read())
            self.assertEqual(read_list_dict, [
                {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}, 
                {"id": 8, "width": 4, "height": 5, "x": 6, "y": 7}
                ])

        list_rects = []
        Rectangle.save_to_file(list_rects)
        with open("Rectangle.json", encoding="utf-8") as file:
            read_list_dict = json.loads(file.read())
            self.assertEqual(read_list_dict, [])

        list_rects = None
        Rectangle.save_to_file(list_rects)
        with open("Rectangle.json", encoding="utf-8") as file:
            read_list_dict = json.loads(file.read())
            self.assertEqual(read_list_dict, [])

        """test saving list of square objects"""
        list_sqs = [Square(1, 2, 3, 5), Square(4, 5, 6, 8)]
        Square.save_to_file(list_sqs)
        with open("Square.json", encoding="utf-8") as file:
            read_list_dict = json.loads(file.read())
            self.assertEqual(read_list_dict, [
                {"id": 5, "size": 1, "x": 2, "y": 3}, 
                {"id": 8, "size": 4, "x": 5, "y": 6}
                ])

        list_sqs = []
        Square.save_to_file(list_sqs)
        with open("Square.json", encoding="utf-8") as file:
            read_list_dict = json.loads(file.read())
            self.assertEqual(read_list_dict, [])

        list_sqs = None
        Square.save_to_file(list_rects)
        with open("Square.json", encoding="utf-8") as file:
            read_list_dict = json.loads(file.read())
            self.assertEqual(read_list_dict, [])

    def test_from_json_string(self):
        """test the from_json_string() fn"""

        """Testing rects"""
        json_list_rects = '[\
                {"id": 89, "width": 10, "height": 4},\
                {"id": 7, "width": 1, "height": 7}\
                ]'
        real_list_rects=[
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        list_rects = Rectangle.from_json_string(json_list_rects)
        self.assertEqual(list_rects, real_list_rects)

        json_list_rects = "[]"
        real_list_rects=[]
        list_rects = Rectangle.from_json_string(json_list_rects)
        self.assertEqual(list_rects, real_list_rects)

        json_list_rects = None
        real_list_rects=[]
        list_rects = Rectangle.from_json_string(json_list_rects)
        self.assertEqual(list_rects, real_list_rects)

        """Testing squares"""
        json_list_sqs = '[\
                {"id": 89, "size": 10},\
                {"id": 7, "size": 1}\
                ]'
        real_list_sqs=[
                {'id': 89, 'size': 10,},
                {'id': 7, 'size': 1}
                ]
        list_sqs = Square.from_json_string(json_list_sqs)
        self.assertEqual(list_sqs, real_list_sqs)

        json_list_sqs = "[]"
        real_list_sqs=[]
        list_sqs = Square.from_json_string(json_list_sqs)
        self.assertEqual(list_sqs, real_list_sqs)

        json_list_sqs = None
        real_list_sqs=[]
        list_sqs = Square.from_json_string(json_list_sqs)
        self.assertEqual(list_sqs, real_list_sqs)

    def test_create(self):
        """test for the create() method"""
