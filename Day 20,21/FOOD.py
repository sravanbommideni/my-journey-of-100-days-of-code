import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.change_location()

    def change_location(self):
        self.setpos(random.randint(-380, 380), random.randint(-380, 380))