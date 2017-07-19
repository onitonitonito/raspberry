#!/usr/bin/python3


from sense_hat import SenseHat

RED = 		[255, 0, 0]
GREEN = 	[0, 255, 0]
BLUE = 	[0, 0, 255]
WHITE=	[255,255,255]

sense = SenseHat()
sense.rotation = 180
sense.low_light = True

temp = sense.temp
pixels = [RED if i < temp else BLUE for i in range(64)]
sense.set_pixels(pixels)
