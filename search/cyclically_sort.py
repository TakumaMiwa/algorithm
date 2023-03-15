def cyclically_sort(l):

    left, right = 0, len(l)-1
    while left < right:
        mid = (left + right) // 2
        if l[mid] > l[right]:
            left = mid + 1
        else:
            right = mid
    return left

## 
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(cyclically_sort(l))