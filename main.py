from turtle import Turtle, Screen
from cars import Car, STARTING_MOVE_DISTANCE
import time
import random
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor('white')
screen.tracer(0)

player = Player()
car_manager = Car()
scoreboard = Scoreboard(position=(0,270))
x_boundaries = -300


screen.listen()
screen.onkey(player.advance, 'Up')

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_cars()
    car_manager.moving()

    if player.ycor() > 280:
        scoreboard.update_score()
        player.reseting_the_game()
        car_manager.level_up()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()



























screen.exitonclick()