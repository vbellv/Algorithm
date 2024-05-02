def solution(myString, pat):
    cnt = 0
    
    for idx in range(0, len(myString)):
        if myString[idx:idx+len(pat)] == pat:
            cnt += 1
            
    return cnt
            