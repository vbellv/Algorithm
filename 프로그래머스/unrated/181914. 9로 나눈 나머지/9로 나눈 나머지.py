def solution(number):
    sum_num = 0
    
    for num in number:
        sum_num += int(num)
        
    return sum_num % 9