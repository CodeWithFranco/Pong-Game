from turtle import Turtle, Screen

# 'paddle' changed into 'self'
# This will enable you to tap in turtle class and
# use its methods and attributes

class Paddle(Turtle):   

    def __init__(self, position):
        super().__init__()
        # Paddle is created on the background
        self.color("white")
        self.shape("square") # all turtles starts at 20x20 pixels
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    # This is a method --- denoted by 'self' and function
    def go_up(self): 
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    




















