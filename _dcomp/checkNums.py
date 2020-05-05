def checkNums(num1, num2):
    if num2 > num1:
        return "true"
    elif num1 > num2:
        return "false"
    else:
        return "equal"


print(checkNums(5, 8))
print(checkNums(3, 3))
print(checkNums(100, -100))
