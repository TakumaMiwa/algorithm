def longest_distinct_subarray(l):
    dic = {}
    pre_idx = 0
    max_length = 0
    for i, element in enumerate(l):
        if element in dic:
            max_length = max(max_length, i-pre_idx)
            for _ in range(dic[element]-pre_idx+1):
                del dic[l[pre_idx]]
                pre_idx += 1
        dic[element] = i

    return max_length

## test
l = [1, 2, 1, 3, 4, 5, 3, 6, 5, 3]
print(longest_distinct_subarray(l))

        
