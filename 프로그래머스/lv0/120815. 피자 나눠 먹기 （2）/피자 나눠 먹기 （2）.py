def solution(n): 
    return min([i for i in range(1, n+1) if ((i*6) % n) == 0])