from collections import Counter
def smallest_subarray(l, keywords):
    dic_keywords = Counter(keywords)
    result = (-1, -1)
    remaining = len(keywords)
    left = 0
    for right, p in enumerate(l):
        if p in keywords:
            dic_keywords[p] -= 1
            if dic_keywords[p] >= 0: remaining -= 1
    while remaining == 0:
        if result==(-1, -1) or right - left < result[1] - result[0]:
            result = (left, right)
        pl = l[left]
        if pl in keywords:
            dic_keywords[pl] += 1
            if dic_keywords[pl] > 0:
                remaining += 1
        left += 1
    return result

## test
l = ['apple', 'banana', 'apple', 'apple', 'dog', 'cat', 'apple', 'dog', 'banana', 'apple', 'cat', 'dog']
keywords = {'banana', 'cat'}
print(smallest_subarray(l, keywords))