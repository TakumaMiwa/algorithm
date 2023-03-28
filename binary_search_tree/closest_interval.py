from bintrees import RBTree
def closest_interval(arrays):
    min_distance = float('inf')
    iters = RBTree()
    for idx, sorted_array in enumerate(arrays):
        it = iter(sorted_array)
        first_min = next(it, None)
        if first_min is not None:
            ## RBTree.insert(key, value) <==> RBTree[key] = value
            iters.insert((first_min, idx), it)

    while True:
        min_value, min_idx = iters.min_key()
        max_value = iters.max_key()[0]
        min_distance = min(min_distance, max_value-min_value)
        it = iters.pop_min()[1]
        next_min = next(it, None)
        if next_min is None: return min_distance
        iters.insert((next_min, min_idx), it)
    return min_distance

## test
arrays = [
    [5, 10, 15],
    [3, 6, 9, 12, 15],
    [8, 16, 24]
]
print(closest_interval(arrays))

