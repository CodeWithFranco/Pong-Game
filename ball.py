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
        self.x_move = 10
        self.y_move = 10
     
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()