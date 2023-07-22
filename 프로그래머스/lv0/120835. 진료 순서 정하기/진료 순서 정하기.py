def solution(emergency):
    check_idx, check_val, answer = [], [], []
    
    for idx, val in enumerate(sorted(emergency, reverse=True)):
        check_idx.append(idx+1)
        check_val.append(val)
    print(check_idx, check_val)
        
    for i in range(len(check_idx)):
        for j in range(len(check_idx)):
            if emergency[i] == check_val[j]:
                answer.append(check_idx[j])
    
    return answer