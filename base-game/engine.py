#Student. You should not need to modify this file. 
# AGAIN DO NOT EDIT UNLESS YOU KNOW WHAT YOU ARE DOING!
from pyglet.window import Window, key
from pyglet.clock import schedule_interval, unschedule

from config import config

# Updates
updates = []
def add_to_updates(func):
    updates.append(func)

def remove_from_updates(func):
    if func in updates:
        updates.remove(func)

def update(dt):
    for update in updates:
        update(dt)

#drawing
draws = []

def add_to_draws(func, layer=0):
    draws.append({"func": func, "layer": layer})

def remove_from_draws(func):
    global draws
    draws = [item for item in draws if item["func"] != func]

def draw():
    for item in sorted(draws, key=lambda d: d["layer"]):
        item["func"]()


#scheduling
schedules = []
def add_to_schedules(func, schedule):
    schedule_interval(func,schedule)
    schedules.append(func)

def remove_from_schedules(func):
    unschedule(func)
    if func in schedules:
        schedules.remove(func)

def remove_all_schedules():
    for func in schedules:
        unschedule(func)
    schedules.clear()

# Mouse events
mouse_events = []
def add_mouse_event(func):
    mouse_events.append(func)

def remove_mouse_event(func):
    if func in mouse_events:
        mouse_events.remove(func)

def mouse_event(x, y, button, modifiers):
    for func in mouse_events:
        func(x, y, button, modifiers)

#window
window = Window(width=config["window"]["width"], height=config["window"]["height"], caption=config["window"]["title"])

keys = key.KeyStateHandler()
window.push_handlers(keys)

@window.event
def on_draw():
    window.clear()
    draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    mouse_event(x,y,button,modifiers) 

# Start items
starts = []

def start():
    for startup in starts:
        startup["func"]()

def pause():
    for startup in starts:
        if startup["type"] == "schedule":
            remove_from_schedules(startup["oFunc"])
        if startup["type"]=="update":
            remove_from_updates(startup["oFunc"])
    pass

def add_startup_function(func):
    starts.append({"type":"func","func":func})

def add_startup_schedule(func, rate):
    starts.append({"type":"schedule", "func":lambda:add_to_schedules(func,rate), "oFunc":func})

def add_startup_update(func):
    starts.append({"type":"update", "func":lambda:add_to_updates(func),"oFunc":func})

#This is the engine running. 
schedule_interval(update,1/60)