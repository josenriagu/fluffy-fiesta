def missingNumber(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i] != i:
            return i
        if i == len(arr) - 1:
            return i + 1


print(missingNumber([3, 1, 0]))
print(missingNumber([0]))
