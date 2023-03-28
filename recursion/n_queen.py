def n_queen(n):
    def supporter(row):
        if row==n:
            result.append(col_placement)
            return
        
        for col in range(n):
            if all(abs(col - c) not in (0, row-i) for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                supporter(row+1)
    result, col_placement = [], [0] * n
    supporter(0)
    return result
