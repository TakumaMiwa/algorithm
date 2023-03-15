from collections import namedtuple
import functools
def duplicate_missing(l):
    DuplicateAndMissing = namedtuple('DuplicateAndMissing', ('duplicate', 'missing'))
    
    miss_xor_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(l), 0)
    differ_bit, miss_or_dup = miss_xor_dup & (~(miss_xor_dup - 1)), 0
    for i, num in enumerate(l):
        if i&differ_bit: miss_or_dup ^= i
        if num&differ_bit: miss_or_dup ^= num

    if any(num==miss_or_dup for num in l): return DuplicateAndMissing(miss_or_dup, miss_xor_dup^miss_or_dup)
    else: return DuplicateAndMissing(miss_xor_dup^miss_or_dup, miss_or_dup)