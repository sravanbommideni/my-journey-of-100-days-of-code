from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.setpos(x=0, y=0)
        self.move()

    def move(self):
        new_pos = (self.xcor() + 10 , self.ycor() + 10)
        self.setpos(new_pos)
