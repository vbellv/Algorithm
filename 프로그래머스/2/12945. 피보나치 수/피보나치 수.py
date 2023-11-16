def solution(n):
    fibo_list = [0] * (n+1)
    fibo_list[1] = 1
    
    for num in range(2, n+1):
        fibo_list[num] = fibo_list[num-2] + fibo_list[num-1]
        
    return fibo_list[n] % 1234567