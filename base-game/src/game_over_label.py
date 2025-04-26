from pyglet.text import Label

from engine import window

from const import colors

game_over_label = Label(
    'Game Over',
    font_name='Arial',
    font_size=36,
    x=window.width // 2,
    y=window.height // 2 + 20,  # Centered
    anchor_x='center', 
    anchor_y='center',
    color=colors["RED"]  # Red color
)
click_to_restart_label = Label(
    'Click To Restart',
    font_name='Arial',
    font_size=24,
    x=window.width // 2,
    y=window.height // 2 - 46,  # Centered
    anchor_x='center', 
    anchor_y='center',
    color=colors["BLACK"]  # Red color
)

def draw_game_over():
    game_over_label.draw()
    click_to_restart_label.draw()