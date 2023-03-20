from functools import reduce
def render_calendar(l):
    l = reduce(lambda array, plan: array+[(plan[0], 0), (plan[1], 1)], l, [])
    l.sort()
    result = 0
    event_num = 0
    for event in l:
        if not event[1]: event_num += 1
        else:
            result = max(result, event_num)
            event_num -= 1

    return result

## test
l = [(1, 5), (6, 10), (11, 13), (14, 15), (2, 7), (8, 9), (12, 15), (4, 5), (9, 17)]
print(render_calendar(l))