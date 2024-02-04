import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
p=Player()
c=CarManager()
screen.listen()
screen.onkey(p.move_forward,"Up")
game_is_on = True
sc=Scoreboard()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    c.cars()
    c.move()
    if p.ycor()>=280:
        p.finish()
        sc.score_up()
        c.speed_up()
    
    for car in c.li:
        if p.distance(car)<20:
            game_is_on=False
            sc.score()
screen.exitonclick()