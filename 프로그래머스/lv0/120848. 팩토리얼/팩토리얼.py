def factorial():
    num_list = [0] * 11
    
    num_list[0] = 1
    num_list[1] = 1
    
    for i in range(2, 11):
        num_list[i] = i * num_list[i-1]
    
    return num_list

def solution(n):
    num_list = factorial()
    answer = 0
    
    for i in range(1, 11):
        if num_list[i] <= n:
            answer = i
    
    return answer