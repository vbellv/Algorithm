def solution(array):
    cnt = 0
    
    for arr in array:
        for i in str(arr):
            if int(i) == 7:
                cnt += 1
    
    return cnt