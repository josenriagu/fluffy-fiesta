def fraudulentActivityNotif(expenditure, d):
    notifs = 0
    if len(expenditure) <= d:
        return 0
    checker = expenditure[:d]
    # helper function to check median

    def getMedian(arr):
        median = 0
        if len(checker) % 2 == 0:
            median = (checker[len(checker)//2] +
                      checker[((len(checker)//2) - 1)]) / 2
        else:
            median = checker[len(checker)//2]
        return median
    for el in expenditure[d:]:
        median = getMedian(checker)
        if el >= 2 * median:
            notifs += 1
        checker.pop(0)
        checker.append(el)

    return notifs


print(fraudulentActivityNotif([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
# print(fraudulentActivityNotif([1, 2, 3, 4, 4], 4))

# passing solution - study more

def activityNotifications(expenditure, d):
    notif = 0
    max_num = max(expenditure)
    c = [0] * (max_num + 1)
    for el in expenditure[: d]:
        c[el] += 1

    def median():
        # returns twice the median
        s = 0
        for x in range(max_num + 1):
            s += c[x]
            if 2*s >= d:
                break
        if d % 2 == 1 or 2*s > d:
            return 2*x
        return x + next(y for y in range(x+1, max_num + 1) if c[y])

    for i in range(d, len(expenditure)):
        if expenditure[i] >= median():
            notif += 1
        c[expenditure[i-d]] -= 1
        c[expenditure[i]] += 1

    return notif
