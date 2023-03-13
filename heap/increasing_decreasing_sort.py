def increasing_decreasing_sort(l):
    sorted_subarrays = []
    INCREASING, DECREASING = range(2)
    subarray_type = INCREASING
    start_idx = 0

    for i in range(1, len(l)+1):
        if (i==len(l) or (l[i-1] < l[i] and subarray_type==DECREASING) or (l[i-1]>=l[i] and subarray_type==INCREASING)):
            sorted_subarrays.append(l[start_idx:i] if subarray_type==INCREASING else list(reversed(l[start_idx:i]))) ## only reversed() doesn't work
            start_idx = i
            subarray_type ^= 1
    return merge_array(sorted_subarrays)

import heapq
def merge_array(arrays):
    l = [(array[0], i) if array else None for i, array in enumerate(arrays)]
    heapq.heapify(l)
    idx_list = [1] * len(arrays)
    result = []
    while l:
        min_num, min_array_idx = heapq.heappop(l)
        result.append(min_num)
        if idx_list[min_array_idx] < len(arrays[min_array_idx]):
            heapq.heappush(l, (arrays[min_array_idx][idx_list[min_array_idx]], min_array_idx))
            idx_list[min_array_idx] += 1

    return result

## test
l = [97, 131, 493, 294, 221, 339, 418, 452, 442, 190]
print(increasing_decreasing_sort(l))