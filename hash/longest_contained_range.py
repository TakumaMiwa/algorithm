def longest_contained_range(l):
    dic = set(l)
    max_size = 0
    while dic:
        base = dic.pop()

        lower_bound = base - 1
        while lower_bound in dic:
            dic.remove(lower_bound)
            lower_bound -= 1

        upper_bound = base + 1
        while upper_bound in dic:
            dic.remove(upper_bound)
            upper_bound += 1

        max_size = max(max_size, upper_bound-lower_bound-1)

    return max_size

## test
l = [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]
print(longest_contained_range(l))