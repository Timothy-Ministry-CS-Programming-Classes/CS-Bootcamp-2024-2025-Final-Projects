from random import randint,choice as randchoice

from pyglet.image import load as loadImage
from pyglet.sprite import Sprite

from engine import (
    window, 
    add_startup_function, 
    add_startup_schedule, 
    add_startup_update,
    add_to_draws
)
from config import config

o_config = config["obstacles"]
obstacle_image_location = o_config["image_location"]
min_x = o_config["min_start_x"]
max_x = o_config["max_start_x"]
speed = o_config["speed"]
min_side_speed = o_config["min_side_speed"]
max_side_speed = o_config["max_side_speed"]
add_rate = o_config["add_rate"]
damage = o_config["damage"]

obstacle_image = loadImage(obstacle_image_location)

half_height = obstacle_image.height / 2
half_width = obstacle_image.width / 2

obstacle_image.anchor_x = int(half_width)
obstacle_image.anchor_y = int(half_height)

obstacles = []

def add_obstacle(dt=None):
    obstacle = Sprite(obstacle_image)
    obstacle.half_height = half_height
    obstacle.half_width = half_width
    obstacle.damage = damage or 0
    obstacle.dir = randchoice(['left', 'right'])
    obstacle.side_speed = randint(min_side_speed, max_side_speed)

    x = randint(int(min_x + (obstacle.half_width)), int(max_x - (obstacle.half_width)))
    obstacle.x = x
    obstacle.y = window.height + (obstacle.half_height)
    obstacles.append(obstacle)

def move_obstacles(dt):
    for obstacle in obstacles[:]:
        obstacle.y -= speed * dt
        if(obstacle.dir == 'left'):
            obstacle.x -= obstacle.side_speed * dt
            if obstacle.x < min_x + (obstacle.half_width):
                obstacle.x = min_x + (obstacle.half_width)
                obstacle.dir = 'right'
        if(obstacle.dir == 'right'):
            obstacle.x += obstacle.side_speed * dt
            if obstacle.x > max_x - (obstacle.half_width):
                obstacle.x = max_x - (obstacle.half_width)
                obstacle.dir = 'left'

        if obstacle.y + (obstacle.half_height) < 0:
            destroy_obstacle(obstacle)

def draw_obstacles():
    for obstacle in obstacles[:]:
        obstacle.draw()

def destroy_obstacle(obstacle):
    obstacle.delete()
    obstacles.remove(obstacle)

def reset_all_obstacles():
    for obstacle in obstacles[:]:
        obstacle.delete()
    obstacles.clear()

add_startup_function(reset_all_obstacles)

add_startup_schedule(add_obstacle, add_rate)

add_startup_update(move_obstacles)

add_to_draws(draw_obstacles, 10)

