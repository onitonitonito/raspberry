#!/usr/bin/python3
from sense_hat import SenseHat
hat = SenseHat()

def clear(hat):
    hat.show_message(" ",text_colour=[0,0,0],scroll_speed=0.03)

def main(hat):
    clear(hat)

# When import, it would not run..
if __name__ == '__main__':
    main(hat)
