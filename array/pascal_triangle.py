import math
def pascal_triangle(n):
    if n==0: return [1]
    elif n==1: return [1, 1]
    result = []
    n_fac = math.factorial(n)
    for i in range(n+1):
        coefficient = n_fac // (math.factorial(n-i)*math.factorial(i))
        result.append(coefficient)

    return result

## test
print(pascal_triangle(5))