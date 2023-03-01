def swap_bits(x, i, j):
    if (x>>i)&1 != (x>>j)&1:
        bit_mask = 1<<i | 1<<j
        x ^= bit_mask

    return x

## test
x = 0b11001001
i, j = 1, 6
print(bin(x))
print(bin(swap_bits(x, i, j)))