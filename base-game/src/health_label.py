from pyglet.text import Label

from engine import window, add_to_updates, add_to_draws

from src.player import player

health_label = Label(
    f'Health: {str(player.health)}%',
    font_name='Arial',
    font_size=18,
    x=10, 
    y=window.height - 60,  # Positioned below the Points label
    anchor_x='left', 
    anchor_y='top'
)

def update_health_label_text(dt):
    health_label.text = f'Health: {str(player.health)}%'

add_to_updates(update_health_label_text)

add_to_draws(health_label.draw, 11)
