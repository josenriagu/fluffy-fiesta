def binaryGap(N):
    binary = str(bin(N)).split("b")[1]
    longest = 0
    count = 0
    for i in range(len(binary)):
        if binary[i] == "1":
            continue
        elif binary[i] == "0":
            count += 1
            if i + 1 < len(binary) and binary[i + 1] == "1":
                if count > longest:
                    longest = count
                count = 0
    return longest if longest > count else count

print(binaryGap(32))
print(binaryGap(529))
print(binaryGap(1041))
print(binaryGap(5172))
print(binaryGap(6291457))
print(binaryGap(1610612737))
