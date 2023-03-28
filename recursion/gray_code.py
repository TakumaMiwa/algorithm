def gray_code(n):
    if n == 0:
        return [0]
    
    gray_code_minus = gray_code(n-1)
    leading_bit = 1 << (n - 1)
    return gray_code_minus + [leading_bit | i for i in reversed(gray_code_minus)]

## test
print(gray_code(3))
