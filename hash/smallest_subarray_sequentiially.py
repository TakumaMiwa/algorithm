from collections import namedtuple
def smallest_subarray_sequentially(l, keywords):
    Subarray = namedtuple('Subarray', ('start', 'end'))
    keyword_to_idx = {k: i for i, k in enumerate(keywords)}
    latest_occurrence = [-1] * len(keywords)
    shortest_subarray_length = [float('inf')] * len(keywords)
    min_distance = float('inf')
    result = (-1, -1)

    for i, word in enumerate(l):
        if word in keyword_to_idx:
            keyword_idx = keyword_to_idx[word]
            if keyword_idx==0:
                shortest_subarray_length[keyword_idx] = 1
            elif shortest_subarray_length[keyword_idx - 1] != float('inf'):
                distance_to_previous_keyword = i - latest_occurrence[keyword_idx-1]
                shortest_subarray_length[keyword_idx] = distance_to_previous_keyword + shortest_subarray_length[keyword_idx-1]
            latest_occurrence[keyword_idx] = i


            if (keyword_idx==len(keywords)-1 and shortest_subarray_length[-1] < min_distance):
                min_distance = shortest_subarray_length[-1]
                result = Subarray(i-min_distance+1, i)
    return result

## test
l = ['apple', 'banana', 'apple', 'apple', 'dog', 'cat', 'apple', 'dog', 'banana', 'apple', 'cat', 'dog']
keywords = ['banana', 'cat', 'dog']
print(smallest_subarray_sequentially(l, keywords))