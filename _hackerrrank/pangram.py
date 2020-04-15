def pangrams(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    found = ""
    for el in alphabet:
        if (el.lower() in s or el.upper() in s) and el.lower() not in found:
            found += el
            if len(found) == len(alphabet):
                return "pangram"
    return "not pangram"


print(pangrams("We promptly judged antique ivory buckles for the next prize"))
