import time
from turtle import Turtle,Screen
from snake import Snake

screen = Screen()
screen.setup(800,800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #turning the animation off , won't show animation until screen.update

snake = Snake()

while True:
    screen.update()
    time.sleep(0.2)
    snake.move()

# screen.exitonclick()