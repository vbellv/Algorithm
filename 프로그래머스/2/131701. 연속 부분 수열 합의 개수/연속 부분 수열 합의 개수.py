def solution(elements):
    answer = set()
    
    n = len(elements)
    total_elements = elements * 2
    
    for num in range(1, n + 1):
        for i in range(n):
            sum_array = sum(total_elements[i : i + num])
            answer.add(sum_array)
            
    return len(answer)
