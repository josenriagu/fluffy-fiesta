def rotLeft(a, d):
    # loop
    while d != 0:
        # remove first element
        c = a.pop(0)
        # add it to the back
        a.append(c)
        # decrement rotation count
        d -= 1
    return a


print(rotLeft([1, 2, 3, 4, 5], 4))
