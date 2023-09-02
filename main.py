import time
import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
scoreboard=Scoreboard()
screen.tracer(0)
food = Food()
snake = Snake()
screen.onkey(fun=snake.move_up, key='w')
screen.onkey(fun=snake.move_left, key="a")
screen.onkey(fun=snake.move_right, key="d")
screen.onkey(fun=snake.move_down, key="s")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    screen.listen()
    if snake.body_segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.snake_reset()
    for segment in snake.body_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.snake_reset()

screen.exitonclick()
