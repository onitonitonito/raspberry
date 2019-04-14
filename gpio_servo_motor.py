#! /usr/bin/python

import time
import RPi.GPIO as GPIO

# Define Using PinNo and Other Variables
PWM_PIN = 18

def main():
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()

def setup():
    global pwm

    # Initializing GPIO Port
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PWM_PIN, GPIO.OUT)

    # Initializing Pin for PWM
    pwm = GPIO.PWM(PWM_PIN, 50)
    pwm.start(7.5)

def loop():
    while True:
        # Duty Change
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)

        # Duty Change
        pwm.ChangeDutyCycle(12.5)
        time.sleep(1)

        # Duty Change
        pwm.ChangeDutyCycle(2.5)
        time.sleep(3)


if __name__ == '__main__':
    main()
