from turtle import Turtle,Screen

screen = Screen()
class ScoreBoard(Turtle):

    def __init__(self,position , alignment):
        super().__init__()
        with screen.no_animation():
            self.ALIGNMENT = alignment
            self.score = 0
            self.color("white")
            self.hideturtle()
            self.penup()
            self.setpos(position)
            self.update_score()

    def update_score(self):
        self.write(f"score : {self.score}",align=self.ALIGNMENT,font=('Arial', 12, 'bold'))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()