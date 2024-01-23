def solution(my_string, queries):
    my_string = list(my_string)
    for nums in queries:
        start, end = nums[0], nums[1]
        my_string[start:end+1] = my_string[start:end+1][::-1]
        
    return ''.join(my_string)