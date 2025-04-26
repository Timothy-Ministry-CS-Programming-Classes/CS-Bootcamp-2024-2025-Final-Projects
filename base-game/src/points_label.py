from pyglet.text import Label

from engine import window, add_to_updates, add_to_draws

from src.player import player

points_label = Label(
    f'Points: {str(player.points)}%',
   font_name='Arial',
    font_size=18,
    x=10, 
    y=window.height - 30, 
    anchor_x='left', 
    anchor_y='top'
)

def update_points_label_text(dt):
    points_label.text = f'Points: {str(player.points)}'

add_to_updates(update_points_label_text)

add_to_draws(points_label.draw, 11)
