# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

from turtle import Screen
from score import Score
from snake import Snake
from food import Food
import time

# Setting up the Screen
s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

# Create the Snake, Food and Score
snake = Snake()
food = Food()
scoreboard = Score()

# Keep a track of which key is pressed
s.listen()

# Check the key pressed and control the snake
s.onkey(snake.forward,"Up") or s.onkey(snake.forward,"w")
s.onkey(snake.backward,"Down") or s.onkey(snake.backward,"s")
s.onkey(snake.left,"Left") or s.onkey(snake.left,"a")
s.onkey(snake.right,"Right") or s.onkey(snake.right,"d")

# Refresh the screen and Tell the Snake to move
game_on = True
while game_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.update()

# s.exitonclick()