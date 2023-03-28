def k_permutation(array, k):
    def supporter(idx, permutation, select_num):
        if select_num==0:
            result.append(permutation.copy())
            return
        
        for cur_idx in range(idx, len(array)-select_num+1):
            supporter(cur_idx+1, permutation+[array[cur_idx]], select_num-1)
    result = []
    supporter(0, [], k)
    return result

## test
print(k_permutation([1, 2, 3, 4, 5], 2))
