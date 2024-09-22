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

# # Paddle is created on the background
# paddle.color("white")
# paddle.shape("square") # all turtles starts at 20x20 pixels
# paddle.shapesize(stretch_len=1, stretch_wid=5)
# paddle.penup()
# paddle.goto(350, 0)

# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)

# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball.moving_random()

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()