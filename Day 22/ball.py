from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.xmove=10
        self.ymove=10
        self.move_speed=0.1

    def move(self):
        new_pos = (self.xcor() + self.xmove , self.ycor() + self.ymove)
        self.setpos(new_pos)

    def bounce_back_y(self):
        self.ymove *= -1

    def bounce_back_x(self):
        self.xmove *= -1
        self.move_speed *= 0.95

    def is_hit_top_or_bottom(self):
        if self.ycor() > 280 or self.ycor() < -280:
            return True
        return False

    def restart(self):
        self.reset()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.ymove *= -1
        self.xmove *= -1
        self.move_speed = 0.1