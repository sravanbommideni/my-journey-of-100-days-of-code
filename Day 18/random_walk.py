import random
from turtle import Turtle,Screen

obj=Turtle()
screen=Screen()
screen.colormode(255)

def pick_random_color(object):
    # c = ['black', 'cyan', 'goldenrod', 'deep pink', 'pale green', 'purple', 'teal', 'dark red']
    # object.color(random.choice(c))
    random_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    object.color(random_color)

def pick_random_direction(object):
    directions = [0,90,180,270]
    object.forward(random.randint(1,51))
    object.setheading(random.choice(directions))

while True:
    obj.pensize(13)
    obj.speed('fastest')
    pick_random_color(obj)
    pick_random_direction(obj)

