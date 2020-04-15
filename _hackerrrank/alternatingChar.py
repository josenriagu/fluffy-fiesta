def alternatingChar(s):
    letter_a = False
    letter_b = False
    count = 0

    for el in s:
        if el == "A":
            letter_b = False
            if letter_a == True:
                count += 1
            letter_a = True

        if el == "B":
            letter_a = False
            if letter_b == True:
                count += 1
            letter_b = True
    return count


print(alternatingChar("ABABABAB"))
