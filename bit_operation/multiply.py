def multiply(x, y):
    def add(x, y):
        s, c = 0, 0
        k, result = 1, 0
        temp_x, temp_y = x, y
        while temp_x or temp_y or c:
            s = x&k ^ y&k ^ c
            c =(((x&k) & (y&k)) | ((x&k) & c) | (c & (y&k))) << 1
            result |= s
            k <<= 1
            temp_x, temp_y = temp_x>>1, temp_y>>1

        return result
    result = 0
    while y:
        if y&1:
            result = add(result, x)
        x <<= 1
        y >>= 1
    return result
import random
import sys
## test
for _ in range(100):
    x, y = random.randint(0, 100), random.randint(0, 100)
    if x*y != multiply(x,y):
        print("false.")
        print(x, y, multiply(x, y))
        sys.exit()
print("success")
    
        

