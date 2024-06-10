from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        start_price = queue.popleft()
        count = 0
        for price in queue:
            if start_price <= price:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
        
    return answer