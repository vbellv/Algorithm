def solution(sides):
    sides_in_max_cnt, sides_out_max_cnt = 0, 0
    
    # 제시된 두 변의 길이 중 max가 있을 때
    for _ in range(max(sides)-min(sides)+1, max(sides)+1):
        sides_in_max_cnt += 1        
    # 제시된 두 변의 길이 외에 max가 있을 때
    for _ in range(max(sides)+1, sum(sides)):
        sides_out_max_cnt += 1
        
    return sides_in_max_cnt + sides_out_max_cnt
    