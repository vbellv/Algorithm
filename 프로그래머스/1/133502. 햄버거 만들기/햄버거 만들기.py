def solution(ingredient):
    hamburger = []
    cnt = 0
    
    for num in ingredient:
        hamburger.append(num)
        
        if hamburger[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                hamburger.pop()
            cnt += 1
            
    return cnt
