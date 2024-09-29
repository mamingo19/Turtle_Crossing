import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
timmy = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(timmy.move_up, "Up")
screen.onkey(timmy.move_left, "Left")
screen.onkey(timmy.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    #Detect collision of turtle and cars
    for car in car_manager.all_cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            scoreboard.game_over()

    if timmy.win():
        timmy.reset()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()