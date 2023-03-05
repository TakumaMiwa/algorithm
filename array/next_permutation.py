def next_permutation(l):
    for i in range(len(l)-2, -1, -1):
        if l[i] < l[i+1]: break

    if not i and l[i] >= l[i+1]: return []

    for k in range(len(l)-1, i, -1):
        if l[i] < l[k]:
            l[i], l[k] = l[k], l[i]
            break
    l[i+1:] = reversed(l[i+1:])

    return l

## test
print(next_permutation([1, 2, 3]))
print(next_permutation([3, 2, 1]))