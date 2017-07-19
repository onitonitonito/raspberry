#!/usr/bin/python3

import time
import max7219.led as led

from datetime import datetime
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

DICT = [
    {'Sun':'Sunday', 'Mon':'Monday', 'Tue':'Tuesday', 'Wed':'Wednesday',
    'Thu':'Thusday', 'Fri':'Friday', 'Sat':'Satureday'},

    {'Jan':'January', 'Feb':'February', 'Mar':'March', 'Apr':'April',
    'May':'May', 'Jun':'June', 'Jul':'July', 'Aug':'August', 'Sep':'September',
    'Oct':'October', 'Nev':'November', 'Dec':'December'}]

def get_greeting_message():
    dt = datetime.now()
    dvalue = dt.ctime().split()     # array str

    ts = dvalue[3].split(':')       # 23:34:57 -- time
    time_set = int(ts[0])           # 23

    if (time_set >=0 and time_set < 12):
        greeting = "Good Morning"
    elif (time_set >=12 and time_set < 18):
        greeting = "Good Afternoon"
    elif (time_set >=18 and time_set < 22):
        greeting = "Good Evening"
    else:
        greeting = "Good Night"

    message = "%s - %s!.. Today is %s %s %sth, %s"%(
		dvalue[3],				#'23:26:57'
        greeting,               # Good Evening!
        DICT[0][dvalue[0]],     # Monday
        DICT[1][dvalue[1]],     # July
        dvalue[2],              # day
        dvalue[4],              # year
    )
    return message

lcdh = led.matrix(cascaded=4, vertical=True)
lcdv = led.matrix(cascaded=4, vertical=False)

def sendh(txt,n):
    for i in range(n):
        #lcdh.show_message(txt, delay=0.02, font=proportional(SINCLAIR_FONT))
        #lcdh.show_message(txt, delay=0.02, font=SINCLAIR_FONT)        
        lcdh.show_message(txt, delay=0.02, font=proportional(CP437_FONT))
		#lcdh.show_message(txt, delay=0.02, font=CP437_FONT)
		
        print("shows ---> %i times of %i :: run %.2f%%"%( i+1, n , float( 100*(i+1)/n) ) )


def sendv(txt,n):
    for i in range(n):
        lcdv.show_message(txt, delay=0.06)

def clear():
    sendh("^_^  Clear!!",1)
    sendh("kkk",1)
    time.sleep(1)          # wait 1 sec
    
    lcdh.flush()
    lcdv.flush()


#txt = "%s  HELLO Raspberry Pi World! is going to be a whole new game.. \
#I hope you guys have a wonderful day & always remember I LOVE YOU, ^_^*   "%get_greeting_message()

txt = "hello today is wednesday and tomorrow is thursday  \
and tomorrow is my school vacation until July 20th ~ August 14th. yeahh (^O^)V \
I will have a great time like sleeping (@_@)       \
(-_-)a      ...      (o_o) oh! I have a great idea! I will go to the beach at saturday and swim there with my father\
bye bye guys (^^*)"

print(get_greeting_message())
print
print(txt)

clear()
sendh(txt,20)
clear()

