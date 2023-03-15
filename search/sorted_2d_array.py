import bisect
def sorted_2d_array(l, key):
    row, col = 0, len(l[0]) - 1

    while row < len(l) and col >= 0:
        if l[row][col] == key: return True
        elif l[row][col] < key: row += 1
        else: col -= 1
    return False

## test
l = [
    [-1, 2, 4, 4, 6],
    [1, 5, 5, 8, 13],
    [2, 5, 7, 11, 13],
    [3, 5, 7, 46, 49],
    [4, 7, 9, 47, 50]
]

print(sorted_2d_array(l, 7))
print(sorted_2d_array(l, -4))