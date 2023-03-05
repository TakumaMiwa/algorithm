import random
def random_sampling(l, k):
    if len(l) == k: return set(l)
    elif len(l) < k: raise ValueError 
    for i in range(k):
        r = random.randint(i, len(l)-1)
        l[i], l[r] = l[r], l[i]

    return set(l[:k])

## test
print(random_sampling([2, 3, 4, 5], 2))

