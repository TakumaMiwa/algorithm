def all_permutation(array):
    def supporter(idx, used_list):
        if idx==len(array):
            result.append(permutation.copy()) ## need to copy
            return
        
        for i in range(len(array)):
            if i not in used_list:
                permutation[idx] = array[i]
                supporter(idx+1, used_list+[i])
    
    result, permutation = [], [0] * len(array)
    supporter(0, [])
    return result

## test
print(all_permutation([2, 3, 5, 7]))