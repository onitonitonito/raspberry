#!/usr/bin/python3
from pyfirmata import Arduino, util
import sys, time
'''  Arduino Shield - Digital INPUT.
 DFRobot Non-contact Liquid Level Sensor XKC-Y25-T12V SKU: SEN0204
 #1, 7, 8, 15 : DFRobot Water level sensor kit
 #21,20,16,12 : Arduino Water level sensor
'''

INTERVAL = 1              # in second

# Creates a new BOARD
PORT = '/dev/ttyACM0'       # Extention Port
BOARD = Arduino(PORT)

# Definition of the analog pin
# PINS = (0, 1, 2, 3)
PINS = (0, 1, 2, 3, 4, 5)
print("Setting up the connection to the BOARD ...")

it = util.Iterator(BOARD)
it.start()

def setup():
    # Start reporting for defined pins
    for pin in PINS:
        BOARD.analog[pin].enable_reporting()

def loop():
    count = 1
    while True:
        # Loop for reading the input. Duration approx. 10 s
        print("\nValues after %s second(s) --- %s times " % (INTERVAL, count))

        for pin in PINS:
            print("Pin A%i : %s" % (pin, BOARD.analog[pin].read()))
        BOARD.pass_time(INTERVAL)
        count += 1

def main():
    setup()

    try:
        loop()
    except KeyboardInterrupt:
        sys.exit()
        BOARD.exit()

if __name__ == '__main__':
    main()
