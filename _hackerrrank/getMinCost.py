import functools
import operator


def getMinimumCost(k, c):
    # sort array, so they start to buy highest per round
    c.sort()
    # initialize variables
    total = 0  # hold total spent
    buy_round = 0  # hold buy round
    # edge case: if number of friends equal to availabe flowers in c
    if k == len(c):
        # reduce c and return
        return functools.reduce(operator.add, c)
    # while c is greater than number of friends
    while len(c) > k:
        # if at first buy round
        if buy_round == 0:
            # reduce "k" upper part of c and add to total
            # slice c
            # increment buy round for next iteration
            total += functools.reduce(operator.add, c[len(c)-k:])
            c = c[:len(c)-k]
            buy_round += 1
        else:
            # multiply each element in "k" upper part of c by buy_round+1
            # reduce and add to total
            # slice c
            # increment buy round for next iteration
            mod_c = [(buy_round + 1)*el for el in c[len(c)-k:]]
            total += functools.reduce(operator.add, mod_c)
            c = c[:len(c)-k]
            buy_round += 1
        # if c is now less than number of friends
        if 0 < len(c) <= k:
            # multiply each element in "k" upper part of c by buy_round+1
            # reduce and add to total
            mod_c = [(buy_round + 1)*el for el in c]
            total += functools.reduce(operator.add, mod_c)
    return total


print(getMinimumCost(3, [2, 5, 6]))
print(getMinimumCost(3, [1, 3, 5, 7, 9]))
print(getMinimumCost(3, [1, 2, 2, 3, 5, 7, 9]))
