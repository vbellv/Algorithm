def solution(n):
    cnt = 1
    
    for i in range(1, n+1):
        num_sum = 0
        num_sum += i
        for j in range(i+1, n+1):
            num_sum += j
            if num_sum == n:
                cnt += 1
                break
            elif num_sum > n:
                break
    
    return cnt