from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    counts = sorted(list(count.values()), reverse=True)
    
    answer = 0
    sum_counts = 0
    
    for count in counts:
        if count < k:
            sum_counts += count
            answer += 1
        elif count >= k:
            return 1
        if sum_counts >= k:
            return answer
        