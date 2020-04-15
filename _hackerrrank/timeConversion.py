import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # Write your code here.
    # Slice parts of the time
    ap = s[len(s)-2:len(s)]
    hour = s[ : 2]
    minute = s[3 : 5]
    secs = s[6 : 8]
    if ap == "PM" and hour != "12":
        return("{}:{}:{}".format(int(hour)+12, minute, secs))
    elif ap == "AM" and hour == "12":
        return("00:{}:{}".format(minute, secs))
    else:
        return("{}:{}:{}".format(hour, minute, secs))


print(timeConversion("11:05:45PM"))