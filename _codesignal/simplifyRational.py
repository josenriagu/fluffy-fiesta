def simplifyRational(numerator, denominator):
    arr = [7, 5, 3, 2, 1]
    final = False
    # edge case: numerator is zero
    if numerator == 0:
        return [0, 1]
    # edge case: numerator and denominator are equal, consider signs
    if abs(numerator) == abs(denominator):
        return [numerator//denominator, denominator//denominator]
    # edge case: denominator is negative, flip the signs
    if denominator < 0:
        numerator *= -1
        denominator *= -1
    # edge case: their diff is a common factor
    diff = abs(abs(numerator) - abs(denominator))
    if numerator % diff == 0 and denominator % diff == 0:
        return [numerator//diff, denominator//diff]

    while not final:
        for el in arr:
            if numerator % el == 0 and denominator % el == 0:
                numerator = numerator//el
                denominator = denominator//el
                if el == 1:
                    final = True
                break

    return [numerator, denominator]


print(simplifyRational(3, 6))
print(simplifyRational(8, 5))
print(simplifyRational(8, -5))
print(simplifyRational(-18, -24))
print(simplifyRational(-18, 24))
print(simplifyRational(5495, -9135))
print(simplifyRational(478, -239))
print(simplifyRational(-10000, 10000))
print(simplifyRational(-23944, 43408))
