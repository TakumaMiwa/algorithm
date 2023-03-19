def collatz_convergence(n):
    dic = set()
    for i in range(2, n+1):
        sequence = set()
        num = i
        while i <= num:
            ## hypothesis is disproved.
            if num in sequence:
                print(f'case i={i}: disproved!')
                return False

            sequence.add(num)
            if num in dic:
                break
            else:
                dic.add(num)
                if num%2: num = 3 * num + 1
                else: num //= 2

        print(f'case i={i}: proved!')

## test
collatz_convergence(1000)