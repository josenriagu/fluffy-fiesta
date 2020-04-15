from collections import Counter


def checkMagazine(magazine, note):
    # form counter dictionaries of both lists
    dict_magazine = Counter(magazine)
    dict_note = Counter(note)
    # loop
    for word in dict_note:
        # if word exists in magazine and frequency is greater or equal that of note
        if word in dict_magazine and dict_magazine[word] >= dict_note[word]:
            # continue
            continue
        # otherwise, word does not exist
        else:
            print("No")
            return
    # if it loops successfully, means all words were found
    print("Yes")
    return


print(checkMagazine(["ive", "got", "a", "lovely", "bunch",
                     "of", "coconuts"], ["ive", "got", "some", "coconuts"]))
print(checkMagazine(["give", "me", "one", "grand",
                     "today", "night"], ["give", "one", "grand", "today"]))
