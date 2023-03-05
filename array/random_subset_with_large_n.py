import random
def random_subset(n, k):
    dic = {}
    for i in range(k):
        bef_idx = dic.get(i, i)
        r = random.randint(i, n-1)
        aft_idx = dic.get(r, r)
        dic[bef_idx] = aft_idx
        dic[aft_idx] = bef_idx
    return [dic[i] for i in range(k)]

## test
print(random_subset(10000, 5))