def convertToTime(seconds):
    hr = seconds // 3600
    rem = seconds % 3600
    mins = rem // 60
    sec = rem % 60

    return f"{hr} : {mins} : {sec}"


print(convertToTime(10001))
print(convertToTime(14225))
