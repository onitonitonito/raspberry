#!/usr/bin/python3
"""
# SenseHat Joy Stick

"""
from sense_hat import SenseHat

# Draw the foreground (fg) into a numpy array
Rd = (255, 0, 0)
Gn = (0, 255, 0)
Bl = (0, 0, 255)
Gy = (128, 128, 128)
__ = (0, 0, 0)

x = y = 4
(x,y) = 4

hat = SenseHat()

hat.rotation = 0
hat.low_light = True

def update_screen():
    hat.clear()
    hat.set_pixel(x, yclear, 255, 255, 255)

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def move_dot(event):
    global x, y
    if event.action in ('pressed', 'held'):
        x = clamp(x + {'left': -1, 'right': 1,}.get(event.direction, 0))
        y = clamp(y + {'up': -1, 'down': 1,}.get(event.direction, 0))

def main():
    update_screen()

    while True:
        for event in hat.stick.get_events():
            move_dot(event)
            update_screen()

if __name__ == '__main__':
    main()
