from collections import defaultdict
def nearest_word_pair(words):
    min_distance = len(words)
    dic = defaultdict()
    for idx, word in enumerate(words):
        if word in dic: min_distance = min(min_distance, idx-dic[word])
        dic[word] = idx

    return min_distance

## test
s = 'All work and no play makes for no work no fun and no results'
print(nearest_word_pair(list(s.split())))