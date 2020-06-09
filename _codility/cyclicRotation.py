def cyclicRotation(A, K):
    if len(A) == 0:
        return A
    while K > 0:
        last = A.pop(len(A) - 1)
        A.insert(0,last)
        K -= 1
    return A


print(cyclicRotation([3, 8, 9, 7, 6], 3))
