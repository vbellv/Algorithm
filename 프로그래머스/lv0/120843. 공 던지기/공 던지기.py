def solution(numbers, k):
    idx, num = 0, 0
    answer = []
    
    while num < k:
        num += 1
        answer.append(numbers[idx])
        
        if idx == len(numbers)-1 or idx == len(numbers)-2:
            idx = (idx+2) % len(numbers)
        else:
            idx += 2
            
    return answer[-1]
        
        
            