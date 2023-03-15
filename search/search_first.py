import bisect
def search_first(l, k):
    left, right, result = 0, len(l)-1, -1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] < k: left = mid + 1
        elif l[mid] == k:
            result = mid
            right = mid - 1 ## Nothing to the right of mid can be solution
        else:
            right = mid - 1
    return result

## test
l = [1, 1, 1, 1, 1, 1, 1]
print(search_first(l, 1))