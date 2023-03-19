from collections import Counter
def palindromic_permutation(s):
    dic = Counter(s)
    is_odd = False
    for key in dic.keys():
        if dic[key]%2:
            if is_odd: return False
            is_odd = True
    return True

## test
print(palindromic_permutation("aabbcd"))