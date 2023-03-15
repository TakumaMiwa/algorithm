def entry_equal_idx(l):
    left, right = 0, len(l)-1
    while left<=right:
        mid = (left + right) // 2
        diff = l[mid] - mid
        if diff==0: return mid
        elif diff < 0: left = mid + 1
        else: right = mid - 1
    return -1

## test
l = [-2, 0, 2, 3, 6, 7, 9]
print(entry_equal_idx(l))