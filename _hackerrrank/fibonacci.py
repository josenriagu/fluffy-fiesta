def fibonacci(n):
    fib_arr = []
    for i in range(n + 1):
        if i < 2:
            fib_arr.append(i)
        else:
            fib_arr.append(fib_arr[i-1] + fib_arr[i-2])
    return fib_arr[n]

# recursively...


def fibonacciRec(n):
    if n > 1:
        return fibonacciRec(n - 1) + fibonacciRec(n - 2)
    else:
        return n


print(fibonacci(10))
print(fibonacciRec(10))
