def closest_int_same_bit_count(x):
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS-1):
        if (x>>i&1 != x>>(i+1)&1):
            x ^= 1 << i | 1 << (i+1)
            return x

    return ValueError('All bits are 0 or 1')

def closest_int_same_bit_count2(x):
    # solve the same problem in O(1) time and space.
    if x==0:
        return ValueError('All bits are 0')
    elif x==2**64-1:
        return ValueError('All bits are 1')
    




## test
x = 0b1011100
y = 2**64 - 1

print(closest_int_same_bit_count(x))
print(closest_int_same_bit_count(y))