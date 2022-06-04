from turtle import Turtle


ALIGN = "center"
FONT = ("Verdana", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.write("Score: {}".format(self.score), align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def update(self):
        self.clear()
        self.write("Score: {}".format(self.score), align=ALIGN, font=FONT)
