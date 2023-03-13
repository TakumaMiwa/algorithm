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
arrays = [[3, 5, 7], [0, 6], [0, 6, 8]]
print(merge_array(arrays))
    