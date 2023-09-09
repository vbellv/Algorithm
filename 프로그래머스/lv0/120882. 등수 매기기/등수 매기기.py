def solution(score):
    ranks = sorted([sum(scores) for scores in score], reverse=True)
    
    rank_score, cnt, check = 201, 0, 0
    rank_dict = {}
    
    for rank in ranks:
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

    answer = [rank_dict[sum(scores)] for scores in score]
    
    return answer
