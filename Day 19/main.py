import random
from turtle import Turtle,Screen
from racing_data import objects_data

screen = Screen()
screen.setup(width=800,height=600)

colors_list=[]
objects_list=[]
result_list=[]

def create_objects(obj_list,col_list,data):
    """creates turtle instances , appends them into object list along with colors and changes their shape to turtle"""
    for obj in data:
        obj_name = obj["name"]
        obj_color = obj["color"]
        obj_name = Turtle()
        obj_list.append(obj_name)
        obj_name.color(obj_color)
        col_list.append(obj_color)
        obj_name.shape("turtle")
        obj_name.speed(0)


def set_position(obj_list):
    """places the turtle instances in starting position"""
    j=-60
    for obj in obj_list:
        obj.penup()
        obj.setpos(x=-380,y=j)
        j+=30

def run(obj_list,winner_list):
    """generates random fd steps for all objects and return the list of turtles with ascending order of finishing times"""
    while len(winner_list)!=6:
        for obj in obj_list:
            if obj not in winner_list:
                obj.fd(random.randint(0,10))
                if obj.pos()[0]>=390:
                    winner_list.append(obj)
    return winner_list

create_objects(obj_list=objects_list,col_list=colors_list,data=objects_data)

user_bet=screen.textinput(title="make your bet" ,prompt=f"choose one colour {colors_list}")

set_position(obj_list=objects_list)

winner_object = run(obj_list=objects_list,winner_list=result_list)[0]

if winner_object.pencolor() != user_bet:
    print(f"you lost....the winner is {winner_object.pencolor()}")
else:
    print("your turtle has won....")
screen.bye()
