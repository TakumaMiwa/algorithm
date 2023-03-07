import string
import functools
def search_string(s, t):
    if len(s)  < len(t): return -1

    base = 26
    s_hash = functools.reduce(lambda hash, c: hash * base + string.ascii_uppercase.index(c), s[:len(t)], 0)
    t_hash = functools.reduce(lambda hash, c: hash * base + string.ascii_uppercase.index(c), t, 0)
    print(t_hash)
    if s_hash==t_hash: return 0
    power = max(len(t)-1, 0) ** base

    for i in range(len(t), len(s)):
        print(s[i-len(t)])
        s_hash = (s_hash - string.ascii_uppercase.index(s[i-len(t)])*power)*base + string.ascii_uppercase.index(s[i])
        print(s_hash)
        if s_hash==t_hash: return i - len(t) + 1

    return -1


## test
# print(search_string("AAAAA", "AA"))
print(search_string("AAABB", "BB"))
# print(search_string("AAAAA", "BB"))