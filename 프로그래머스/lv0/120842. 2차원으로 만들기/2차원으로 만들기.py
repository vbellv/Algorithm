def solution(num_list, n):
    
    answer = [[0 for i in range(n)] for i in range(len(num_list)//n)]
    
    for i in range(len(num_list)//n):
        for j in range(n):
            answer[i][j] = num_list.pop(0)
            
    return answer