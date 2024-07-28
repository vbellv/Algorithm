def solution(arr):
    answer = []
    
    n = len(arr)
    m = len(arr[0])
    
    if n > m:
        for array in arr:
            for _ in range(n - m):
                array.append(0)
            answer.append(array)
    elif n < m:
        for _ in range(m - n):
            arr.append([0] * m)
        answer = arr
    else:
        answer = arr
        
    return answer
