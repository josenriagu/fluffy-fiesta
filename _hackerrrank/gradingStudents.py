import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for idx, grade in enumerate(grades):
        # check if the grade is at least 38 and that the remainder when divided by 5 is at least 3
        if grade >= 38 and grade % 5 >= 3:
            # if so, then increment the quotient by 1 and multiply back by 5
            grades[idx] = ((grade // 5) + 1) * 5
    return grades

print(gradingStudents([73, 67, 38, 33]))