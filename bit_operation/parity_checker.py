def parity_checker(x):
    NUM_UNSIGNED_BITS = 64

    while 1 < NUM_UNSIGNED_BITS:
        NUM_UNSIGNED_BITS //= 2
        x ^= x >> NUM_UNSIGNED_BITS

    return x&0b1

## test
import random

for _ in range(100):
    x1 = x2 = random.randint(0, 10000000000000)
    parity = 0
    while x1:
        parity ^= x1&0b1
        x1 >>= 1
    if parity==parity_checker(x2):
        print("CORRECT!")
    else:
        print("INCORRECT...")
        print("prity: ", parity)
        break
