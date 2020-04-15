from collections import Counter


def makingAnagrams(a, b):
    dict1 = Counter(a)
    dict2 = Counter(b)
    common = list((dict1 & dict2).elements())
    return len(a) + len(b) - len(common)*2


print(makingAnagrams("geeks", "forgeeks"))
print(makingAnagrams("cde", "def"))
