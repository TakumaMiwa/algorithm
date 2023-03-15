def square_root(n):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if mid**2==n: return mid
        elif mid**2<n: left = mid
        else: right = mid - 1
    return left

## test
print(square_root(300))