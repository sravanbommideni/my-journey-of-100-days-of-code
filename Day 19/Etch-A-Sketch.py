from turtle import Turtle,Screen

obj=Turtle()
screen = Screen()
screen.listen()

initial_position=obj.pos()
def move_forward():
    obj.forward(20)

def move_backward():
    obj.backward(20)

def rotate_clockwise():
    obj.setheading(obj.heading() - 10)

def rotate_anti_clockwise():
    obj.setheading(obj.heading() + 10)

def clear():
    obj.penup()
    obj.home()
    obj.clear()
    obj.pendown()


screen.onkeypress(fun=move_forward,key="w")

screen.onkeypress(fun=move_backward,key="s")

screen.onkeypress(fun=rotate_anti_clockwise,key="a")

screen.onkeypress(fun=rotate_clockwise,key="d")

screen.onkey(fun=clear,key="c")

screen.exitonclick()