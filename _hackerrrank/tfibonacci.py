def fibonacci(n):
    fib_arr = []
    for i in range(n):
        if i < 2:
            fib_arr.append(i)
        else:
            fib_arr.append(fib_arr[i-1] + fib_arr[i-2])
    return fib_arr


print(fibonacci(4))

# 6/6 test cases
