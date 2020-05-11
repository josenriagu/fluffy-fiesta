import math
import os
import random
import re
import sys

# Complete the kangaroo function below.


def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and (v2 > v1 or v2 == v1):
        return "NO"
    elif x2 > x1 and v1 > v2:
        cur_first = x1
        cur_second = x2
        met = False
        while not met:
            cur_first += v1
            cur_second += v2
            if cur_first == cur_second:
                met = True
            if cur_first > cur_second:
                return "NO"
    return "YES"


print(kangaroo(0, 3, 4, 2))
print(kangaroo(0, 2, 5, 3))
print(kangaroo(14, 4, 98, 2))
print(kangaroo(42, 3, 94, 2))
print(kangaroo(21, 6, 47, 3))
print(kangaroo(43, 2, 70, 2))
