import random
def random_permutation(n):
    def random_sampling(l, k):
        if len(l) < k: raise ValueError 
        for i in range(k):
            r = random.randint(i, len(l)-1)
            l[i], l[r] = l[r], l[i]

        return l
    
    l = list(range(n))
    result = random_sampling(l, n)
    return result

## test
print(random_permutation(5))