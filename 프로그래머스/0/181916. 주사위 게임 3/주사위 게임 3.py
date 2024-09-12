from collections import Counter


def solution(a, b, c, d):
    scores = sorted(list(Counter([a, b, c, d]).items()), key=lambda x: (x[1], x[0]), reverse=True)
    keys = list(Counter([a, b, c, d]).keys())
    
    if len(scores) == 1:
        return 1111 * scores[0][0]
    elif len(scores) == 2:
        if scores[0][1] == 3:
            return (10 * scores[0][0] + scores[1][0]) ** 2
        else:
            return (scores[0][0] + scores[1][0]) * abs(scores[0][0] - scores[1][0])
    elif len(scores) == 3:
        return scores[1][0] * scores[2][0]
    else:
        return min(keys)
