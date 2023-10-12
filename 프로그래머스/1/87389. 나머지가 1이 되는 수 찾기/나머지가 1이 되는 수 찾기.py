def solution(n):
    answer = 0
    
    for num in range(2, (n-1)//2+1):
        if (n-1) % num == 0:
            answer = num
            break
        else:
            answer = n - 1
    
    return answer