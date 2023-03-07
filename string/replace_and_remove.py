def replace_and_remove(size, l):
    new_size = size
    for i in range(size):
        if l[i] == 'a': new_size += 1
        elif l[i] == 'b': new_size -= 1

    idx = new_size - 1
    for i in reversed(range(size)):
        if l[i] == 'a':
            l[idx-1:idx+1] = ['d', 'd']
            idx -= 2
        elif l[i] != 'b':
            l[idx] = l[i]
            idx -= 1

    return l

## test
print(replace_and_remove(4, ['a', 'b', 'a', 'c', None]))