def arithmetic(num1, num2):
    quot = num1//num2

    # helper function to help with arithmetic
    def helper(num, operator):
        strEq = str(num)
        if len(strEq) == 1:
            strEq = "0" + strEq
        if operator == "mul":
            return int(strEq[0]) * int(strEq[1])
        elif operator == "add":
            return int(strEq[0]) + int(strEq[1])
        elif operator == "sub":
            return int(strEq[0]) - int(strEq[1])

    prod = helper(quot, "mul")
    add = helper(prod, "add")
    diff = helper(add, "sub")

    return [quot, prod, add, diff]


print(arithmetic(36, 3))
print(arithmetic(185, 5))
print(arithmetic(267, 3))
print(arithmetic(174, 2))
