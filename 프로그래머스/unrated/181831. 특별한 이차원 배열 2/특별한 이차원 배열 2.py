def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == arr[j][i]:
                answer.append(0)
            else:
                answer.append(1)
                
    if sum(answer) == 0: return 1
    else: return 0