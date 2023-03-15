import math
def square_root(r):
    left, right = (1, r) if 1 <= r else (r, 1)
    while not math.isclose(left, right,):
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        if mid_squared > r:
            right = mid
        else:
            left = mid
    return left

print(square_root(0.25))
