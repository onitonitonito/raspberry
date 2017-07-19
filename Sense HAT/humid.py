#!/usr/bin/python3

from sense_hat import SenseHat

RED = 		[255, 0, 0]
GREEN = 	[0, 255, 0]
BLUE = 	[0, 0, 255]
WHITE=	[255,255,255]

sense = SenseHat()
sense.rotation = 180
sense.low_light = True

humidity = sense.humidity
humidity_value = 64 * humidity / 100
pixels = [GREEN if i < humidity_value else WHITE for i in range(64)]
sense.set_pixels(pixels)
