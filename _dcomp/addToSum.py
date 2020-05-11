def addToSum(arr, target):
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in arr:
            return [i, arr.index(complement)]


print(addToSum([32, 68, 93, 2, 3, 56], 71))
