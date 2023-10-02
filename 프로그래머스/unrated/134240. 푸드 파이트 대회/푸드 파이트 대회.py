def solution(food):
    arranged_food = ''
    
    for idx in range(len(food)):
        arranged_food += (food[idx] // 2) * str(idx)
    
    return arranged_food + '0' + arranged_food[::-1]
