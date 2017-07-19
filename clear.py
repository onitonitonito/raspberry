#!/usr/bin/python3

import max7219.led as led

led = led.matrix(cascaded=4, vertical=True)
led.flush()
