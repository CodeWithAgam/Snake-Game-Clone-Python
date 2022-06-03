from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.write("Score: {}".format(self.score), align="center", font=("Verdana", 20, "normal"))

    def update(self):
        self.clear()
        self.write("Score: {}".format(self.score), align="center", font=("Verdana", 20, "normal"))