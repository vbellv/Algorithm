def solution(score):
    rank_list = sorted([sum(scores) for scores in score], reverse = True)
    return [rank_list.index(sum(scores))+1 for scores in score]