import functools
import operator


def luckBalance(k, contests):
    # filter important contests
    important = []
    # initialize variable to hold total luck
    total = 0
    # loop
    for arr in contests:
        # increment total by element at index 0
        total += arr[0]
        # if element at index 1 is 1,
        if arr[1] == 1:
            # append to important
            important.append(arr[0])
    # CASES:
    # 1. if no important game, can lose all. return total
    # 2. if important is less than total permissible loss - "k", return total
    if len(important) == 0 or len(important) < k:
        return total
    # sort important
    important.sort()
    # slice the important games with least luck up to "k"
    can_win = (important[:len(important) - k])
    # reduce the list
    count_can_win = functools.reduce(operator.add, can_win)
    # return total - twice count_can_win - because it was included initially
    return total - (count_can_win * 2)


values = []
# read test case file and load contests
with open("luckBalance.in") as f:
    values = f.readlines()
    # remove first line
    values = values[1:]
    for index, value in enumerate(values):
        value = value.split(" ")
        values[index] = [int(value[0]), int(value[1])]


print(luckBalance(58, values))
