def solution(t, p):
    idx, cnt = 0, 0
    
    while True:
        num = t[0+idx:len(p)+idx]
        
        if int(num) <= int(p):
            cnt += 1
        
        if len(p)+idx == len(t):
            break
        
        idx += 1
            
    return cnt