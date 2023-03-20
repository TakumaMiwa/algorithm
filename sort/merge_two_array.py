def merge_array(l1, l2):
    p1, p2 = 0, len(l2)-1
    while l1[p1+1] is not None: p1 += 1

    p3 = p1 + p2 + 1
    while 0 <= p3 and 0 <= p1 and 0 <= p2:
        if l1[p1] < l2[p2]:
            l1[p3] = l2[p2]
            p2 -= 1
        else:
            l1[p3] = l1[p1]
            p1 -= 1
        p3 -= 1
    if p1 < 0: l1[:p2] = l2[:p2]
    return l1

## test

l1 = [5, 13, 17] + [None] * 5
l2 = [3, 7, 11, 19]
print(merge_array(l1, l2))