
def test_palindromic(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower()!=s[r].lower(): return False

        l, r = l+1, r-1
    return True

## test
s = "Able was I, ere I saw Elba!"
print(test_palindromic(s))