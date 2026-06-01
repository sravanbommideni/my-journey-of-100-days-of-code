from turtle import Turtle, Screen

obj = Turtle()
screen = Screen()

for i in range(5):
    obj.forward(20)
    obj.penup()
    obj.forward(20)
    obj.pendown()
screen.exitonclick()
