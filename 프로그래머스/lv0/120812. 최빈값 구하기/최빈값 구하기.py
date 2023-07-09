from collections import Counter

def solution(array):
    
    count = Counter(array)
    cnt = 0

    for idx, val in count.items():
        if val == max(count.values()):
            cnt += 1
        
    if cnt >= 2:
        return -1
    elif cnt == 1:
        return count.most_common(1)[0][0]