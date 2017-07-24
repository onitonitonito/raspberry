#!/usr/bin/python3
from dot_HAT import echo_text
from sense_hat import SenseHat

hat = SenseHat()

if __name__ == '__main__':
    echo_text(hat)
