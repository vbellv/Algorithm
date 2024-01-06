def solution(s):
    answer = []
    
    s = s.lstrip('{').rstrip('}').split('},{')
    s = sorted([nums.split(',') for nums in s], key = lambda x: len(x))
    
    for num_list in s:
        for num in num_list:
            if num not in answer:
                answer.append(num)
    
    return list(map(int, answer))