#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.


def migratoryBirds(arr):
    species = set(arr)
    dict1 = {}
    for specie in species:
        dict1[specie] = arr.count(specie)
    cur_max = max(dict1.values())
    highest = [i for i in dict1 if dict1[i] == cur_max]
    return sorted(highest)[0]


print(migratoryBirds([1, 4, 4, 4, 5, 3]))
print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
