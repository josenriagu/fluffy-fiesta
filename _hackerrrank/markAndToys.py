#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.


def maximumToys(prices, k):
    prices.sort()
    count = 0
    total = 0
    for price in prices:
        if total + price <= k:
            total += price
            count += 1
    return count


maximumToys([1, 12, 5, 111, 200, 1000, 10], 50)
