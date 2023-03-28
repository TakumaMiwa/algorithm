import math
def subset(array):
    max_key = 2 ** len(array)
    result = []
    for key in range(max_key):
        bit_key = key
        l = []
        while bit_key:
            l.append(array[int(math.log2(bit_key & ~(bit_key - 1)))])
            bit_key &= bit_key - 1
        result.append(l)
    return result

## test
print(subset([0, 1, 5]))
