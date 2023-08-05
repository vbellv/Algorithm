import math

def solution(my_str, n):
    answer = []
    N = math.ceil(len(my_str)/n)

    for i in range(N):
        answer.append(my_str[i*n : i*n+n])
    
    return answer    