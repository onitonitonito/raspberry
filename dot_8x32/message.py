#!/usr/bin/python3
from datetime import datetime

import max7219.led as led
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT
from . import clear, func_dot

lcdh = led.matrix(cascaded=4, vertical=True)
lcdv = led.matrix(cascaded=4, vertical=False)

TABLE='''   %s
	+------------+-------------+
	| Temprature |    %.1f'c   |
	+------------+-------------+
	|  Humidity  |    %.1f%%    |
	+------------+-------------+
	|  Pressure  | %4.2f mmb |
	+------------+-------------+'''

DICT = [
    {'Sun': 'Sunday', 'Mon': 'Monday', 'Tue': 'Tuesday', 'Wed': 'Wednesday',
    'Thu': 'Thusday', 'Fri': 'Friday', 'Sat': 'Satureday'},

    {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April',
    'May': 'May', 'Jun': 'June', 'Jul': 'July', 'Aug': 'August', 'Sep': 'September',
    'Oct': 'October', 'Nev': 'November', 'Dec': 'December'}]

# txt = "%s  HELLO Raspberry Pi World! is going to be a whole new game.. \
# I hope you guys have a wonderful day & always remember I LOVE YOU, ^_^* \
#  " % get_greeting()

txt = "Hello today is wednesday and tomorrow is thursday  \
and tomorrow is my school vacation until July 20th ~ August 14th. yeahh (^O^)V \
I will have a great time like sleeping (@_@) (-_-)a ... (o_o) \
oh! I have a great idea! I will go to the beach at saturday and swim there \
with my father.. bye bye guys (^^*)"


def get_greeting():
	dt = datetime.now()
	dvalue = dt.ctime().split()     # array str
	time_12 = dt.strftime("%p %l:%M:%S")

	ts = dvalue[3].split(':')       # 23:34:57 -- time
	time_set = int(ts[0])           # 23

	if (time_set >= 0 and time_set < 12):
		greet = "Good Morning"
	elif (time_set >= 12 and time_set < 18):
		greet = "Good Afternoon"
	elif (time_set >= 18 and time_set < 22):
		greet = "Good Evening"
	else:
		greet = "Good Night"

	greeting = "%s - %s!.. Today is %s %s %sth, %s" % (
		# dvalue[3],			# '23:26:57'
		time_12,				# 'PM 11:15:54'
		greet,               	# Good Evening!
		DICT[0][dvalue[0]],     # Monday
		DICT[1][dvalue[1]],     # July
		dvalue[2],              # 17th
		dvalue[4],              # 2017
	)
	return greeting				# <class 'str'> greeting


def sendh(txt, n, delay=0.02, font=SINCLAIR_FONT):
	for i in range(n):
		# font=SINCLAIR_FONT, CP437_FONT, proportional(SINCLAIR_FONT)
		print("show_h ---> %i times of %i :: run %.2f%%" % (i+1, n, float(100*(i+1)/n)))
		lcdh.show_message(txt, delay=delay, font=font)


def sendv(txt, n, delay=0.06, font=SINCLAIR_FONT):
	for i in range(n):
		print("show_v ---> %i times of %i :: run %.2f%%" % (i+1, n, float(100*(i+1)/n)))
		lcdv.show_message(txt, delay=delay, font=font)


def main(lcdh):
	print(get_greeting(), "\n")       # return <class 'str'> greeting
	print(txt)

	clear.main(lcdh)
	sendh(txt, 2)
	clear.main(lcdh)

# When import, it would not run..
if __name__ == '__main__':
	main(lcdh)
