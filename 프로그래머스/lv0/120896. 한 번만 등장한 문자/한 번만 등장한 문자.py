from collections import Counter

def solution(s):
    count = Counter(s)
    
    answer = ''
    
    for idx, val in count.items():
        if val == 1:
            answer += idx
    return ''.join(sorted(answer))
        