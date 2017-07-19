#!/usr/bin/python3
import time

from datetime import datetime
from sense_hat import SenseHat
from ..dot_8x32.greeting import TABLE, DICT #-----

hat = SenseHat()
hat.rotation = 0
hat.low_light = True

def get_color():
	color = {
		red : 	[255, 	0, 		0],
		green : [0,		150, 	0],
		blue : 	[0,		100,	255],
		white :	[130,	130,	130],
	}

def get_sense(hat):     # return (temp, humid, press as float)
    sense = {
        'temp'  : hat.temperature,
        'humid' : hat.humidity,
        'press' : hat.pressure,
    }
    return sense

color = get_color()			# <class 'dict'> = color
sense = get_sense(hat)		# <class 'dict'> = sense
table = TABLE %("DT()", sense['temp'], sense['humid'], sense['press'])

txt_01="HELLO SenseHat World!.. "
txt_02 ="Temp=%.1f'C.. " %sense['temp']
txt_03="Humid=%.1f%%.. " %sense['humid']
txt_04="Press= %6.2f mmBars.. " %sense['press']

def logging():
	print(table)
	print("\n\n", txt_01, txt_02, txt_03, txt_04)

def get_temperature_bar(hat):
	pixels = [color['red'] if i < sense['temp'] else color['white'] for i in range(64,0,-1)]
	hat.set_pixels(pixels)
	time.sleep(1.5)
	hat.show_message(txt_02,text_colour=color['red'],scroll_speed=0.03)

def get_humidity_bar():
	humidity_value = 64 * sense['humid'] / 100
	pixels = [color['blue'] if i < humidity_value else color['white'] for i in range(64,0,-1)]
	hat.set_pixels(pixels)
	time.sleep(1.5)
	hat.show_message(txt_03,text_colour=color['blue'],scroll_speed=0.03)

def get_pressure_bar():
	pressure_value = sense['press']* 0.0494 * ( 64 / 100)
	pixels = [color['green'] if i < pressure_value else color['white'] for i in range(64,0,-1)]
	hat.set_pixels(pixels)
	time.sleep(1.5)
	hat.show_message(txt_04,text_colour=color['white'],scroll_speed=0.03)

def main(hat):
	logging()

	hat.show_message(txt_01,text_colour=sense['green'],scroll_speed=0.025)

	get_temperature_bar()
	get_humidity_bar()
	get_pressure_bar()

	for i in range(2):
		hat.show_message( "%.1f"%sense['temp'], text_colour=color['red'],scroll_speed=0.03); time.sleep(0.5)
		hat.show_message( "%.1f"%sense['humid'], text_colour=color['blue'],scroll_speed=0.03); time.sleep(0.5)
		hat.show_message( "%4.2f"%sense['press'], text_colour=color['green'],scroll_speed=0.03); time.sleep(0.5)

# When import, it would not run..
if __name__ == '__main__':
	main(hat)
