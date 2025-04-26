from pyglet.app import run

from engine import start

#scene
import src.background
import src.path

# moving items
import src.player
import src.obstacles

#label
import src.health_label
import src.points_label

#game over
import src.game_over

start()
run()
