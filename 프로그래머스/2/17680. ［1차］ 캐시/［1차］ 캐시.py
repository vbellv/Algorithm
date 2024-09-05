from collections import deque

def solution(cacheSize, cities):
    queue = deque()
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    else:
        for city in cities:
            city = city.lower()
            if len(queue) < cacheSize:
                if city in queue:
                    queue.remove(city)
                    answer += 1
                else:
                    answer += 5
            else:
                if city in queue:
                    queue.remove(city)
                    answer += 1
                else:
                    queue.popleft()
                    answer += 5
            queue.append(city)

        return answer
