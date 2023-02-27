def largest_rectangle(heights):
    pillar_indices, max_rectangle_area = [], 0

    for i, h in enumerate(heights+[0]):
        while pillar_indices  and heights[pillar_indices[-1]] >= h:
            height = heights[pillar_indices.pop()]
            width = i if not pillar_indices else i - 1 - pillar_indices[-1]
            max_rectangle_area = max(max_rectangle_area, height*width)
        pillar_indices.append(i)
    return max_rectangle_area

## test
heights = [1, 4, 2, 5, 6, 3, 2, 6, 6, 6, 6, 1, 3]
print(largest_rectangle(heights))