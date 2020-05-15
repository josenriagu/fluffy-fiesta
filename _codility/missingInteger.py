def missingInteger(A):
    A.sort()
    cur_max = 0
    for el in A:
        if el > 0 and el == cur_max + 1:
            cur_max = el

    return cur_max + 1


print(missingInteger([1, 3, 6, 4, 1, 2]))
print(missingInteger([1, 2, 3]))
print(missingInteger([-1, -3]))
