import string
import functools
def string_to_int(s):
    if s[0]=='-':
        s, sign = s[1:], -1
    else:
        sign = 1

    result = 0
    for digit in s:
        result *= 10
        result += string.digits.index(digit)
    return sign * result

def string_to_int2(s):
    if s[0]=='-':
        s, sign = s[1:], -1
    else:
        sign = 1

    return sign * functools.reduce(lambda result, digit: result * 10 + string.digits.index(digit), s, 0)


s = '-123'
print(string_to_int2('-123'))

    