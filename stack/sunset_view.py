def sunset_view(l):
    result = []
    for i, height in enumerate(l):
        while result and l[result[-1]] <= height:
            result.pop()
        result.append(i)
    return result

## test
print(sunset_view([1, 7, 3, 6, 5]))