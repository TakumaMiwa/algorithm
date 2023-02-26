import collections
Item = collections.namedtuple('Item', ('weight', 'value'))

def optimum_subject_to_capacity(items, capacity):
    def optimum_subject_to_item_and_capacity(k, available_capacity):
        if k<0:
            return 0

        if V[k][available_capacity] == -1:
            without_curr_item = optimum_subject_to_item_and_capacity(k-1, available_capacity)
            with_curr_item = (0 if available_capacity < items[k].weight
                            else items[k].value + optimum_subject_to_item_and_capacity(k-1, available_capacity-items[k].weight))
            V[k][available_capacity] = max(without_curr_item, with_curr_item)

        return V[k][available_capacity]

    V = [[-1] * (capacity+1) for _ in range(len(items))]
    result = optimum_subject_to_item_and_capacity(len(items)-1, capacity)
    print(V)
    return result

## test
data = [(60, 5), (50, 3), (70, 4), (30, 2)]
items = [Item(x[1], x[0]) for x in data]
print(optimum_subject_to_capacity(items, 5))