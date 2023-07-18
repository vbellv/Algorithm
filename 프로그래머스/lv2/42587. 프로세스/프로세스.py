from collections import deque

def solution(priorities, location):
    queue = deque((idx, val) for idx, val in enumerate(priorities))
    answer = 0
    
    while True:
        pop_num = queue.popleft()
        if any(pop_num[1] < queue[i][1] for i in range(len(queue))):
            queue.append(pop_num)
            
        else:
            answer += 1
            if pop_num[0] == location:
                return answer