def rotateImage90Anti(a):
    # Consider all squares one by one
    for x in range(0, int(len(a) / 2)):

        # Consider elements in group
        # of 4 in current square
        for y in range(x, len(a)-x-1):

            # store current cell in temp variable
            temp = a[x][y]

            # move values from right to top
            a[x][y] = a[y][len(a)-1-x]

            # move values from bottom to right
            a[y][len(a)-1-x] = a[len(a)-1-x][len(a)-1-y]

            # move values from left to bottom
            a[len(a)-1-x][len(a)-1-y] = a[len(a)-1-y][x]

            # assign temp to left
            a[len(a)-1-y][x] = temp
    return a


def rotateImage90(a):
    n = len(a[0])
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = a[i][j]
            a[i][j] = a[n - 1 - j][i]
            a[n - 1 - j][i] = a[n - 1 - i][n - 1 - j]
            a[n - 1 - i][n - 1 - j] = a[j][n - 1 - i]
            a[j][n - 1 - i] = temp
    return a


# neater solution
# def rotateImage(a):
#     a.reverse()
#     for i in range(len(a)):
#         for j in range(i):
#             a[i][j], a[j][i] = a[j][i], a[i][j]
#     return a

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(rotateImage90(a))
