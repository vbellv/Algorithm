def solution(arr, queries):
    answer = []
    
    for query in queries:
        s, e, k = query        
        array = arr[s:e+1]
        flag = -1
        
        for number in sorted(array):
            if number > k:
                flag = number
                break
        answer.append(flag)
            
    return answer
