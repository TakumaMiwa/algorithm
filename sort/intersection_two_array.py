def intersection_two_array(l1, l2):
    p1 = p2 = 0
    result = set()
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] < l2[p2]: p1 += 1
        elif l1[p1]==l2[p2]:
            result.add(l1[p1])
            p1 += 1
            p2 += 1
        else:
            p2 += 1
    return result

## test
l1 = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
l2 = [5, 5, 6, 8, 8, 9, 10, 10]
print(intersection_two_array(l1, l2))