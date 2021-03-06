from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("red")
        self.speed(0)
        x, y = randint(-280, 280), randint(-280, 280)
        self.goto(x, y)
        self.refresh()

    def refresh(self):
        x, y = randint(-280, 280), randint(-280, 280)
        self.goto(x, y)
