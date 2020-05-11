#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'filledOrders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k
#

def filledOrders(order, k):
    # Write your code here
    order.sort()
    count = 0
    for i in order:
        if i <= k:
            count += 1
            k = k - i
    return count


print(filledOrders([10, 30], 40))
print(filledOrders([5, 4, 6], 3))
print(filledOrders([5, 3, 3, 3, 4, 6], 9))
