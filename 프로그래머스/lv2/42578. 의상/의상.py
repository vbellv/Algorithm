from collections import Counter

def solution(clothes):
    answer = 1
    count = Counter([kind for name, kind in clothes])
    
    for num in count.values():
        answer *= (num+1)
    
    return answer-1