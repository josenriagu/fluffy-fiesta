if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_el = max(arr)
    arr.sort()
    arr = list(reversed(arr))
    for i in range(len(arr)):
        if arr[i] < max_el:
            print(arr[i])
            break
