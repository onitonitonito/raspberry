#!/usr/bin/python3
 
import time
import max7219.led as led

from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT
from random import randrange

device = led.matrix(cascaded=4, vertical=True)
         
def Brightness():
	global pos, asc
	 
	pos = 0
	asc = 65 		# int(ord('A')) = 65

	device.flush()
	time.sleep(1)	
	   
	for i in range(1000):
			
		if pos >= 4:
			pos = 0
			
		if asc >= 250:
			asc = 65	

		if pos <=3 and asc <=125:
			device.letter(pos, asc)		
			for intensity in xrange(8):
				device.brightness(intensity)
				time.sleep(0.1)

		asc +=1
		pos +=1	

def Orientation():
	
    time.sleep(1)
    device.letter(0, ord('l'))
    time.sleep(1)
    for _ in range():
        for angle in [0, 90, 180, 270]:
            device.orientation(angle)
            time.sleep(0.2)
         
def scroll_down():
    time.sleep(1)
    device.letter(0, ord('R'))
    time.sleep(1)
    for row in range(8):
        device.scroll_down()
        time.sleep(0.2)
     
def Inverse():
    device.letter(0, ord('A'))
    time.sleep(1)
    for _ in range(10):
        device.invert(1)
        time.sleep(0.25)
        device.invert(0)
        time.sleep(0.25)
 
def Font(delay):     
    time.sleep(1)
    device.show_message("Alternative font!", font=SINCLAIR_FONT, delay=delay)
     
    time.sleep(1)
    device.show_message("Proportional font - characters are squeezed together!", font=proportional(SINCLAIR_FONT),delay=delay)
     
    time.sleep(1)
    device.show_message(
    "Tiny is, I believe, the smallest possible font \
    (in pixel size). It stands at a lofty four pixels \
    tall (five if you count descenders), yet it still \
    contains all the printable ASCII characters.     ",
    font=proportional(TINY_FONT), delay=delay)
 
 
def CP437_Characters():
    time.sleep(1)
    for x in range(256):
    #    device.letter(1, 32 + (x % 64))
        device.letter(0, x)
        device.letter(1, x)
        device.letter(2, x)
        device.letter(3, x)

        time.sleep(0.5)
 
def Scrolling_pixel():
    while True:
        for x in range(500):
            device.pixel(17, 4, 1, redraw=False)
            direction = randrange(8)
            
            if direction == 7 or direction == 0 or direction == 1:
                device.scroll_up(redraw=False)
            if direction == 1 or direction == 2 or direction == 3:
                device.scroll_right(redraw=False)
            if direction == 3 or direction == 4 or direction == 5:
                device.scroll_down(redraw=False)
            if direction == 5 or direction == 6 or direction == 7:
                device.scroll_left(redraw=False)
     
            device.flush()
            time.sleep(0.005)
         
#Chay ham ban muon tai day                      

#Brightness()    # Change Brightness with 'A'
#Orientation()    # Rotating '1'
#scroll_down()    # set down vertical 'R'
#Inverse()
#Font(0.01)        # delay=0.01, change font
#CP437_Characters()
Scrolling_pixel()

device.flush()
