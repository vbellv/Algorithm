def solution(t, p):
    idx, cnt = 0, 0
    
    while len(p)+idx <= len(t):
        num = t[0+idx:len(p)+idx]
        
        if int(num) <= int(p):
            cnt += 1

        idx += 1
            
    return cnt