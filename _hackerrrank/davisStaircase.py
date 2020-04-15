def stepPerms(n):
    seed = {
        1: 1,
        2: 2,
        3: 4
    }
    for i in range(1, n+1):
        if i in seed:
            continue
        else:
            seed[i] = seed[i-1] + seed[i-2] + seed[i-3]
    return seed[n]


print(stepPerms(7))

# 1 = 1
# 2 = 2
# 3 = 4
# 4 = 7
# 5 = 13
# 6 = 24
# 7 = 44

# for n = 4

# 1 1 1 1
# 1 1 2
# 1 2 1
# 1 3
# 2 1 1
# 2 2
# 3 1
