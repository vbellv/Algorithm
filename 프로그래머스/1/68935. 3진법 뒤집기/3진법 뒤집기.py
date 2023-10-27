def base(n):
    num = ''
    
    while True:
        n, mod = divmod(n, 3)
        num += str(mod)
        
        if n == 0:
            break
        
    return num

def solution(n):
    num = base(n)
    
    return int(str(num), 3)