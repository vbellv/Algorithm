from collections import Counter

def solution(before, after):
    diff = Counter(before) - Counter(after)
    if len(diff) == 0:
        return 1
    else:
        return 0
    