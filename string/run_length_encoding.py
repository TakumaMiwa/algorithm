def encoding(s):
    def supporter(start):
        key = s[start]
        while start < len(s) and s[start]==key: start += 1
        return start
    start = 0
    result = []
    while start < len(s):
        end = supporter(start)
        result.append(s[start])
        result.append(str(end-start))
        start = end
    return ''.join(result)

import functools
def decoding(s):
    ## cannot deal with the case in which num is more than 10.
    # return ''.join(functools.reduce(lambda result, i: result + [s[i]] * int(s[i+1]), range(len(s))[::2], []))
    idx = 0
    result = []
    while idx < len(s):
        count = 0
        key = s[idx]
        idx += 1
        while idx < len(s) and s[idx].isdigit():
            count *= 10
            count += int(s[idx])
            idx += 1
        result += [key] * count
    return ''.join(result)

## test
s = 'aaaaaaaaaabbbccc'
s = encoding(s)
print(s)
s = decoding(s)
print(s)
