def jumpingOnClouds(c):
    con_zeros = 0
    path = 0
    for i, el in enumerate(c):
        if el == 0:
            if c[i-1] == 1:
                path += 1
            else:
                con_zeros += 1
        if el == 1:
            path += (con_zeros // 2)
            con_zeros = 1
    path += (con_zeros // 2)
    return path


print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))