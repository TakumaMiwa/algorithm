def reverse_bits(x):
    result = 0
    while x:
        result <<= 1
        result |= x&1
        x >>= 1
    return result

## test
x = 0b11001001
print(bin(x))
print(bin(reverse_bits(x)))
