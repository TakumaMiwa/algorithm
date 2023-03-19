import heapq
from collections import defaultdict
def top_student(l):
    dic = defaultdict(list)
    for line in l:
        student, score = list(map(int, line.split(', ')))
        heapq.heappush(dic[student], score)
        if 3 < len(dic[student]): heapq.heappop(dic[student])

    max_mean = (0, 0)
    for key in dic.keys():
        max_mean = max(max_mean, (0, 0) if len(dic[key]) < 3 else ((sum(dic[key])/3), key))

    return max_mean

## test
data = [
    '11111, 12',
    '22222, 22',
    '33333, 42',
    '11111, 32',
    '22222, 42',
    '33333, 52',
    '33333, 62',
    '11111, 12',
    '22222, 32',
]

print(top_student(data))

