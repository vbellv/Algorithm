def solution(arr, queries):
    for i in range(len(arr)):
        for query in queries:
            s, e, k = query
            if s <= i <= e and i % k == 0:
                arr[i] += 1
    return arr
