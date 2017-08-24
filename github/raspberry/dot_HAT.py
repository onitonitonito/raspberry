#!/usr/bin/python3
import time
import echo_HAT as eh

from dot_8x32 import func_dot as fd     # font(0.01)
from dot_8x32 import message as ms     # DICT, TABLE, sendh, sendv, get_greeting
from dot_8x32 import clear as dc

from sense_HAT import bars
from sense_HAT import clear as hc

mssg = eh.get_message()      # <class 'array'> message
message = "%s %s %s %s"% (mssg[0],mssg[1],mssg[2],mssg[3])

def main():
	bars.display_readings(bars.hat)

	for i in range(2):
		eh.echo_text(eh.hat)
		ms.sendh(message, 1, font=ms.proportional(ms.SINCLAIR_FONT))
		time.sleep(7)

	hc.main(hc.hat)
	fd.main()
	dc.main(dc.led)


# When import, it would not run..
if __name__ == '__main__':
	main()
