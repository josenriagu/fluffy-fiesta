#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


rect = Rectangle(5, 4)
circ = Circle(4)

print(rect.area())
print(circ.area())
