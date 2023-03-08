def is_well_formed(s):
    stack = []
    dic = {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if c in dic: stack.append(dic[c])
        elif c != stack.pop(): return False
    return True

## test
print(is_well_formed("(){}[][]"))
print(is_well_formed("([){)}[][]"))