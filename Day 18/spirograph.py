import random
from turtle import Turtle,Screen

obj=Turtle()
obj.speed('fastest')
screen=Screen()
screen.colormode(255)

def pick_random_color(object):
    random_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    object.color(random_color)

def draw_spirographs(object,gap_size):
    for i in range(int(360/gap_size)):
        pick_random_color(object)
        object.circle(100)
        object.setheading(obj.heading() + gap_size)

pick_random_color(obj)
draw_spirographs(obj,5)

screen.exitonclick()