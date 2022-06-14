from turtle import Turtle


ALIGN = "center"
FONT = ("Verdana", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", "r") as hs:
            self.high_score = int(hs.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write("Score: {}, High Score: {}".format(self.score, self.high_score), align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as hs:
                hs.write(f"{self.high_score}")
        self.update()

    def update(self):
        self.clear()
        self.write("Score: {}, High Score: {}".format(self.score, self.high_score), align=ALIGN, font=FONT)
