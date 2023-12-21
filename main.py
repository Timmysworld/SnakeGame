import time
from turtle import Screen

from SnakeGame.food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Retro Snake Game")
screen.tracer(0)

# Create Snake,Food,Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

# snake = Turtle(shape="square")
# snake.color("white")
# snake.goto(x=0, y=0)
#
# snake2 = Turtle(shape="square")
# snake2.color("white")
# snake2.goto(x=-20, y=0)
#
# snake3 = Turtle(shape="square")
# snake3.color("white")
# snake3.goto(x=-40, y=0)
