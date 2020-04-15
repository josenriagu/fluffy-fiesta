def marsExploration(s):
    original = "SOS"*(len(s)//3)
    altered = 0
    for i, el in enumerate(s):
        if el != original[i]:
            altered += 1
    return altered

print(marsExploration("SOSSPSSQSSOR"))