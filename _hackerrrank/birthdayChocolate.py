def birthdayChocolate(arr, d, m):
    count = 0
    for i in range(len(arr) - m + 1):
        if sum(arr[i: i + m]) == d:
            count += 1
    return count


print(birthdayChocolate([2, 2, 1, 3, 2], 6, 3))
print(birthdayChocolate([1, 2, 1, 3, 2], 3, 2))
