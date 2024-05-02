def solution(arr):
    index = []
    
    for idx in range(len(arr)):
        if arr[idx] == 2:
            index.append(idx)
    
    if arr.count(2) > 1:
        return arr[index[0]:index[-1]+1]
    elif arr.count(2) == 1:
        return [2]
    else:
        return [-1]
    