def mnemonic_phone_number(nums):
    dic = ('0', '1', 'ABC', 'DEF', 'GHI','JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')
    def supporter(l, k):
        if k==len(nums):
            result.append(l)
            return
        for i in range(len(dic[int(nums[k])])):
            supporter(l+[dic[int(nums[k])][i]], k+1)

    result = []
    supporter([], 0)
    return result

## test
print(mnemonic_phone_number('123'))
        
