# Complete the 'threeNumberSum' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER target
#


def threeNumberSum(arr, target):
    # Write your code here
    triplets = []
    for i in range(len(arr)):
        x = arr[i]
        rem = arr[i + 1:]
        for j in range(len(rem)):
            y = rem[j]
            z = target - (x + y)
            if z in arr:
                if (z == x or z == y) and arr.count(z) < 2:
                    continue
                else:
                    triplet = sorted([x, y, z])
                    if triplet not in triplets:
                        triplets.append(triplet)
    return sorted(triplets)

# optimized using set
def _threeNumberSum(arr, target):
    size = len(arr)
    output = []
    for i in range(size - 1):
        diff = set()
        x = arr[i]
        y_z = target - x
        for j in range(i+1, size):
            y = arr[j]
            z = y_z - y
            if z in diff:
                matched_pair = sorted([x, y, z])
                output.append(matched_pair)
            else:
                diff.add(y)
    return sorted(output)


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
print(_threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 30))

# large input
values = []
with open("maxMinLarge.in") as f:
    line = f.readlines()
    for i in range(1000):
        line[i] = int(line[i].rstrip())
        values.append(line[i])

print(_threeNumberSum(values, 161631314))
