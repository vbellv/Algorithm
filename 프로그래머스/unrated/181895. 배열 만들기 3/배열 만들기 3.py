def solution(arr, intervals):
    results = []
    
    for nums in intervals:
        start, end = nums[0], nums[1]
        results += arr[start:end+1]
        
    return results