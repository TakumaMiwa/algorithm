import functools
def roman_to_int(roman):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    threshold = 1
    result = 0
    for c in reversed(roman):
        if dic[c] < threshold: result -= dic[c]
        else: result += dic[c]

        threshold = max(threshold, dic[c])

    return result

def roman_to_int2(roman):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    return functools.reduce(lambda result, i: result - dic[roman[i]] if roman[i] < roman[i+1] else result + dic[roman[i]], range(len(roman)-1), dic[roman[-1]])

## test
print(roman_to_int("LIX"))
print(roman_to_int2("LIX"))