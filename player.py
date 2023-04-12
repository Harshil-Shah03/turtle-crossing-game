from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.start()

    def start(self):
        self.seth(90)
        self.pu()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.fd(20)

