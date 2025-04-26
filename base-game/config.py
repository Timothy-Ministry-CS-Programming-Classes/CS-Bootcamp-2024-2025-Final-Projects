from const import colors

config = {
    "window": {
        "height":600,
        "width":800,
        "title":"Endless Runner"
    },
    "player":{
        "y":100,
        "speed":150,
        "image_location":"./assets/player.png",
        "min_x":200,
        "max_x":600,
        "starting_health":100
    },
    "obstacles":{
        "speed":200,
        "max_side_speed":300,
        "min_side_speed":50,
        "min_start_x":200,
        "max_start_x":600,
        "image_location":"./assets/obstacle.png",
        "damage":10,
        "add_rate":2
    },
    "background":{
        "color": colors["GREEN"]
    },
    "path":{
        "width":400,
        "x":200,
        "color":colors["GRAY"]
    }
}