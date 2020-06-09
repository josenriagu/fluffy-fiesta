def dayOfTheProgrammer(year):
    # initialize variables to hold number of days elapsed till August 31
    leap = 244
    normal = 243

    # check for julian
    if year < 1918:
        if year % 4 == 0:
            print(f'{256 - leap}.09.{year}')
            return
        else:
            print(f'{256 - normal}.09.{year}')
            return

    # transition from julian to gregorian in 1918 (not leap) made february 14, the 32nd day, hence 13 days less
    if year == 1918:
        print(f'{256 - (normal -13)}.09.{year}')
        return

    isleap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if isleap:
        print(f'{256 - leap}.09.{year}')
        return
    else:
        print(f'{256 - normal}.09.{year}')
        return


dayOfTheProgrammer(1984)
# dayOfTheProgrammer(1600)
dayOfTheProgrammer(2017)
dayOfTheProgrammer(2016)
# dayOfTheProgrammer(2400)
# dayOfTheProgrammer(1700)
dayOfTheProgrammer(1800)
# dayOfTheProgrammer(1900)
# dayOfTheProgrammer(2100)
# dayOfTheProgrammer(2200)
dayOfTheProgrammer(1918)
