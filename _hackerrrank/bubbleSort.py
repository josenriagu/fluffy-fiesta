def countSwaps(a):
    # initialize variables
    swaps = 0  # hold the number of swaps
    restart = True  # checks if loop should restart
    while restart:
        # loop through length of array
        for i in range(len(a)):
            # if element is last element, already sorted
            if a[i] == a[len(a)-1]:
                # toggle restart to exit loop
                restart = False
                # break out of for loop
                break
            # if element is not the last element and the next element is greater
            if a[i] != a[len(a)-1] and a[i + 1] > a[i]:
                # continue
                continue
            # if element is not the last element and the next element is less
            if a[i] != a[len(a)-1] and a[i + 1] < a[i]:
                # initialize a temp variable to hold the next element
                temp = a[i + 1]
                # swap next element and current element
                a[i + 1], a[i] = a[i], temp
                # increment swaps
                swaps += 1
                # if previous element is now greater,
                if a[i - 1] > a[i]:
                    # break out of for loop and start afresh, since restart is True
                    break

    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a)-1]))


countSwaps([4, 2, 3, 1])


def countSwapsRecursive(a, swaps=0):
    for i in range(len(a)):
        if a[i] != a[len(a)-1] and a[i + 1] > a[i]:
            i += 1
        if a[i] != a[len(a)-1] and a[i + 1] < a[i]:
            temp = a[i + 1]
            # swap
            a[i + 1], a[i] = a[i], temp
            swaps += 1
            if a[i - 1] > a[i]:
                return countSwapsRecursive(a, swaps)
            else:
                i += 1

    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a)-1]))
