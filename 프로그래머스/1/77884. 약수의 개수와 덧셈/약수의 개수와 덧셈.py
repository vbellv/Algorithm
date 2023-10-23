def solution(left, right):
    answer, cnt = 0, 0
    
    for num in range(left, right+1):
        for nums in range(1, num//2+1):
            if num % nums == 0:
                cnt += 1
        cnt += 1 
        
        if cnt % 2 == 0: answer += num
        else: answer -= num

        cnt = 0
    
    return answer