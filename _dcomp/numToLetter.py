def numToLetter(arr):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    letters = [alpha[i-1] for i in arr]
    return "".join(letters)


print(numToLetter([1, 4, 3]))
