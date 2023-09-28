def harshad_num(x):
    num = 0
    
    while True:
        if len(str(x)) == 1:
            num += x
            break
            
        num += x % 10
        x //= 10
        
    return num

def solution(x):
    num = harshad_num(x)
    return True if x % num == 0 else False