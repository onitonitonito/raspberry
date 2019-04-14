#! /usr/bin/python3
"""
# Pyfirmata LED(13) Blinking TEST
# Arduino Link with USB on Rpi3
# - INPUT   = 2, 3, 4, 5, 6, 7
# - OUTPUT  = 8, 9, 10, 11, 12, 13

"""

from pyfirmata import Arduino, util
import time

# initialize Serial Port
port = '/dev/ttyACM0'
BOARD = Arduino(port)

def main():
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()

def setup():
    global set_pins, pins_in, pins_out
    # gathering arr = in + out
    set_pins = []
    pins_in =  [ 2, 3, 4, 5, 6, 7]
    pins_out = [ 8, 9, 10, 11, 12, 13]

    # pin setup : i,o,p = input,output,pwm
    for n in pins_in:
        string = 'd:%s:i' % n
        set_pins.append(BOARD.get_pin(string))
        # pins_in[n].enable_reporting()

    for n in pins_out:
        string = 'd:%s:o' % n
        set_pins.append(BOARD.get_pin(string))
        # pins_out[n].enable_reporting()

    it = util.Iterator(BOARD)
    it.start()

def loop():
	count = 1
    while True:

        # if pins_in[0]: # pin.7 = HIGH --> (13):Built-in LED On
        #     BOARD.digital[pins_out[0]].write(1) else:
        #     BOARD.digital[pins_out[0]].write(0)
        print('__'*20, count)

        BOARD.digital[pins_out[-1]].write(1)
        a = BOARD.digital[pins_out[-1]].read()
        print('pins#%s = %s' %(pins_out[-1],a))
        time.sleep(0.5)

        BOARD.digital[pins_out[-1]].write(0)
        a = BOARD.digital[pins_out[-1]].read()
        print('pins#%s = %s' %(pins_out[-1],a))
        time.sleep(0.5)

        count += 1

if __name__ == '__main__':
    main()
