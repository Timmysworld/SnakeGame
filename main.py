import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Retro Snake Game")
screen.tracer(0)

# Create Snake
snake = Snake()

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
