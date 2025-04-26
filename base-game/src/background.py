from pyglet.shapes import Rectangle

from engine import window,add_to_draws
from config import config

b_config = config["background"]

background = Rectangle(0, 0, window.width, window.height, b_config["color"])

add_to_draws(background.draw,1)
