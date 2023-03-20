def nonconstructible_value(l):
    if not l: return 1
    total = 0
    for num in l:
        if total+1 < num: return total + 1
        total += num
    return total + 1

## test
l = [1, 1, 1, 1, 1, 5, 10, 25]
print(nonconstructible_value(l))
