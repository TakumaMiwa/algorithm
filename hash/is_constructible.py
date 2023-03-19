from collections import Counter
def is_constructible(letter, magazine):
    return not (Counter(letter) - Counter(magazine))
## test
print(is_constructible("aaa", "aaaa"))
print(is_constructible('aaaa', 'aaa'))