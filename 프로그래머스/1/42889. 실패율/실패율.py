def solution(N, stages):
    TOTAL_PERSON = len(stages)
    failuare, person_cnt = [], 0
    
    for stage in range(1, N+1):
        try:
            failuare.append((stage, (stages.count(stage) / (TOTAL_PERSON-person_cnt))))
            person_cnt += stages.count(stage)
        except:
            failuare.append((stage, 0))
        
    failuare = sorted(failuare, key=lambda x: x[1], reverse=True)
    
    return [num[0] for num in failuare]
    
print(solution(5, [4,4,4,4,4]))