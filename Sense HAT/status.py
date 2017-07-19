#!/usr/bin/python3

import time

from datetime import datetime
from sense_hat import SenseHat

RED = 		[255, 	0, 		0]
GREEN = 	[0, 		150, 	0]
BLUE = 	[0, 		100,		255]		# BlightBlue
WHITE=	[130,	130,		130]

sense = SenseHat()
sense.rotation = 0
sense.low_light = True

temp = sense.temp
humid= sense.humidity
press= sense.pressure

TABLE='''
	+------------+-------------+
	| Temprature |    %.1f'c   |
	+------------+-------------+
	|  Humidity  |    %.1f%%    |
	+------------+-------------+
	|  Pressure  | %4.2f mmb |
	+------------+-------------+'''%(temp, humid, press)


txt_01="HELLO SenseHat World!.. "
txt_02 ="Temp=%.1f'C.. " %temp
txt_03="Humid=%.1f%%.. " %humid
txt_04="Press= %6.2f mmBars.. " %press

def logging():
	print(TABLE)
	print("\n\n", txt_01, txt_02, txt_03, txt_04)

def get_temperature_bar():
	pixels = [RED if i < temp else WHITE for i in range(64,0,-1)]
	sense.set_pixels(pixels)	
	time.sleep(1.5)
	sense.show_message(txt_02,text_colour=RED,scroll_speed=0.03)

def get_humidity_bar():
	humidity_value = 64 * humid / 100
	pixels = [BLUE if i < humidity_value else WHITE for i in range(64,0,-1)]
	sense.set_pixels(pixels)
	time.sleep(1.5)
	sense.show_message(txt_03,text_colour=BLUE,scroll_speed=0.03)

def get_pressure_bar():
	pressure_value = press* 0.0494 * ( 64 / 100)
	pixels = [GREEN if i < pressure_value else WHITE for i in range(64,0,-1)]
	sense.set_pixels(pixels)
	time.sleep(1.5)
	sense.show_message(txt_04,text_colour=WHITE,scroll_speed=0.03)


if __name__ == '__main__':
	logging()
	
	sense.show_message(txt_01,text_colour=GREEN,scroll_speed=0.025)

	get_temperature_bar()
	get_humidity_bar()
	get_pressure_bar()
	
	for i in range(5):
		sense.show_message( "%.1f"%temp, text_colour=RED,scroll_speed=0.03); time.sleep(0.5)
		sense.show_message( "%.1f"%humid, text_colour=BLUE,scroll_speed=0.03); time.sleep(0.5)
		sense.show_message( "%4.2f"%press, text_colour=GREEN,scroll_speed=0.03); time.sleep(0.5)
