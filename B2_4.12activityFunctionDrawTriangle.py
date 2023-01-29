# Defining function draw triangle
from turtle import *
def draw_triangle():
    """draw an equilateral triangle with side 40 units"""
    for sides in range(1, 4):
        forward(40)
        left(120)
    
