def firstDuplicate(a):
    holder = {}
    count = 0
    current_min = ()
    for i, el in enumerate(a):
        if el in holder:
            holder[el].append(i)
            if len(holder[el]) > 1:
                if len(current_min) == 0:
                    current_min = (el, holder[el])
                elif holder[el][1] < current_min[1][1]:
                    current_min = (el, holder[el])
        else:
            holder[el] = [i]
        count += 1

    if len(current_min) > 0:
        return current_min[0]
    else:
        return -1

# neater solution
# def firstDuplicate(a):
    # mySet = set()
    # for el in a:
    #     if el in mySet:
    #         return el
    #     mySet.add(el)
    # return -1


print(firstDuplicate([1, 3, 5, 2]))
