def solution(k, score):
    score_list, answer = [], []
    
    for idx in range(len(score)):
        score_list.append(score[idx])
        score_list.sort(reverse=True)

        answer.append(score_list[:k][-1])
            
    return answer