from turtle import Turtle,Screen

screen = Screen()

END = 260
MOVE = 20

class Paddle(Turtle):
    def __init__(self,xcoordinate,ycoordinate):
        super().__init__()
        with screen.no_animation():
            self.shape("square")
            self.penup()
            self.shapesize(stretch_wid=5,stretch_len=1)
            self.color("white")
            self.setpos(x=xcoordinate,y=ycoordinate)

    def up(self):
        new_y = self.ycor() + MOVE
        if new_y < END:
            self.goto(x=self.xcor(),y= new_y)

    def down(self):
        new_y = self.ycor() - MOVE
        if new_y > -END:
            self.setpos(x=self.xcor(),y=new_y)
