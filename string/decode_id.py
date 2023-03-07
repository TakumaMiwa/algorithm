import functools
import string
def decode_id(col_id):
    return functools.reduce(lambda num, c: num * 26 + string.ascii_uppercase.index(c)+1, reversed(col_id), 0)

print(decode_id('ZZ'))