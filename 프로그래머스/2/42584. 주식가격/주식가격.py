from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        start_price = queue.popleft()
        count = 0
        
        for price in queue:
            if start_price > price:
                count += 1
                break
            count += 1
            
        answer.append(count)
        
    return answer