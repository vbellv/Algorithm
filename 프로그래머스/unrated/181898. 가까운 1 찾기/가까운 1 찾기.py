def solution(arr, idx):
    num = len(arr[:idx])
    arr = arr[idx:]
    
    if arr.count(1) >= 1:
        return arr.index(1) + num
    elif arr.count(1) == 0:
        return -1