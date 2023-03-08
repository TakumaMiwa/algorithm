def rpn_expression(s):
    stack = []
    ops = {'+': lambda y, x: x + y,
           '-': lambda y, x: x - y,
           '*': lambda y, x: x * y,
           '/': lambda y, x: x / y}
    nums = s.split(',')
    for num in nums:
        if num in ops:
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[num](a, b))
        else:
            stack.append(int(num))
    return stack.pop()

## test

print(rpn_expression("3,4,+,2,*,1,+"))