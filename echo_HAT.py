#!/usr/bin/python3
from sense_hat import SenseHat

from dot_8x32 import message as ms  # DICT, TABLE, sendh, sendv, get_greeting
from sense_HAT import func_HAT as fh # get_sense,

hat = SenseHat()

sense = fh.get_sense(hat)       # <class 'DICT'>    **sense
greeting = ms.get_greeting()	# <class 'str'> from dot_8x32.greeing.py

def get_message():
    hello="%s.. \nHELLO SenseHat!.. this is with 8x32 DOT.. \n" % greeting
    temp="Temp=%.1f'C " % sense['temp']
    humid="Humid=%.1f %% " % sense['humid']
    press="Press=%6.2fmmBars " % sense['press']

    message = [hello, temp, humid, press]
    return message              # <class 'array'>, message

def echo_text(hat):
    message =  get_message()    # <class 'array'>, message
    table = ms.TABLE % ( greeting, sense['temp'], sense['humid'], sense['press'] )

    print(table, "\n\n")
    print("%s \n %s %s %s "% (message[0],message[1],message[2],message[3]) )

if __name__ == '__main__':
    echo_text(hat)
