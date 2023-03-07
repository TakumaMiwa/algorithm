def reverse_words(l):
    def reverse_word(start, end):
        while start < end:
            l[start], l[end] = l[end], l[start]
            start, end = start+1, end-1

    l.reverse()
    start = 0
    while True:
        if ' ' not in l[start:]: break
        end = l[start:].index(' ') + start
        reverse_word(start, end-1)
        start = end + 1
    reverse_word(start, len(l)-1)

    return ''.join(l)

## test
s = "Alice likes Bob"
l = list(s) # test data
print(reverse_words(l))