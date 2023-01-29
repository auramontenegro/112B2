#general function for draw triangle
from turtle import *
def draw_triangle(length):
    """draw an equilateral triangle with side 40 units"""
    for sides in range(1, 4):
        forward(length)
        left(120)
