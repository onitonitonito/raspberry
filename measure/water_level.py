#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
'''This is example for LED Blinking
 GPIO Example (LED Blinking)
  #4 : DFRobot Water level sensor kit
  #5 : Arduino Water level sensor
'''

SENS = [ n for n in (2,3,4,12,27)]
PORTS = len(SENS)
COUNT = 1

# BroadCom Pin#
GPIO.setmode(GPIO.BCM)

for n in range(PORTS):
    GPIO.setup(SENS[n], GPIO.IN)

# GPIO.output(4,GPIO.HIGH)
# time.sleep(1)
# GPIO.output(4,GPIO.LOW)
# time.sleep(1)
# GPIO.output(23, False)
# GPIO.output(24, False)
# if GPIO.input(4) == 0:

try:
    while True:
        print('-------------- count: %s' % COUNT)

        for n in range(PORTS):
            print('GPIO#%s = %s' % (SENS[n], GPIO.input(SENS[n])))

        print()
        time.sleep(1)
        COUNT += 1

except KeyboardInterrupt:
        GPIO.cleanup()
