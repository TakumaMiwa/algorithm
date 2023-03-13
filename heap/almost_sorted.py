import heapq
def sort_almost_sorted(l, k):
    if len(l) <= k: return list(sorted(l))
    heap = l[:k]
    heapq.heapify(heap)
    idx = 0
    while heap:
        if idx+k < len(l):
            heapq.heappush(heap, l[idx+k])
        l[idx] = heapq.heappop(heap)
        idx += 1

    return l

## test
l = [3, -1, 2, 6, 4, 5, 8]
print(sort_almost_sorted(l, 2))