def countEvenOddStrings(arr):
    odd = 0
    for el in arr:
        if len(el) % 2 != 0:
            odd += 1
    return [odd, len(arr) - odd]


print(countEvenOddStrings(["one", "two", "three"]))
print(countEvenOddStrings(["next", "first"]))
