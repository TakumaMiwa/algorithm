def reverse(x):
    result = 0
    x = x if x >= 0 else -x
    while x:
        result *= 10
        result += x%10
        x //= 10
    return -result if x < 0 else result

## test
print(reverse(123))