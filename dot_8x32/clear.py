#!/usr/bin/python3
import max7219.led as led

led = led.matrix(cascaded=4, vertical=True)

def clear(led):
    led.flush()

def main(led):
    clear(led)

# When import, it would not run..
if __name__ == '__main__':
    main(led)
