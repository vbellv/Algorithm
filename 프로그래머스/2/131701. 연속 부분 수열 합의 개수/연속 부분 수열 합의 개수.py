from collections import deque

def solution(elements):
    answer = []

    for num in range(1, len(elements) + 1):
        queue = deque()
        total_elements = elements + elements[:num - 1]      
        while total_elements:
            number = total_elements.pop()
            queue.append(number)
            
            if len(queue) == num:
                answer.append(sum(queue))
                queue.popleft()

    return len(set(answer))
