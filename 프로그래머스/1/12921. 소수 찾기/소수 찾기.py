def solution(n):
    cnt = 0
    arr = [True] * (n+1)
    arr[1] = False
    
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for num in range(i+i, n+1, i):
                arr[num] = False
                
    for i in range(1, len(arr)):
        if arr[i]:
            cnt += 1
            
    return cnt