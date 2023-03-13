import heapq
def k_largest_element(l, k):
    if len(l) < k: -1
    nodes = [0]
    result = []
    while True:
        next_level = []
        while nodes:
            idx = nodes.pop()
            if idx < len(l):
                heapq.heappush(result, -l[idx])
                next_level += [2*idx+1, 2*idx+2]
        if k <= len(result): break
        nodes = next_level
    return [-heapq.heappop(result) for _ in range(k)]
## test
l = [561, 314, 401, 28, 156, 359, 271, 11, 3]
print(k_largest_element(l, 4))