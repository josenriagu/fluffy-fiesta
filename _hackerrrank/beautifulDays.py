def beautifulDays(i, j, k):
    count = 0
    for n in range(i, j+1):
        newStr = int(str(n)[::-1])
        if (n - newStr) % k == 0:
            count += 1

    return count

print(beautifulDays(20, 23, 6))
