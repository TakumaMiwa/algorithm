import string
def convert_base(num_str, b1, b2):
    num = 0
    base = 1
    for c in reversed(num_str):
        num += string.hexdigits.index(c) * base
        base *= b1

    result = []
    while num:
        result.append(string.hexdigits[num%b2])
        num //= b2

    return ''.join(reversed(result)).upper()

## test
print(convert_base("615", 7, 13))