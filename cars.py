from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
colors = ['blue', 'green', 'yellow', 'red', 'orange', 'cyan', 'magenta', 'purple', 'black']

class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.color(random.choice(colors))
            new_car.penup()
            new_car.goto(280, random.randint(-250, 250))
            new_car.speed(MOVE_INCREMENT)
            self.all_cars.append(new_car)

    def moving(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT




