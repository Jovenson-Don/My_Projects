import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.finish_line():
        scoreboard.update_level()
        player.start()
        car_manager.update_speed()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            screen.exitonclick()
