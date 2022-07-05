from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.colormode(255)
screen.bgcolor(0, 0, 0)
screen.title("Python (body) Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='w', fun=snake.north)
screen.onkey(key='a', fun=snake.west)
screen.onkey(key='s', fun=snake.south)
screen.onkey(key='d', fun=snake.east)

game_on = True
score = 0
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        score += 1
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for square in snake.tail:
        if snake.head.distance(square) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
