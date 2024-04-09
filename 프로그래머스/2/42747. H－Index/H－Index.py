def solution(citations):
    sort_list = sorted(citations, reverse=True)
    max_val = 0
    
    for num in range(1, len(sort_list) + 1):
        cnt = 0
        for idx in range(len(citations)):
            if citations[idx] >= num:
                cnt += 1
        if cnt >= num:
            max_val = max(max_val, num)
            
    return max_val