def minAbsDiff(ar):
    # sort array
    ar.sort()
    # iniialize a variable to hold the minimum abs difference
    minimum = 0
    for i, el in enumerate(ar):
        # if i is 0, assign initial difference
        if i == 0:
            minimum = abs(el - ar[i+1])
        # else if i is last element index, continue
        elif i == len(ar) - 1:
            continue
        # else
        else:
            # if abs difference is smaller than minimum, assign too minimum
            if abs(el - ar[i+1]) < minimum:
                minimum = abs(el - ar[i+1])
    return minimum


print(minAbsDiff([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))
print(minAbsDiff([3, 0, -7]))
