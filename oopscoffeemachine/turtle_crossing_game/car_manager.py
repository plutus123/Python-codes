from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.li=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    def cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=1.5,stretch_wid=0.6)
            y=random.randint(-250,250)
            new_car.goto(300,y) 
            self.li.append(new_car)
    def move(self):
        for car in self.li:
            car.backward(self.car_speed)
    def speed_up(self):
        self.car_speed+=MOVE_INCREMENT
            