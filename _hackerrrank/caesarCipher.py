def caesarCipher(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotated = alphabet[k%26:] + alphabet[:k%26]
    encrypted = ""
    for el in s:
        if not el.isalpha():
            encrypted += el
            continue
        if not el.islower():
            original_index = alphabet.index(el.lower())
            encrypted += rotated[original_index].upper()
            continue
        original_index = alphabet.index(el)
        encrypted += rotated[original_index]
    return encrypted


print(caesarCipher("middle-Outz", 2))
