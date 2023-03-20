def salary_threshold(l, target):
    diff = sum(l) - target
    l.sort()
    i = 1
    while i <= len(l):
        if i==len(l):
            width = l[0]
        else:
            width = l[-i] - l[-i-1]
        if diff <= i * width:
            return l[-i] - (diff / i)
        diff -= i * width
        i += 1
    
## test
l = [90, 30, 100, 40, 20]
print(salary_threshold(l, 210))