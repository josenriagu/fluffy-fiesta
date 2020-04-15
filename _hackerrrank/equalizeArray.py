def equalizeArray(arr):
    # form a set of values in arr
    arr_set = set(arr)
    # initialize variables
    current_max = 0  # hold currently maximum iterable count
    # iterate through set
    for el in arr_set:
        # count occurences in original array
        el_count = arr.count(el)
        # if greater than current_max
        if el_count > current_max:
            # assign to current_max
            current_max = el_count
    # length of arr minus current max shows
    # minimum number of deletions to get equal elements
    return len(arr) - current_max


print(equalizeArray([24, 29, 70, 43, 12, 27, 29, 24, 41, 12, 41, 43, 24, 70, 24, 100, 41, 43, 43, 100, 29, 70, 100, 43, 41, 27, 70, 70, 59, 41, 24, 24, 29, 43, 24, 27, 70, 24, 27, 70, 24, 70, 27, 24, 43, 27, 100, 41, 12, 70, 43, 70, 62, 12, 59, 29, 62, 41, 100, 43, 43, 59, 59, 70, 12, 27, 43, 43, 27, 27, 27, 24, 43, 43, 62, 43, 70, 29]))
