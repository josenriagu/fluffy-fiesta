import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    '''
    In order for the Kangaroos to meet at a point, either (not both) of the distance or jump should be greater or equal to the coresponding kangaroo
    Second condition to be met is that the distance + jump must be multiples of each other
    '''
    if ((x1 > x2 and v1 < v2) or (x2 > x1 and v2 < v1) or (x2 == x1 and v1 == v2)):
        if (x1 + v1)%(x2 + v2) == 0 or (x2 + v2)%(x1 + v1) == 0:
            return "YES"
        else:
            return "NO"
    return "NO"