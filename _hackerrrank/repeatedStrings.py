import math


def repeatedString(s, n):
    # initialize variables
    count_a = s.count("a")  # occurences of "a" in original string
    occurences = count_a * (n // len(s)) # occurences of "a" in extended string

    # CASES
    # if no "a" in string
    if count_a == 0:
        # return 0
        return 0
    # else if string has only a's
    elif count_a == len(s):
        # return n
        return n
    # else if n is wholly divisible by length of string
    elif n % len(s) == 0:
        # return occurences
        return occurences
    # else if n is not wholly divisible by length of string
    elif n % len(s) != 0:
        # find quotient
        quotient = math.floor(n / len(s))
        # find remainder
        remainder = n - (len(s) * quotient)
        # return occurences plus count of "a" in remaining slice of s to make up n
        return occurences + (s[:remainder].count("a"))


print(repeatedString("abcac", 10))
