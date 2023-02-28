import collections

def fill_surrounded_regions(board):
    n, m = len(board), len(board[0])
    q = collections.deque([(i, j) for k in range(n) for i, j in ((k, 0), (k, m-1))] + 
                          [(i, j) for k in range(m) for i, j in ((0, k), (n-1, k))])

    while q:
        x, y = q.popleft()
        if 0<=x<n and 0<=y<m and board[x][y]=='W':
            board[x][y] = 'T'
            q.extend([(x-1, y), (x, y-1), (x+1, y), (x, y+1)])

    return [['W' if char=='T' else 'B' for char in row] for row in board]

## test
l = [['B', 'B', 'B', 'B'],
     ['W', 'B', 'W', 'B'],
     ['B', 'W', 'W', 'B'],
     ['B', 'B', 'B', 'B']]
[print(row) for row in fill_surrounded_regions(l)]