from turtle import Turtle
import random as rd

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.ispeed = STARTING_MOVE_DISTANCE

    def gen_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(rd.choice(COLORS))
        new_car.pu()
        new_car.goto(260, rd.randint(-250, 251))

        self.all_cars.append(new_car)

    def speed(self):
        for obj in self.all_cars:
            obj.bk(self.ispeed)
