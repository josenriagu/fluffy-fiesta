import re


def amendTheSentence(s):
    intro = ""
    for i in range(len(s)):
        if i == 0 and s[i].isupper():
            break
        if s[i].isupper():
            intro = s[:i] + " "
            break
    words = re.findall('[A-Z][^A-Z]*', s)
    return intro + " ".join(words).lower()

# one liner using regex


def _amendTheSentence(s):
    return " ".join(re.findall(r'[A-Za-z][^A-Z]*', s)).lower()


print(amendTheSentence("apCodesignalIsAwesome"))
