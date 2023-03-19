from collections import Counter
def frequent_strings(l, k):
    dic = Counter(l)
    print(dic)
    return [item[0] for item in dic.most_common(k)]

## test
l = ['a', 'a', 'a', 'c', 'b', 'b']
print(frequent_strings(l, 2))
