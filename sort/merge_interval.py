def merge_interval(intervals, new_interval):
    p = 0
    while p < len(intervals) and intervals[p][1] < new_interval[0]: p += 1
    if p==len(intervals): return intervals + [new_interval]
    start = min(intervals[p][0], new_interval[0])
    start_idx = p
    while p < len(intervals) and intervals[p][0] < new_interval[1]: p += 1
    end = max(intervals[p-1][1], new_interval[1])
    return intervals[:start_idx] + [(start, end)] + intervals[p:]

## test
intervals = [(-4, -1), (0, 2), (3, 6), (7, 9), (11, 12), (14, 17)]
print(merge_interval(intervals, [1, 8]))


