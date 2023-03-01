import random
import math
def my_random(a, b):
    one_count = 0
    bit_num = math.floor(math.log2(b)) + 1
    random_num = float('inf')
    while not a <= random_num <= b:
        random_num = 0
        for _ in range(bit_num):
            random_num <<= 1
            random_num |= random.randint(0, 1)
    return random_num
l = [0] * 10
for _ in range(10000):
    l[my_random(0, 9)] += 1
print(l)