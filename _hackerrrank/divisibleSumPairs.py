def divisibleSumPairs(arr, k):
    count = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if i < j and (arr[i]+arr[j]) % k == 0:
                count += 1
    return count


print(divisibleSumPairs([1, 2, 3, 4, 5, 6], 5))
print(divisibleSumPairs([1, 3, 2, 6, 1, 2], 3))
