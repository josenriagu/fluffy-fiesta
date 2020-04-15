def isBalanced(s):
    # if length is odd, return NO
    if len(s) % 2 == 1:
        return "NO"
    # initialize different bracket types to be matched
    bracketTypes = "[]{}()"
    # initialize empty list to hold and compare the match values
    checker = []
    # loop through the length of s
    for i in range(len(s)):
        # get the index of the current element
        cur_index = bracketTypes.index(s[i])
        if cur_index == -1:
            # this will ignore other characters because characters
            # not in bracketTypes will return -1 as index
            continue
        # if position is divisible by 2
        if cur_index % 2 == 0:
            # push next expected brace position into array
            checker.append(cur_index + 1)
        # else if checker is empty or last position in the checker is not equal to the cur_index
        elif len(checker) == 0 or checker.pop(len(checker)-1) != cur_index:
            # unbalanced, return NO
            return "NO"
    # if it exits the loop sucessfully, and balanced, return YES
    return "YES"


# print(isBalanced("{[()}"))
# print(isBalanced("{[()]}"))
# print(isBalanced("{[(])}"))
# print(isBalanced("{{[[(())]]}}"))
# print(isBalanced("{(([])[])[]}"))
# print(isBalanced("}][}}(}][))]"))
# print(isBalanced("[()][{}()][](){}([{}(())([[{}]])][])[]([][])(){}{{}{[](){}}}()[]({})[{}{{}([{}][])}]"))
# print(isBalanced("{{}("))
print(isBalanced("{}(((){}){[]{{()()}}()})[]{{()}{(){()(){}}}}{()}({()(()({}{}()((()((([])){[][{()}{}]})))))})"))
