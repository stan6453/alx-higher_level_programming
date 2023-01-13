#!/usr/bin/python3
import turtle

class Shape:
    width = 5
    height = 10

shape_list = [Shape(), Shape(), Shape()]


"""

print(my_turtle.pos())
my_turtle.forward(100)
my_turtle.left(90)
print(my_turtle.pos())
"""


def draw_quadrilateral(brush, quad, scale):
    from random import choice

    colors = ["red", "black", "pink", "purple", "green", "orange", "blue", "yellow"]
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
    return quad.width * scale



my_turtle = turtle.Turtle()
gap = 100 # distance between shapes
my_turtle.penup()
my_turtle.setpos(-900, 400)
prev_obj_width = 0
for shape in shape_list:
    #make shapes "gap" distance away from each other 
    my_turtle.penup()
    my_turtle.setx(my_turtle.xcor() + gap + prev_obj_width)
    prev_obj_width = draw_quadrilateral(my_turtle, shape, 5)

input("press enter to exit")
