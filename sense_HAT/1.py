#!/usr/bin/python3

from datetime import datetime, date

dt = datetime.now()

print(dt.strftime("%H:%M:%S - %h %dth (%a), %Y"))
