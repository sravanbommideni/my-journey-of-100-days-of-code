from turtle import Turtle, Screen

obj = Turtle()
screen = Screen()

def generate_shapes(no_of_vertices):
    for i in range(no_of_vertices):
        obj.forward(100)
        obj.right(360 / no_of_vertices)

c = ['black', 'cyan', 'goldenrod', 'deep pink', 'pale green', 'purple', 'teal', 'dark red']
k=0

for no_of_sides in range(3,11):
    obj.color(c[k])
    generate_shapes(no_of_sides)
    k += 1

screen.exitonclick()