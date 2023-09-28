def solution(num):
    cnt = 0
    
    while True:
        if num > 1:
            if num % 2 == 0:
                num /= 2
            else:
                num = num * 3 + 1
            cnt += 1
        
        elif num == 1:
            if cnt != 0:
                return cnt
            
            elif cnt == 0:
                return 0
            break
        
        if cnt == 500:
            return -1
            break
        