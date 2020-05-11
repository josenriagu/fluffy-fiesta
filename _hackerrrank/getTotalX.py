#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    # Write your code here
    a.sort()
    b.sort()
    '''
    find elements that exist between the end of a and start of b, such that;
    it is a multiple of all elements in a and a factor of all elements in b
    '''
    elements = [i for i in range(a[-1], b[0] + 1) if all(map(lambda x: i % x == 0, a)) and all(map(lambda x: x % i == 0, b))]

    '''
    breakdown
    '''
    # elements = [i for i in range(a[-1], b[0] + 1) if i %  a[0] == 0 and i % a[-1] == 0]
    # count = 0
    # for el in elements:
    #     if all(map(lambda x: x % el == 0, b)):
    #         count += 1
    # return count


    return len(elements)


print(getTotalX([2, 6], [24, 36]))
print(getTotalX([2, 4], [16, 32, 96]))
print(getTotalX([3, 9, 6], [36, 72]))
