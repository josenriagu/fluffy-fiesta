def sudoku2(grid):
    holder = {}
    for arr in grid:
        for i, el in enumerate(arr):
            if el == ".":
                continue
            if el in holder:
                if i in holder[el]:
                    return False
                holder[el].add(i)
            else:
                holder[el] = set()
                holder[el].add(i)

    return True


grid = [["7", ".", ".", ".", "4", ".", ".", ".", "."],
        [".", ".", ".", "8", "6", "5", ".", ".", "."],
        [".", "1", ".", "2", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "9", ".", ".", "."],
        [".", ".", ".", ".", "5", ".", "5", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]]

print(sudoku2(grid))
