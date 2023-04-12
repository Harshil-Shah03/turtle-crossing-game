from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.hideturtle()
        self.pu()

    def score(self):
        self.goto(-280, 260)
        self.clear()
        self.write(f"Level: {self.lvl}", align="left", font=FONT)

    def over(self):

        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
