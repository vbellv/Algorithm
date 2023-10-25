def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    answer = 0
    
    for a, b in zip(A, B):
        answer += a * b
        
    return answer