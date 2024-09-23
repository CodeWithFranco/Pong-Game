"""
Title: Pong Game
Author: Franco Nepomuceno
Date: 9/22/24
Rev: A
"""

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
paddle = Turtle()

# initial values
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # Turns off animation to hide the bar from moving from center to side

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
screen.exitonclick()