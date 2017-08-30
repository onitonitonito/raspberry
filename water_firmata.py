#!/usr/bin/python3
from pyfirmata import Arduino, util
import sys, time
'''  Arduino Shield - Digital INPUT.
 DFRobot Non-contact Liquid Level Sensor XKC-Y25-T12V SKU: SEN0204
 #1, 7, 8, 15 : DFRobot Water level sensor kit
 #21,20,16,12 : Arduino Water level sensor
'''

INTERVAL = 0.5              # in second
PORT = '/dev/ttyACM0'       # Extention Port
BOARD = Arduino(PORT)
pins_num = (8, 9, 10, 11)

def setup():
    pins = []
    for n in pins_num:
        pins.append(BOARD.get_pin('d:%s:i' % n))

def loop():
    count = 1
    while True:
        print("__"*20,  count)
        for n in pins_num:
            print("pin#%s = %s" % (n, BOARD.digital[n].read()))
        print()
        count += 1
        time.sleep(INTERVAL)

def main():
    setup()

    try:
        loop()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
