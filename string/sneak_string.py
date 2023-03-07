def sneak_string(s):
    if not s: return []
    l1, l2, l3 = [], [s[0]], []
    idx = 1
    while idx < len(s):
        l1.append(s[idx])
        if idx + 1 < len(s): l2.append(s[idx+1])
        if idx + 2 < len(s): l3.append(s[idx+2])
        if idx + 3 < len(s): l2.append(s[idx+3])
        idx += 4
    return l1 + l2 + l3

## test
print(sneak_string("Hello World!"))