from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
from game_over import GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# Keybind snake's movements
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    # Keep snake constantly moving forward
    snake.move()
    # Detect Snake Food Collision
    if snake.head.distance(food) < 15:
        # Move food to new random location
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect Wall Collision
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_on = False

    # Detect Tail Collision
    for seg in snake.seg_list[2:]:
        if snake.head.distance(seg) <= 0:
            game_on = False

game_over = GameOver()

screen.exitonclick()
