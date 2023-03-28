def palindromic_decomposition(s):
    s = list(s)
    def supporter(idx, l):
        print(idx)
        if idx==len(s):
            result.append(l.copy())
            return
        for i in range(idx, len(s)):
            prefix = s[idx:i+1]
            if prefix==prefix[::-1]:
                supporter(i+1, l+[''.join(s[idx:i+1])])
    result = []
    supporter(0, [])
    return result

## test
print(palindromic_decomposition('02044'))


