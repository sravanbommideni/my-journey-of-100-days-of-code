from turtle import Turtle,Screen

screen = Screen()

INITIAL_COORDINATES_LIST = [(0, 0), (-20, 0), (-40, 0)]

END = 390

MOVEMENT = 20

UP = 90
DOWN = 270
LEFT=180
RIGHT=0

class Snake:

    def move(self):
        for i in range(len(self.objects_list) - 1, 0, -1):
            new_pos = self.objects_list[i - 1].pos()
            self.objects_list[i].setpos(new_pos)
        self.head.forward(MOVEMENT)

    def up(self):
        if self.head.heading()!=DOWN: #IF SNAKE IS GOING UP IT SHOULD NOT GO DOWN
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP: #IF SNAKE IS GOING DOWN IT SHOULD NOT GO UP
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT: #IF SNAKE IS GOING LEFT IT SHOULD NOT GO RIGHT
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT: #IF SNAKE IS GOING RIGHT IT SHOULD NOT GO LEFT
            self.head.setheading(RIGHT)

    def create_objects(self):
        for obj in INITIAL_COORDINATES_LIST:
            self.add_object(obj)

    def add_object(self,position):
        new_object = Turtle()
        self.objects_list.append(new_object)
        new_object.shape("square")
        new_object.color("white")
        new_object.speed("slowest")
        new_object.penup()
        new_object.setpos(position)

    def extend(self):
        self.add_object(self.objects_list[-1].position())


    def is_hit_wall(self):
        if self.head.xcor() > END or self.head.xcor() < -END or self.head.ycor() > END or self.head.ycor() < -END:
            return True
        return False

    def is_snake_eaten(self,food_object):
        if self.head.distance(food_object) < 18:
            return True
        return False

    def is_snake_hit_tail(self):
        for segment in self.objects_list[1:]:
            if self.head.distance(segment) < 18:
                return True
        return False


    def __init__(self):
        self.objects_list = []
        self.create_objects()
        self.head = self.objects_list[0]