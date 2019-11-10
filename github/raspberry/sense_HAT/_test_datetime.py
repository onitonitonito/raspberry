#!/usr/bin/python3
from datetime import datetime

dt = datetime.now()

# print(dt.strftime("%H:%M:%S - %h %dth (%a), %Y"))
print(dt.strftime("%p %I:%M:%S - %B %dth (%a), %Y"))
