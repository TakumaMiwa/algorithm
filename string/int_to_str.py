import string
def int_to_str(num):
    if not num: return 0
    if num < 0:
        isNegative = True
        num = -num
    else: isNegative = False
    result = []
    while num:
        ## adding a digit to the beginning of the list is expensive
        # result = [string.digits[num%10]] + result

        result.append(string.digits[num%10])
        num //= 10

    return ''.join(reversed(result+['-'])) if isNegative else ''.join(reversed(result))

## test
print(int_to_str(-123))