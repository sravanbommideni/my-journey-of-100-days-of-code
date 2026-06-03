import time
from turtle import Turtle,Screen
from snake import Snake
from FOOD import Food
from scorecard import Scorecard

screen = Screen()
screen.setup(800,800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #turning the animation off , won't show animation until screen.update

snake = Snake()
food = Food()
scorecard = Scorecard()

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_over=False
while not game_over:
    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.is_snake_eaten(food_object=food):
        snake.extend()
        scorecard.increase_score()
        food.change_location()

    if snake.is_hit_wall() or snake.is_snake_hit_tail():
        game_over = True
        scorecard.game_over()
        
screen.exitonclick()

