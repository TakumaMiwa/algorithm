def score_combination(final_score, scores):
    count = [0]
    def supporter(idx, score):
        if score==0:
            count[0] += 1
            return
        num = 0
        while scores[idx] <= score:
            supporter(idx+1, score-scores[idx]*num)
            num += 1
    supporter(0, final_score)
    return count[0]

## test
print(score_combination(12, [2, 3, 7]))