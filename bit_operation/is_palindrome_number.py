import math
def is_palindrome_number(x):
    digits_num = math.floor(math.log10(x))
    
    while 10 <= x:
        if x//(10**digits_num) != x%10: return False
        x %= 10**digits_num
        x //= 10
        digits_num -= 2
    return True

print(is_palindrome_number(1231))
print(is_palindrome_number(12321))
