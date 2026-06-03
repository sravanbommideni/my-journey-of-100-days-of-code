from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'bold')
class Scorecard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(x=0,y=375)
        self.update_score()

    def update_score(self):
        self.write(f"score : {self.score}",align=ALIGNMENT,font=(FONT))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.setpos(0,0)
        self.write(arg=f"Game over....your FINAL SCORE : {self.score}",align=ALIGNMENT,font=FONT)