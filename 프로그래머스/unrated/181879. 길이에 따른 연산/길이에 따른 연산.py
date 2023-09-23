def solution(num_list):
    multiply_num = 1
    
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for num in num_list:
            multiply_num *= num
        return multiply_num