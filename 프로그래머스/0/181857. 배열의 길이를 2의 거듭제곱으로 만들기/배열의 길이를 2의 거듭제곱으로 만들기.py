def solution(arr):
    length = 1
    
    while True:
        if length - len(arr) >= 0:
            arr += [0] * (length - len(arr))
            break
        
        length *= 2
    
    return arr