def solution(emergency):
    check_list, answer = [], []
    
    for idx, val in enumerate(sorted(emergency, reverse=True)):
        check_list.append((idx+1, val))
        
    for i in range(len(check_list)):
        for j in range(len(check_list)):
            if emergency[i] == check_list[j][1]:
                answer.append(check_list[j][0])
    
    return answer