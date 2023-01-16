#!/usr/bin/python3
"""Test for Rectangle class"""
import unittest
from unittest.mock import patch  # testing calls to print
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test for Rectangle Class"""

    def test_instance(self):
        """Test if rectangle is an instance of Base class"""
        self.assertIsInstance(Rectangle(7, 4), Base)
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        """Test Triangle class' properties and contructor parameters"""
        """test width and height"""
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, "4", 5)
        self.assertRaises(TypeError, Rectangle, 4, "5")
        self.assertRaises(ValueError, Rectangle, 0, 5)
        self.assertRaises(ValueError, Rectangle, 4, 0)

        """test x and y"""
        self.assertRaises(TypeError, Rectangle, 4, 5, "2")
        self.assertRaises(TypeError, Rectangle, 4, 5, 2, "5")
        self.assertRaises(ValueError, Rectangle, 4, 5, -1)
        self.assertRaises(ValueError, Rectangle, 4, 5, 8, -1)

        """test id"""
        # I didnt supply id when calling Rectangle()
        # rect4 = Rectangle(4, 5, 2, 1)
        # self.assertEqual(rect4.id, 1)

        """test rectangle object's state"""
        rect3 = Rectangle(4, 5, 2, 1, 7)
        self.assertEqual(rect3.id, 7)
        self.assertEqual(rect3.width, 4)
        self.assertEqual(rect3.height, 5)
        self.assertEqual(rect3.x, 2)
        self.assertEqual(rect3.y, 1)

        """Testing getters and setters"""
        rect5 = Rectangle(4, 5)
        self.assertRaises(TypeError, rect5.width, "")
        rect6 = Rectangle(4, 5)
        self.assertRaises(ValueError, setattr, rect6, "width",  0)
        rect7 = Rectangle(4, 5)
        rect7.width = 7
        self.assertEqual(rect7.width, 7)

        rect8 = Rectangle(4, 5)
        self.assertRaises(TypeError, rect8.height, "")
        rect9 = Rectangle(4, 5)
        self.assertRaises(ValueError, setattr, rect9, "height",  0)
        rect10 = Rectangle(4, 5)
        rect10.height = 7
        self.assertEqual(rect10.height, 7)

        rect8 = Rectangle(4, 5)
        self.assertRaises(TypeError, rect8.x, "")
        rect9 = Rectangle(4, 5)
        self.assertRaises(ValueError, setattr, rect9, "x",  -1)
        rect10 = Rectangle(4, 5)
        rect10.x = 7
        self.assertEqual(rect10.x, 7)

        rect8 = Rectangle(4, 5)
        self.assertRaises(TypeError, rect8.y, "")
        rect9 = Rectangle(4, 5)
        self.assertRaises(ValueError, setattr, rect9, "y",  -1)
        rect10 = Rectangle(4, 5)
        rect10.y = 9
        self.assertEqual(rect10.y, 9)

    def test_instance_methods(self):
        """Test Rectangle Class instance methods"""
        rect1 = Rectangle(7, 5, 4, 9, 0)
        self.assertEqual(rect1.area(), 35)

        """Test display() method"""
        rect1 = Rectangle(5, 3)
        string = """#####\n#####\n#####\n"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            rect1.display()
            self.assertEqual(mock_stdout.getvalue(), string)

        rect1 = Rectangle(4, 3, 3, 4)
        string = """\n\n\n\n   ####\n   ####\n   ####\n"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            rect1.display()
            self.assertEqual(mock_stdout.getvalue(), string)

        rect1 = Rectangle(1, 1, 3, 0)
        string = """   #\n"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            rect1.display()
            self.assertEqual(mock_stdout.getvalue(), string)

        rect1 = Rectangle(2, 2, 0, 3)
        string = """\n\n\n##\n##\n"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            rect1.display()
            self.assertEqual(mock_stdout.getvalue(), string)

        """Test __str__ magic method"""
        rect1 = Rectangle(2, 2, 0, 3, 9)
        self.assertEqual(str(rect1), "[Rectangle] (9) 0/3 - 2/2")

        rect2 = Rectangle(1, 1, 0, 0, 8)
        self.assertEqual(str(rect2), "[Rectangle] (8) 0/0 - 1/1")

        """Test update function"""
        rect1 = Rectangle(2, 2, 0, 3)
        """Test *args"""
        self.assertRaises(ValueError, rect1.update, 1, 2, 3, -1, 0)
        self.assertRaises(ValueError, rect1.update, 1, 0, 3, 1, 0)
        self.assertRaises(ValueError, rect1.update, 1, 2, 0, 1, 0)
        self.assertRaises(ValueError, rect1.update, 1, 2, 3, 1, -2)
        self.assertRaises(TypeError, rect1.update, 1, "2", 3, 1, 2)
        self.assertRaises(TypeError, rect1.update, 1, 2, "3", 1, 2)
        self.assertRaises(TypeError, rect1.update, 1, 2, 3, "1", 2)
        self.assertRaises(TypeError, rect1.update, 1, 2, 3, 1, "2")

        rect1.update(90, 23, 45, 12, 14)
        self.assertEqual(rect1.id, 90)
        self.assertEqual(rect1.width, 23)
        self.assertEqual(rect1.height, 45)
        self.assertEqual(rect1.x, 12)
        self.assertEqual(rect1.y, 14)

        """Test **kwargs"""
        rect1.update(width=90, height=23, y=45, id=12, x=14)
        self.assertEqual(rect1.id, 12)
        self.assertEqual(rect1.width, 90)
        self.assertEqual(rect1.height, 23)
        self.assertEqual(rect1.x, 14)
        self.assertEqual(rect1.y, 45)

        self.assertRaises(ValueError, rect1.update, width=1,
                          height=2, y=3, x=-1, id=0)
        self.assertRaises(ValueError, rect1.update, y=1,
                          width=0, x=3, height=1, id=0)
        self.assertRaises(ValueError, rect1.update, x=1,
                          width=2, height=0, y=1, id=0)
        self.assertRaises(ValueError, rect1.update, id=1,
                          height=2, width=3, x=1, y=-2)
        self.assertRaises(TypeError, rect1.update, height=1,
                          width="2", x=3, y=1, id=2)
        self.assertRaises(TypeError, rect1.update, y=1,
                          x=2, height="3", width=1, id=2)
        self.assertRaises(TypeError, rect1.update, width=1,
                          height=2, y=3, x="1", id=2)
        self.assertRaises(TypeError, rect1.update, id=1,
                          hight=2, width=3, x=1, y="2")

        rect1 = Rectangle(7, 3, 0, 3)
        rect1.update(5, 75, id=78, width=8, height=89)
        self.assertEqual(rect1.id, 5)
        self.assertEqual(rect1.width, 75)
        self.assertEqual(rect1.height, 3)

    def test_to_dictionary(self):
        """Test the to_dictioanry() method"""
        rect1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect1.to_dictionary(), {
                         "id": 5, "width": 1, "height": 2, "x": 3, "y": 4})

    def tearDown(self):
        """Tear down test method to reset class attribute
        """
        Base._Base__nb_objects = 0
