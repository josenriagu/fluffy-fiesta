def maxMin(k, arr):
    # sort array
    arr.sort()
    # current_min = 0
    # while len(arr) >= k:
    #     if current_min == 0:
    #         current_min = max(arr[len(arr)-k:]) - min(arr[len(arr)-k:])
    #     else:
    #         new_minimum = max(arr[len(arr)-k:]) - min(arr[len(arr)-k:])
    #         if current_min > new_minimum:
    #             current_min = new_minimum
    #     arr = arr[: len(arr) - k]
    print(len(arr))
    return max(arr[:len(arr)-k]) - min(arr[:len(arr)-k])


values = []
# read test case file and load arr
with open("maxMinLarge.in") as f:
    values = f.readlines()
    # remove first line
    values = values[2:]
    for index, value in enumerate(values):
        value = value.split("\n")
        values[index] = int(value[0])
    # print(values)

# print(maxMin(2, [1, 2, 1, 2, 1]))
# print(maxMin(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]))
print(maxMin(5000, values))
# print(maxMin(3, [10, 20, 30, 100, 200, 300, 1000]))
