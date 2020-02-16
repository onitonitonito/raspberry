#!/usr/bin/python3
from sense_hat import SenseHat

RED = 	[255, 0, 0]
GREEN = [0, 255, 0]
BLUE = 	[0, 0, 255]
WHITE=	[255,255,255]

hat = SenseHat()
hat.rotation = 180
hat.low_light = True

humidity = hat.humidity
humidity_value = 64 * humidity / 100
pixels = [GREEN if i < humidity_value else WHITE for i in range(64)]
hat.set_pixels(pixels)
