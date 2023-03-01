def power(x, y):
    if y<0:
        y, x = -y, 1.0 / x
    result = 1
    while y:
        result = x*result if y&1 else result
        y >>= 1
        x = x*x
        
    return result

import random
import sys
## test 
for _ in range(100):
    x, y = random.randint(1, 100), random.randint(1, 100)
    if x**y != power(x,y):
        print("false.")
        print(x, y, power(x, y))
        sys.exit()
print("success")
