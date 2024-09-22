from turtle import Turtle, Screen
import random

screen = Screen()

class Ball(Turtle):   

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle") # all turtles starts at 20x20 pixels
        #self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(0, 0)

    def moving_random(self):
        random_x = random.randint (-350, 350)
        random_y = random.randint (-250, 250)
        self.goto(random_x, random_y)
