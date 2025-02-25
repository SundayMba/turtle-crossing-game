import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import pygame

pygame.mixer.init()
screen = Screen()
screen.setup(width=800, height=800)
screen.tracer(0)
player = 'raccoon2.gif'    
car = 'attacker2.gif'
screen.register_shape(player)
screen.register_shape(car)
pygame.mixer.music.load("shoot.mp3")    

def play_music():
    pygame.mixer.music.play()

player = Player(player, play_music)
car_manager = CarManager(car)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")
# screen.onkey(pygame.mixer.music.play, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
