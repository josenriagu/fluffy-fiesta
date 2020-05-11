def removeEvens(words):
    odd = []
    for el in words.split(" "):
        if len(el) % 2 != 0:
            odd.append(el)
    return " ".join(odd)


print(removeEvens("hi Joe how is it going"))
print(removeEvens("hi there John Smith"))
