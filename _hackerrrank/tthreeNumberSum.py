# Complete the 'threeNumberSum' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER target
#


def threeNumberSum(arr, target):
    # Write your code here

    # sort list
    arr.sort()
    print(arr)
    # initialize variable to hold triplets
    triplets = []
    # loop
    for i in range(len(arr)):
        # condition to prevent index error
        if i > len(arr) - 2:
            continue
        # concatenate matched elements, reverse and loop
        for el in list(reversed(arr[i+2:]+arr[:i])):
            # if equal to target
            if arr[i] + arr[i+1] + el == target:
                # append to triplets list
                triplets.append([arr[i], arr[i+1], el])
        i += 1
    # reverse triplets
    triplets = list(reversed(triplets))

    # sort lists
    for ar in triplets:
        ar.sort()

    # remove identical lists
    for i, ar in enumerate(triplets):
        if i < len(triplets) - 1:
            if ar == triplets[i+1]:
                triplets.pop(i)

    # return triplets
    return triplets


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
# 3/5 test cases
