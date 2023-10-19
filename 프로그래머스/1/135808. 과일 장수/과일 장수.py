def solution(k, m, score):
    profit = 0
    
    for idx, num in enumerate(sorted(score, reverse=True)):
        if idx % m == 0:
            temp_list = []
        temp_list.append(num)

        if len(temp_list) == m:
            profit += temp_list[-1] * m
                
    return profit