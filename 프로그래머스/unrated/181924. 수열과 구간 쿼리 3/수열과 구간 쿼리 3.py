def solution(arr, queries):
    for query in queries:
        i, j = query[0], query[1]
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr