def strstr(s, x):
    if x in s:
        found = s.split(x)
        return len(found[0])
    return -1


print(strstr("CodeFightsIsAwesome", "IsA"))
print(strstr("CodeFightsIsAwesome", "Code"))
