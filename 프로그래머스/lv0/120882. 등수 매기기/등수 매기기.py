def solution(score):
    rank_score, cnt, check = 101, 0, 0
    rank_dict = {}
    answer = []
    
    for rank in sorted([sum(scores)/2 for scores in score], reverse=True):
        if rank < rank_score:
            cnt += 1
            
            if check != 0:
                cnt += check
                check = 0
                
            rank_dict[rank] = cnt
            rank_score = rank
            
        elif rank == rank_score:
            rank_dict[rank] = cnt
            check += 1
            
    for scores in score:
        answer.append(rank_dict[sum(scores)/2])
        
    return answer

print(solution([[80, 70], [90, 50], [90, 50], [90, 50], [40, 70], [50, 80]]))
    
    
            
            