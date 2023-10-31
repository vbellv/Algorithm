def solution(d, budget):
    cnt = 0
    d.sort()
    
    for num in d: 
        budget -= num
        
        if budget < 0:
            break
            
        cnt += 1
        
    return cnt