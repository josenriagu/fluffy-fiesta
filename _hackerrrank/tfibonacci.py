def fibonacci(n):
    fib_arr = []  # O(1)
    for i in range(n):  # O(n) * O(1)
        if i < 2:
            fib_arr.append(i)  # O(1)
        else:
            fib_arr.append(fib_arr[i-1] + fib_arr[i-2])  # 2 * O(1)
    return fib_arr  # O(1)


'''
O(1) + O(n) * O(1) + O(1) + O(2) + O(1)
O(n) + O(5)
O(n)
'''
print(fibonacci(4))


# 6/6 test cases
