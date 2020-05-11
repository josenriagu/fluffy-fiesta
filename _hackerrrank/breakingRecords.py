#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.


def breakingRecords(scores):
    lowest = []
    highest = []
    for i in range(len(scores)):
        if i == 0:
            lowest.append(scores[i])
            highest.append(scores[i])
        else:
            if scores[i] < lowest[-1]:
                lowest.append(scores[i])
            if scores[i] > highest[-1]:
                highest.append(scores[i])

    return (len(highest) - 1, len(lowest) - 1)


print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))
print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
