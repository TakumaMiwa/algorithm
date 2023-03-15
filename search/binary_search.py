def binary_search(l, key):
    left, right = 0, len(l) - 1
    while left <= right:
        mid = (left - right) // 2 + right
        if l[mid] < key: left = mid + 1
        elif l[mid] == key: return mid
        else: right = mid - 1

    return -1

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(l, 5))