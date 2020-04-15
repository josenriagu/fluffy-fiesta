from collections import Counter


def twoStrings(s1, s2):
    s1 = Counter(s1)
    s2 = Counter(s2)
    count = 0
    for el in s2:
        if el in s1:
            count += 1

    return "YES" if count > 0 else "NO"


print(twoStrings("hello", "world"))
print(twoStrings("hi", "world"))
