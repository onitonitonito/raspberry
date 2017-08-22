#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
'''  RPi.GPIO modul - Digital INPUT.
 DFRobot Non-contact Liquid Level Sensor XKC-Y25-T12V SKU: SEN0204
 # 20,16,12 : Arduino Water level sensor
'''

SENS = []
SENS.extend((14, 15, 18))		# Arduino Sensors
SENS.extend((23, 24))			# Blank
SENS.extend((25, 8, 7, 1))		# XKC-Y25-T12V SKU: SEN0204

PORTS = len(SENS)

def setup():
    # BroadCom Chip Pin# Set
    GPIO.setmode(GPIO.BCM)
    for n in range(PORTS):
        GPIO.setup(SENS[n], GPIO.IN)

def loop():
    COUNT = 1
    while True:
        print('-------------- count: %s' % COUNT)

        for n in range(PORTS):
            num_bcm = str()
            read_bcm = GPIO.input(SENS[n])

            if SENS[n] >= 10:
                num_bcm = str(SENS[n])
            else:
                num_bcm = '0' + str(SENS[n])
            print('GPIO# %s = %s' % (num_bcm, read_bcm))

        print()
        time.sleep(1)
        COUNT += 1


def main():
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
