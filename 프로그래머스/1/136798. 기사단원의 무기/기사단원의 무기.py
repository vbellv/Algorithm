def divisor(number):
    divisor_cnt = []
    
    for num in range(1, number+1):
        temp_cnt = 0
        for divisor in range(1, int(num**0.5)+1):
            if num % divisor == 0:
                temp_cnt += 1
                
        if num != 1:
            if num**0.5 == round(num**0.5, 0):
                temp_cnt = temp_cnt*2-1
            else:
                temp_cnt *= 2

        divisor_cnt.append(temp_cnt)
        temp_cnt = 0
        
    return divisor_cnt

def solution(number, limit, power):
    divisor_cnt = divisor(number)
    answer = []
    
    for num in divisor_cnt:
        if num > limit:
            num = power
        answer.append(num)
            
    return sum(answer)