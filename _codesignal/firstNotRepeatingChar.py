from collections import Counter


def firstNotRepeatingCharacter(s):
    dict1 = Counter(s)
    for key in dict1:
        if dict1[key] == 1:
            return key
        # print(key,dict1[key])
    return "_"

# def firstNotRepeatingCharacter(s):
#     for c in s:
#         if s.index(c) == s.rindex(c):
#             return c
#     return '_'

# NB: index() returns index of first occurence, while rindex() returns index of last occurence


print(firstNotRepeatingCharacter("abaccsfsc"))
