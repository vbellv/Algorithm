def solution(num, total):
    for i in range(num):
        total -= i
        
    number = total // num
    
    return [number + i for i in range(num)]