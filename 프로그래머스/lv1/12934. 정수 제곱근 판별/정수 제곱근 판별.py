def solution(n):
    return int(n**(1/2)+1)**2 if int(n**(1/2))**2 == n else -1