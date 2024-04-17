def solution(survey, choices):
    indicators = ['RT', 'CF', 'JM', 'AN']
    rank = {}
    answer = ''
    
    for ans in indicators:
        rank[ans[0]] = 0
        rank[ans[1]] = 0
    
    for idx in range(len(survey)):
        if choices[idx] in [1, 2, 3]:
            if choices[idx] == 1:
                rank[survey[idx][0]] += 3
            elif choices[idx] == 2:
                rank[survey[idx][0]] += 2
            elif choices[idx] == 3:
                rank[survey[idx][0]] += 1
        
        elif choices[idx] in [5, 6, 7]:
            if choices[idx] == 7:
                rank[survey[idx][1]] += 3
            elif choices[idx] == 6:
                rank[survey[idx][1]] += 2
            elif choices[idx] == 5:
                rank[survey[idx][1]] += 1
    
    for indicator in indicators:
        if rank[indicator[0]] < rank[indicator[1]]:
            answer += indicator[1]
        else:
            answer += indicator[0]
    
    return answer