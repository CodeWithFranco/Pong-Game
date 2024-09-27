"""
Title: Pong Game
Author: Franco Nepomuceno
Date: 9/22/24
Rev: A
"""

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
paddle = Turtle()

# initial values
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # Turns off animation to hide the bar from moving from center to side

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    pong.move()

    #Detect collision
    if pong.ycor() > 280 or pong.ycor() < -280:
        #bounce_y off the wall (Top and Bottom)
        pong.bounce_y()

    #Detect collision with r_paddle
    if pong.distance(r_paddle) < 50 and pong.xcor() > 320 or pong.distance(l_paddle) < 50 and pong.xcor() < -320:
        pong.bounce_x()

    #Detect the ball that goes at the edge of the screen (R) 
    if pong.xcor() > 380:
        pong.reset()

    #Detect the ball that goes at the edge of the screen (L)
    if pong.xcor() < -380:
        pong.reset()


screen.exitonclick()
