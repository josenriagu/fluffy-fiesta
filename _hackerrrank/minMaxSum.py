import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.


def miniMaxSum(arr):
    # sort array to make sum easier
    arr.sort()
    # hold the popped last item so we can append it back
    popped = arr.pop(len(arr) - 1)
    min_sum = sum(arr)
    arr.append(popped)
    # pop first index this time
    arr.pop(0)
    max_sum = sum(arr)
    print("{} {}".format(min_sum, max_sum))


miniMaxSum([0, 1, 2, 3, -4, 5])
