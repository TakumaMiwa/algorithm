import heapq

def kth_largest_element(l, k):
    ## O(n*logk) solution
    heap = []
    for num in l:
        if len(heap) < k: heapq.heappush(heap, num)
        elif heap[0] < num: heapq.heappushpop(heap, num)

    return heap[0]

import random
def kth_largest_element(l, k):
    if len(l) < k: return -1 
    ## expected O(n) solution
    def partition_around_pivot(left, right, pivot_idx):
        pivot_value = l[pivot_idx]
        new_pivot_idx = left
        l[pivot_idx], l[right] = l[right], l[pivot_idx]
        for i in range(left, right):
            if l[i] > pivot_value:
                l[i], l[new_pivot_idx] = l[new_pivot_idx], l[i]
                new_pivot_idx += 1

        l[right], l[new_pivot_idx] = l[new_pivot_idx], l[right]
        return new_pivot_idx

    left, right = 0, len(l)-1
    while left<=right:
        pivot_idx = random.randint(left, right)
        new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
        if new_pivot_idx==k-1:
            return l[new_pivot_idx]
        elif new_pivot_idx > k-1: right = new_pivot_idx - 1
        else: left = new_pivot_idx + 1

## test
print(kth_largest_element([3, 2, 1, 5, 4], 3))