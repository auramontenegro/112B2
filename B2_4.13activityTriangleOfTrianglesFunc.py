#Triangle of triangles with function
from turtle import *
def draw_triangle():
    """draw an equilateral triangle with side 40 units"""
    for sides in range(1, 4):
        forward(40)
        left(120)
        
#draw triangle 1
draw_triangle()

#move to start of triangle 2
penup()
left(90)
forward(100)
right(90)
pendown()

#draw triangle 2
draw_triangle()

#move to start of triangle 3
penup()
forward(100)
right(90)
forward(100)
left(90)
pendown()

#draw triangle 3
draw_triangle()
