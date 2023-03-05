import itertools
import random
import bisect
def random_generate(nums, probs):
    new_probs = [0] + list(itertools.accumulate(probs))
    r = random.random()
    return nums[bisect.bisect(new_probs, r)-1]
    
## test
nums = [3, 5, 7, 11]
probs = [1/2, 1/3, 1/9, 1/18]
result = [0, 0, 0, 0]
for _ in range(500000):
    output = random_generate(nums, probs)
    idx = nums.index(output)
    result[idx] += 1

print(result)
        

