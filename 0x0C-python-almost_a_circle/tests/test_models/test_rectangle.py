#!/usr/bin/python3
"""Test for Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test for Rectangle Class"""
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
        self.assertRaises(ValueError, Rectangle, 4, 5, -1)

        """test id"""
        #I didnt supply id when calling Rectangle()
        #rect4 = Rectangle(4, 5, 2, 1)
        #self.assertEqual(rect4.id, 1)

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
        """Test Tringle Class instance methods"""
        rect1 = Rectangle(7, 5, 4, 9, 0)
        self.assertEqual(rect1.area(), 35)

        rect1 = Rectangle(5, 3, 9, 5)
        string = """#####
        #####
        #####"""
        self.assertEqual(rect1.display(), string)


