from collections import Counter
import functools
import operator


def sherlockValid(s):
    # edge case: s has only one character
    if len(s) == 1:
        return "YES"
    # form a count dictionary of letter occurences
    dict1 = Counter(s)
    # get a list of all occurences for each letter
    values = list(dict1.values())
    # pick the minimum occurence
    minimum = min(values)

    # ----replacing this loop with generator on line 19----
    # for i, el in enumerate(values):
    #     remove minimum from each el
    #     values[i] = el - minimum

    zeros = [el - minimum for el in values]

    # reduce the values array using functools and operator module methods
    outcome = functools.reduce(operator.add, zeros)
    print(outcome, zeros)
    if zeros.count(0) == 1 and outcome % (len(zeros) - 1) == 0:
        return "YES"
    elif outcome <= 1 and zeros.count(0) > 1:
        return "YES"
    else:
        return "NO"


print(sherlockValid("aabbc"))
print(sherlockValid("abcdefghhgfedecba"))
print(sherlockValid("ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"))
