def rotate(l):
    for i in range((len(l)+1)//2):
        for j in range(i, len(l)-1-i):
            l[i][j], l[j][-1-i], l[-1-i][-1-j], l[-1-j][i] = l[-1-j][i], l[i][j], l[j][-1-i], l[-1-i][-1-j]

## test
l = [[1, 2, 3], 
     [4, 5, 6],
     [7, 8, 9]]

rotate(l)
print(l)