color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

import random
from turtle import Turtle,Screen

obj=Turtle()
obj.speed('fastest')
screen=Screen()
screen.colormode(255)

def random_color_RGB(object):
    """picks random color and assigns it to object"""
    picked_color=random.choice(color_list)
    object.color(picked_color[0] , picked_color[1] , picked_color[2])


def draw_row(object,no_of_dots):
    """draws an entire row of 10 colors"""
    for i in range(no_of_dots):
        random_color_RGB(object)
        object.dot(15)
        object.penup()
        object.fd(30)

def change_col_position(object,pos):
    """changes position of object fot it to be a square"""
    object.setpos((pos[0],pos[1]+30))

def initialise_postion(object):
    """bringing object to a center position"""
    object.penup()
    object.setheading(225)
    object.fd(200)
    object.setheading(0)
    object.pendown()

def start_paint(object , no_of_units_of_square):
    for i in range(no_of_units_of_square):
        position = object.pos()
        draw_row(object,no_of_units_of_square)
        change_col_position(object, position)

initialise_postion(obj)
starting_pos=obj.pos() #saving starting position coordinates
start_paint(obj,10)
obj.setpos(starting_pos)  #positiing the obj to where it started
obj.hideturtle()

screen.exitonclick()