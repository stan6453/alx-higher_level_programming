#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)

print("--")

my_square = Square(3)
print(my_square)

print("--")

my_square = Square(3, (1, 1))
print(my_square)

print("--")

my_square = Square(3, (3, 0))
print(my_square)

print("--")

my_square = Square(5)
print(my_square)

print("--")

my_square = Square(0, (5,6))
print(my_square)

print("--")
