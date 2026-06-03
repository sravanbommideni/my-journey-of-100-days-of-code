from turtle import Turtle,Screen

screen = Screen()

INITIAL_COORDINATES_LIST = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 20

class Snake:

    def move(self):
        for i in range(len(self.objects_list) - 1, 0, -1):
            new_pos = self.objects_list[i - 1].pos()
            self.objects_list[i].setpos(new_pos)
        self.objects_list[0].forward(MOVEMENT)

    def create_objects(self):
        for obj in INITIAL_COORDINATES_LIST:
            new_object = Turtle()
            self.objects_list.append(new_object)
            new_object.shape("square")
            new_object.color("white")
            new_object.speed("slowest")
            new_object.penup()
            new_object.setpos(obj)

    def __init__(self):
        self.objects_list = []
        self.create_objects()