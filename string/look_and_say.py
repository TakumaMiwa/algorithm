def look_and_say(n):
    def successive_num(start, l):
        key = l[start]
        while start < len(l) and l[start]==key:
            start += 1

        return start
    
    seq = '1'
    for _ in range(n-1):
        start = 0
        new_seq = ''
        while start < len(seq):
            end = successive_num(start, seq)
            new_seq += str(end-start) + str(seq[start])
            start = end
        seq = new_seq
    return seq

## test
print(look_and_say(5))


