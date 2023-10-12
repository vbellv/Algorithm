def solution(n):
    return min([num for num in range(2, n+1) if n % num == 1])