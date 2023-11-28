def solution(a, b):
    one = str(a)+str(b)
    two = str(b)+str(a)
    
    return max(int(one), int(two))