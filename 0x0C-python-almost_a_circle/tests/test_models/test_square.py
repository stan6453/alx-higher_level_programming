#!/usr/bin/python3
"""Test for Square class"""
import unittest
from unittest.mock import patch #testing calls to print
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square



class TestSquare(unittest.TestCase):
    """Test for Square Class"""

    def test_instance(self):
        """Test if Square is an instance of Base and Rectangle class"""
        self.assertIsInstance(Square(7), Base)
        self.assertIsInstance(Square(8), Rectangle)
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))

    def test_parameters(self):
        """Test sqaure class' properties and contructor parameters"""
        """test size"""
        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, "4")
        self.assertRaises(ValueError, Square, 0)

        """test x and y"""
        self.assertRaises(TypeError, Square, 4, "2")
        self.assertRaises(TypeError, Square, 4, 2, "5")
        self.assertRaises(ValueError, Square, 4, -1)
        self.assertRaises(ValueError, Square, 4, 5, -1)

        """test id"""
        #I didnt supply id when calling Square()
        #square4 = Square( 5, 2, 1)
        #self.assertEqual(square4.id, 1)

        """test Square object's state"""
        sq3 = Square(5, 2, 1, 7)
        self.assertEqual(sq3.id, 7)
        self.assertEqual(sq3.size, 5)
        self.assertEqual(sq3.width, 5)
        self.assertEqual(sq3.height, 5)
        self.assertEqual(sq3.x, 2)
        self.assertEqual(sq3.y, 1)

        """Testing getters and setters"""
        sq5 = Square(9)
        self.assertRaises(TypeError, sq5.width, "")
        self.assertRaises(ValueError, setattr, sq5, "width",  0)
        sq5.size = 1
        self.assertEqual(sq5.width, 1)
        self.assertEqual(sq5.height, 1)
        self.assertEqual(sq5.size, 1)

        sq8 = Square(4)
        self.assertRaises(TypeError, sq8.x, "")
        sq9 = Square(5)
        self.assertRaises(ValueError, setattr, sq9, "x",  -1)
        sq10 = Square(4)
        sq10.x = 7
        self.assertEqual(sq10.x, 7)

        sq8 = Square(4)
        self.assertRaises(TypeError, sq8.y, "")
        sq9 = Square(4)
        self.assertRaises(ValueError, setattr, sq9, "y",  -1)
        sq10 = Square(4)
        sq10.y = 9
        self.assertEqual(sq10.y, 9)

    def test_instance_methods(self):
        """Test Square Class instance methods"""

        """Test Area method"""
        sq1 = Square(7, 5, 4, 9)
        self.assertEqual(sq1.area(), 49)

        """Test display() method"""
        sq1 = Square(5)
        string = """#####\n#####\n#####\n#####\n#####\n"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            sq1.display()
            self.assertEqual(mock_stdout.getvalue(), string)

        sq1 = Square(4, 3, 3)
        string = """\n\n\n   ####\n   ####\n   ####\n   ####\n"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            sq1.display()
            self.assertEqual(mock_stdout.getvalue(), string)

        sq1 = Square(1, 3, 0)
        string = """   #\n"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            sq1.display()
            self.assertEqual(mock_stdout.getvalue(), string)


        sq1 = Square(2, 0, 3)
        string = """\n\n\n##\n##\n"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            sq1.display()
            self.assertEqual(mock_stdout.getvalue(), string)

        """Test __str__ magic method"""
        sq1 = Square(2, 0, 3, 9)
        self.assertEqual(str(sq1), "[Square] (9) 0/3 - 2")

        sq2 = Square(1, 0, 0, 8)
        self.assertEqual(str(sq2), "[Square] (8) 0/0 - 1")

        """Test update function"""
        sq1 = Square(2, 0, 3)
        """Test *args"""
        self.assertRaises(ValueError, sq1.update, 1,2,-1,0)
        self.assertRaises(ValueError, sq1.update, 1,0,1,0)
        self.assertRaises(ValueError, sq1.update, 1,2,1,-2)
        self.assertRaises(TypeError, sq1.update, 1,"2",1,2)
        self.assertRaises(TypeError, sq1.update, 1,2,"1",2)
        self.assertRaises(TypeError, sq1.update, 1,3,1,"2")

        sq1.update(90, 45, 12, 14)
        self.assertEqual(sq1.id, 90)
        self.assertEqual(sq1.size, 45)
        self.assertEqual(sq1.height, 45)
        self.assertEqual(sq1.height, 45)
        self.assertEqual(sq1.x, 12)
        self.assertEqual(sq1.y, 14)

        """Test **kwargs"""
        sq1.update(size=90, y=45, id=12, x=14)
        self.assertEqual(sq1.id, 12)
        self.assertEqual(sq1.size, 90)
        self.assertEqual(sq1.width, 90)
        self.assertEqual(sq1.height, 90)
        self.assertEqual(sq1.x, 14)
        self.assertEqual(sq1.y, 45)

        self.assertRaises(ValueError, sq1.update, size=1,y=3,x=-1,id=0)
        self.assertRaises(ValueError, sq1.update, y=1,size=0,x=3,id=0)
        self.assertRaises(ValueError, sq1.update, id=1,x=1,y=-2)
        self.assertRaises(TypeError, sq1.update, size="2",x=3,y=1,id=2)
        self.assertRaises(TypeError, sq1.update, size=1,y=3,x="1",id=2)
        self.assertRaises(TypeError, sq1.update, id=1,size=2,x=1,y="2")

        sq1 = Square(7, 3, 0, 3)
        sq1.update(5, 75, id=78, width=8, height=89)
        self.assertEqual(sq1.id, 5)
        self.assertEqual(sq1.width, 75)
        self.assertEqual(sq1.height, 75)
        self.assertEqual(sq1.size, 75)

    def test_to_dictionary(self):
        """Test the to_dictioanry() method"""
        sq1 = Square(1, 3, 4, 5)
        self.assertEqual(sq1.to_dictionary(), {"id": 5, "size": 1, "x": 3, "y": 4})
