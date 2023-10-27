def base(n):
    num = ''
    
    while n > 0:
        n, mod = divmod(n, 3)
        num += str(mod)
        
    return num

def solution(n):
    num = base(n)
    
    return int(str(num), 3)