#! /usr/bin/python
"""
# function append() should have just 1 argument
# ( not multipule arguments )
"""

SENS = []
SENS[len(SENS):len(SENS)+1] = (1, 7, 8, 25)
SENS[len(SENS):len(SENS)+1] = (21, 20, 16, 12)
print(SENS)

SENS = []
SENS.extend((1, 7, 8, 25))
SENS.extend((21, 20, 16, 12))
print(SENS)

SENS = []
SENS.append([1, 7, 8, 25])
SENS.append([24, 23])
SENS.append([18, 15, 14])
print(SENS)
