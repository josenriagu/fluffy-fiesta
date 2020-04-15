def minimumBribes(q):
    swaps = 0
    individual_swap = 0
    for i, el in enumerate(q):
        if i == len(q) - 1 and ((i + 1) - el > 2):
            swaps += 1
            continue
        if el == i + 1 or el < i + 1:
            continue
        individual_swap = el - (i + 1)
        swaps += individual_swap
        if individual_swap > 2:
            print("Too chaotic")
            return
    print(swaps)


# minimumBribes([1, 2, 3, 4, 5])
# minimumBribes([2, 1, 3, 4, 5])
# minimumBribes([2, 1, 5, 3, 4])
# minimumBribes([2, 5, 1, 3, 4])
minimumBribes([5, 1, 2, 3, 7, 8, 6, 4])
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
minimumBribes([1, 2, 5, 3, 4, 7, 8, 6])
