#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getBattery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY events as parameter.
#

def getBattery(events):
    # Write your code here
    charge = 50
    for level in events:
        charge += level
        if charge > 100:
            charge = 100
    return charge


print(getBattery([25, -30, 70, -10]))
