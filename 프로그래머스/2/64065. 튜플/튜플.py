def make_list(s):
    index_list, total_list = [], []
    
    for idx in range(len(s)):
        if idx != 0 and idx != len(s)-1:
            if s[idx] == '{' or s[idx] == '}':
                index_list.append(idx)
    
    for idx in range(0, len(index_list), 2):
        start = index_list[idx]
        end = index_list[idx+1]
        
        total_list.append(s[start+1:end].split(','))
    
    total_list = sorted(total_list, key=lambda x: len(x))
    answer = [list(map(int, nums)) for nums in total_list]
    
    return answer

def solution(s):    
    total_list = make_list(s)
    answer = []
    
    for nums in total_list:
        if len(nums) == 1:
            answer += nums
        if len(nums) > 1:
            for num in nums:
                if num not in answer:
                    answer.append(num)
    
    return answer