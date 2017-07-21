#!/usr/bin/python3
import time
from datetime import datetime
from random import randrange

from sense_hat import SenseHat
from dot_8x32.greeting import DICT, TABLE, sendh, sendv, get_greeting

hat = SenseHat()
hat.rotation = 0
hat.low_light = True

def get_sense(hat):     # return (temp, humid, press as float)
    sense = {
        'temp'  : hat.temperature,
        'humid' : hat.humidity,
        'press' : hat.pressure,
    }
    return sense

def echo_text(hat):
	sense = get_sense(hat)      # <class 'DICT'>    **sense
	greeting = get_greeting()	# from dot_8x32.greeing.py

	txt01="%s.. \nHELLO SenseHat!.. this is with 8x32 DOT.. \n" % greeting
	txt02="Temp=%.1f'C " % sense['temp']
	txt03="Humid=%.1f %% " % sense['humid']
	txt04="Press=%6.2fmmBars " % sense['press']

	dt = datetime.now()
	date = dt.strftime("%H:%M:%S - %h %dth (%a), %Y")

	global mssg
	table = TABLE % (date, sense['temp'], sense['humid'], sense['press'] )
	mssg = "%s\n%s %s %s"%(txt01,txt02,txt03,txt04)

	print(table, end="\n\n")
	print(mssg)

def main(hat):
	for i in range(2):
		echo_text(hat)
		sendh(mssg,1)

		time.sleep(7)

	func.main()

# When import, it would not run..
if __name__ == '__main__':
	main(hat)
