import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    # initialize variables
    pos = 0
    neg = 0
    zeros = 0
    for i in range (0, len(arr)):
        if (arr[i] > 0):
            pos += 1
        elif (arr[i] == 0):
            zeros += 1
        elif (arr[i] < 0):
            neg += 1
    print(pos, neg, zeros)
    print("%.6f\n%.6f\n%.6f\n" % (pos/len(arr), neg/len(arr), zeros/len(arr)))

plusMinus([-4, 3, -9, 0, 4, 1 ])