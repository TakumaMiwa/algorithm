def divide(x, y):
    k = 63
    quotient = 0
    while y <= x:
        quotient <<= 1
        if (y<<k) <= x:
            x -= y<<k
            quotient |= 1
        k -= 1
    return quotient<<(k+1), x

import random
import sys
## test 
for _ in range(100):
    x, y = random.randint(0, 100), random.randint(1, 100)
    if (x//y, x%y) != divide(x,y):
        print("false.")
        print(x, y, divide(x, y))
        sys.exit()
print("success")

            