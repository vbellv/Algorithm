def solution(numbers, target):
    count = 0
    
    def dfs(idx, current_sum):
        nonlocal count
        
        if idx == len(numbers):
            if current_sum == target:
                count += 1
            return
        
        dfs(idx + 1, current_sum + numbers[idx])
        dfs(idx + 1, current_sum - numbers[idx])

    dfs(0, 0)
    
    return count