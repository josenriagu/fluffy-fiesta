def leastFrequentNumber(arr):
    values = set()
    least = (0, 0)
    for i in range(len(arr)):
        freq = arr.count(arr[i])
        if i == 0:
            least = (arr[i], freq)
        elif arr[i] not in values and freq < least[1]:
            least = (arr[i], freq)
        values.add(arr[i])
    return least[0]


print(leastFrequentNumber([3, 4, 8, 3, 4, 8, 9]))
print(leastFrequentNumber([100, -1, 0, 5, 100, -1, 5]))
