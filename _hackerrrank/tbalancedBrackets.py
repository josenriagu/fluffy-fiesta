#
# Complete the 'balancedBrackets' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING string as parameter.
#


def balancedBrackets(s):
    # Write your code here

    # initialize variables
    bracketTypes = "[]{}()||"  # bracket types including "|"
    checker = []  # array to hold next matching pair in order
    just_braces = ""  # to filter items in bracketTypes

    # loop through s
    for el in s:
        # if el in bracketTypes, concatenate to just_braces
        if el in bracketTypes:
            just_braces += el

    # loop through just_braces
    for el in just_braces:
        # find the element index in bracketTypes
        cur_index = bracketTypes.index(el)
        # edge case: condition to trap matching "|", remove it from checker list and continue
        if cur_index == 6 and len(checker) != 0 and checker[len(checker) - 1] == 7:
            checker.pop(len(checker)-1)
            continue
        # if cur_index is even, the matching pair is one index ahead (odd)
        if cur_index % 2 == 0:
            # append to checker
            checker.append(cur_index + 1)
        # otherwise, if checker is not empty and the last element is not same as cur_index
        elif len(checker) == 0 or checker.pop(len(checker)-1) != cur_index:
            # unbalanced, return False
            return False

    # if it exits loop and checker is empty, means matching was completed
    if len(checker) == 0:
        # balanced, return True
        return True
    # otherwise
    else:
        # unbalanced, return False
        return False


print(balancedBrackets("[(])"))
print(balancedBrackets("foo(bar)baz"))
print(balancedBrackets("{{||[]||}}"))
print(balancedBrackets(
    "I am happy to take your donation; any amount will be greatly appreciated."))
print(balancedBrackets(
    "This is t(he la[st random sentence I will be writing |and| I am going to stop mid-sent]"))
print(balancedBrackets(
    "He ran| |out of money, so he {| had} to stop playing | poker."))

# 8/8 test cases
