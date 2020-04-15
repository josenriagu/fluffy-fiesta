import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    numbers = set(arr)
    count = 0
    for i in arr:
        if i + k in numbers:
            count += 1

    return count

print(pairs(2, [1, 3, 5, 8, 6, 4, 2]))