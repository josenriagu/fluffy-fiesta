import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    appl = [apple+a for apple in apples]
    orang = [orange+b for orange in oranges]
    def counter(s, t, arr):
        count = 0
        for ar in arr:
            if s <= ar and ar <= t:
                count +=1
        return count
    print(counter(s,t,appl), counter(s,t,orang), sep="\n")

    # for the records
    print ("The outcome of this function is really: ",end="") 
    print ("Amazing")


countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])
