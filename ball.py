from turtle import Turtle, Screen
#import random
#import time

screen = Screen()

class Ball(Turtle):   

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle") # all turtles starts at 20x20 pixels
        #self.shapesize(width = 20, height = 20)
        self.penup()
     

    def move(self):
        new_x = self.xcor + 10
        new_y = self.ycor + 10
        self.goto(new_x, new_y)
