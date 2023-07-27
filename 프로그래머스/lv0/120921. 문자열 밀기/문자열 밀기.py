from collections import deque

def solution(A, B):
    A = deque([i for i in A])
    B = deque([i for i in B])
    cnt = 0
    
    if A == B:
        return cnt
    
    elif A != B:
        while True:
            A.rotate()
            cnt += 1
            
            if A == B:
                return cnt
            
            elif cnt > len(A):
                return -1