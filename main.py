import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()
game_is_on = True
screen.listen()
screen.onkey(key="Up", fun=player.move_up)
gen_cnt = 0
while game_is_on:
    gen_cnt += 1
    time.sleep(0.1)
    score.score()
    if gen_cnt % 6 == 0:
        car.gen_car()
    car.speed()

    for i in car.all_cars:
        if player.distance(i) < 25:
            game_is_on = False
            score.over()

    if player.ycor() == 280:
        player.start()
        car.ispeed += 10
        score.lvl += 1

    screen.update()


screen.exitonclick()
