#!/usr/bin/python3

import numpy as np

from datetime import datetime
from time import sleep
from sense_hat import SenseHat

hat = SenseHat()

RED   = 	(255, 	0, 		0)
GREEN = 	(0, 	150, 	0)
BLUE  =     (0, 	100,	255)		# BlightBlue
WHITE =     (130,	130,	130)

def clamp(value, min_value, max_value):
    return min(max_value, max(min_value, value))

def scale(value, from_min, from_max, to_min=0, to_max=8):
    from_range = from_max - from_min
    to_range = to_max - to_min
    return (((value - from_min) / from_range) * to_range) + to_min

def render_bar(screen, origin, width, height, color):
    # Calculate the coordinates of the boundaries
    x1, y1 = origin
    x2 = x1 + width
    y2 = y1 + height

    # Invert the Y-coords so we're drawing bottom up
    max_y, max_x = screen.shape[:2]
    y1, y2 = max_y - y2, max_y - y1

    # Draw the bar
    screen[y1:y2, x1:x2, :] = color

def display_readings(hat):
    # Calculate the environment values in screen coordinates
    temperature_range = (0, 40)         # Max=40'c
    pressure_range = (0, 1013*2)      # Max= 2026 mmBars
    humidity_range = (0, 100)           # Max= 100 %

    temperature = scale(clamp(hat.temperature, *temperature_range), *temperature_range)
    humidity = scale(clamp(hat.humidity, *humidity_range), *humidity_range)
    pressure = scale(clamp(hat.pressure, *pressure_range), *pressure_range)

    # Render the bars
    screen = np.zeros((8, 8, 3), dtype=np.uint8)

    render_bar(screen, (0, 0), 2, round(temperature), color=RED)
    render_bar(screen, (3, 0), 2, round(humidity), color=BLUE)
    render_bar(screen, (6, 0), 2, round(pressure), color=GREEN)


    hat.set_pixels([pixel for row in screen for pixel in row])


def show_text(hat):
	hat.show_message("%.1f"%hat.temperature, text_colour=RED,scroll_speed=0.03); sleep(0.5)
	hat.show_message("%.1f"%hat.humidity, text_colour=BLUE,scroll_speed=0.03); sleep(0.5)
	hat.show_message("%4.2f"%hat.pressure, text_colour=GREEN,scroll_speed=0.03); sleep(0.5)


def echo_text(hat):
	dt = datetime.now()
	date = dt.strftime("%p %l:%M:%S - %h %dth (%a), %Y")
	TABLE='''
		%s
		+------------+-------------+
		| Temprature |    %.1f'c   |
		+------------+-------------+
		|  Humidity  |    %.1f%%    |
		+------------+-------------+
		|  Pressure  | %4.2f mmb |
		+------------+-------------+''' % (
	date, hat.temperature, hat.humidity, hat.pressure)

	print(TABLE, end="\n\n")


def main(hat):
    for i in range(5):
        echo_text(hat)         # echo to ..CONSOLE

        display_readings(hat)  # show bars
        sleep(60)              # wait 60 sec.
        show_text(hat)         # Show text


if __name__ == '__main__':
    main(hat)
