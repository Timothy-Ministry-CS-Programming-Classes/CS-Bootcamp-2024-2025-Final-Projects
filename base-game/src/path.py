from pyglet.shapes import Rectangle

from engine import window,add_to_draws
from config import config

b_config = config["path"]
color = b_config["color"]
x = b_config["x"]
width= b_config["width"]
path = Rectangle(x, 0, width, window.height, b_config["color"])

add_to_draws(path.draw, 2)
