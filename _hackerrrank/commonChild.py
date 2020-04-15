from collections import Counter

def commonChild(s1, s2):
    dict1 = Counter(s1)
    dict2 = Counter(s2)
    return len(list((dict1 & dict2).elements()))

print(commonChild("OUDFRMYMAW", "AWHYFCCMQX"))