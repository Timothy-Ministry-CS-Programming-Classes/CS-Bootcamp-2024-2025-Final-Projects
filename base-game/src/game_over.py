from pyglet.text import Label

from engine import (
    window,
    add_startup_update,
    add_to_draws,
    add_mouse_event,
    remove_mouse_event, 
    start,
    pause
)

from const import colors

from src.player import player

game_over = False

def click_to_restart(x,y,button, modifiers):#We could make the button clickable
    global game_over
    remove_mouse_event(click_to_restart)
    game_over = False
    start()

def check_for_game_over(dt):
    global game_over
    if player.health <= 0:
        game_over = True
        pause()
        add_mouse_event(click_to_restart)

def show_game_over_when_game_over():
    if game_over:
        draw_game_over()


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

add_startup_update(check_for_game_over)

add_to_draws(show_game_over_when_game_over, 12)
