import math
from collections import deque

def solution(progresses, speeds):
    n = len(progresses)
    data = deque([math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)])
    
    check_data = []
    cnt = 1
    check = data.popleft()
    
    while len(data) > 0:
        pop_num = data.popleft()

        if check >= pop_num:
            cnt += 1
        
        elif check < pop_num:
            check = pop_num
            check_data.append(cnt)
            cnt = 1
        
    check_data.append(cnt)   
    
    return check_data