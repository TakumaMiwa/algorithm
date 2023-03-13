import heapq
def compute_median(l):
    min_heap, max_heap = [], []

    for x in l:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))

        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        print(0.5 * (min_heap[0]-max_heap[0]) if len(max_heap)==len(min_heap) else min_heap[0])

## test
l = [1, 0, 3, 5, 2, 0, 1]
compute_median(l)