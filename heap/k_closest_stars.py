import heapq
import math
def k_closest_stars(stars, k):
    def calculate_dist(star):
        return math.sqrt(sum([x*x for x in star]))
    heap = []
    for star in stars:
        if len(heap) < k: heapq.heappush(heap, (-calculate_dist(star), star))
        else:
            dist = -calculate_dist(star)
            if heap[0][0] < dist:
                heapq.heappushpop(heap, (dist, star))
    return [heapq.heappop(heap)[1] for _ in range(k)]

## test
stars = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [1, 1, 1]]
print(k_closest_stars(stars, 2))