def spiral_order(l):
    def in_clockwise(offset):
        if offset == len(l) - 1 - offset:
            spiral_ordering.append(l[offset][offset])
            return
        
        spiral_ordering.extend(l[offset][offset:-1-offset])
        spiral_ordering.extend(list(zip(*l))[-1-offset][offset:-1-offset])
        spiral_ordering.extend(l[-1-offset][-1-offset:offset:-1])
        spiral_ordering.extend(list(zip(*l))[offset][-1-offset:offset:-1])

    spiral_ordering = []
    for i in range((len(l)+1)//2):
        in_clockwise(i)
    return spiral_ordering

## test

l = [[1, 2, 3], 
     [4, 5, 6],
     [7, 8, 9]]

print(spiral_order(l))