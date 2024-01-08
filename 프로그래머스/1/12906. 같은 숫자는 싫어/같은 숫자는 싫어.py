def solution(arr):
    answer = list()
    
    for num in arr:
        if answer[-1:] != [num]:
            answer.append(num)
            
    return answer