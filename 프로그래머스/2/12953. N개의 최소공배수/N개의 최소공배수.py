def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def solution(arr):
    lcm = arr[0] * arr[1] // gcd(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        lcm = lcm * arr[i] // gcd(lcm, arr[i])
        
    return lcm