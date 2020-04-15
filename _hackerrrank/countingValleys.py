def countingValleys(n, s):
    [mountain, valley, sea, up, down] = [0, 0, 0, False, False]
    for el in s:
        if el == 'U':
            if (up == False and sea >= 0) or (up == False and sea == 0):
                up = True
                down = False
                mountain += 1
            sea += 1
        elif el == 'D':
            if (down == False and sea <= 0) or (down == True and sea == 0):
                down = True
                up = False
                valley += 1 
            sea -= 1
    return valley

print(countingValleys(10, 'DUDDDUUDUU'))