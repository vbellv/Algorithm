def solution(num_list):
    multiply_num = 1
    
    for num in num_list:
        multiply_num *= num
        
    if multiply_num > sum(num_list) ** 2:
        return 0
    else:
        return 1