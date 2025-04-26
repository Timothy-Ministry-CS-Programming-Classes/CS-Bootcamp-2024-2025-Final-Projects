from pyglet.image import load as loadImage
from pyglet.sprite import Sprite

from engine import (
    window, 
    keys, 
    key, 
    add_to_updates, 
    add_startup_function, 
    add_startup_schedule, 
    add_startup_update,
    add_to_draws
)

from config import config

from src.obstacles import obstacles, destroy_obstacle

#Use configs
p_config = config["player"]
y = p_config["y"]
x = window.width / 2
player_image_location = p_config["image_location"]
speed = p_config["speed"]
min_x = p_config["min_x"]
max_x = p_config["max_x"]
starting_health = p_config["starting_health"]

#load image and set anchor to center
player_image = loadImage(player_image_location)  # Ensure this file exists
half_width = player_image.width / 2
half_height = player_image.height / 2
player_image.anchor_x = int(half_width)
player_image.anchor_y = int(half_height)

player = Sprite(player_image, x=x, y=y)

player.speed = speed
player.health = starting_health
player.points = 0  

player.half_height = half_height
player.half_width = half_width

def player_move(dt):
    if keys[key.LEFT]:
        player.x -= player.speed * dt
    if keys[key.RIGHT]:
        player.x += player.speed * dt

    if player.x > max_x - player.half_width:
        player.x = max_x - player.half_width
    if player.x < min_x + player.half_width:
        player.x = min_x + player.half_width

def take_damage(dmg=0):
     player.health = player.health - dmg

def check_collision(dt=None):
    for obstacle in obstacles:
        if abs(obstacle.x - player.x) < (obstacle.half_width + player.half_width):
            if abs(obstacle.y - player.y) < (obstacle.half_height + player.half_height):
                take_damage(obstacle.damage)
                destroy_obstacle(obstacle)

def add_point(dt):
    player.points += 1

def reset_starting_values():
    player.speed = speed
    player.health = starting_health
    player.points = 0
    player.x = x

add_to_updates(check_collision)

add_startup_function(reset_starting_values)

add_startup_schedule(add_point,1)
add_startup_update(player_move)

add_to_draws(player.draw,10)# Technically you can have any number of layers, but 10 is a good one to be the top.
