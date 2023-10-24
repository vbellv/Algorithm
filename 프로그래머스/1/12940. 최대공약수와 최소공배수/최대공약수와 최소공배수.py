def solution(n, m):
    lcm = 0
    
    for num in range(1, (max(n, m)//2+1)):
        if n % num == 0 and m % num == 0:
            lcm = num
            
    gcd = (n*m) // lcm
    
    return [lcm, gcd]