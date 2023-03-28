def generate_matched_parens(n):
    def supporter(left_num, remain_num, l):
        if remain_num==0:
            result.append(''.join(l))
            return
        
        if left_num < n:
            supporter(left_num+1, remain_num, l+['('])

        if n - remain_num < left_num:
            supporter(left_num, remain_num-1, l+[')'])

    result = []
    supporter(1, n, ['('])
    return result

## test
print(generate_matched_parens(3))