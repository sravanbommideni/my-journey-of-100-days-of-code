from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

#create screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong game")
screen.listen()

user_1=Paddle(370,0)
user_2=Paddle(xcoordinate=-380,ycoordinate=0)
ball = Ball()

screen.onkeypress(user_1.up,"Up")
screen.onkeypress(user_1.down,"Down")
screen.onkeypress(user_2.up,"w")
screen.onkeypress(user_2.down,"s")

game_over = False
while not game_over:
    time.sleep(0.1)
    ball.move()

screen.exitonclick()