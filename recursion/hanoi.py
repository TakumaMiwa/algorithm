def hanoi(num_rings):
    ## O(2**n)
    def supporter(n, from_idx, to_idx):
        if n <= 0: return
        supporter(n-1, from_idx, 3-from_idx-to_idx)
        print(f"ring_{n} is moved: {from_idx} --> {to_idx}")
        supporter(n-1, 3-from_idx-to_idx, to_idx)
    supporter(num_rings, 0, 1)

## test
hanoi(3)
