#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    newS = ""
    for i in range(len(sentence)):
        if sentence[i].isupper():
            newS += sentence[i].lower()
        elif sentence[i].islower():
            newS += sentence[i].upper()
        else:
            newS += sentence[i]

    return " ".join(reversed(newS.split(" ")))


print(reverse_words_order_and_swap_cases("rUns dOg"))
