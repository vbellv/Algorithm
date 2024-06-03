from collections import deque

def solution(people, limit):
    boat_count = 0
    
    people.sort()
    people = deque(people)
    
    while people:
        person = people.pop()
        if len(people) > 0 and person + people[0] <= limit:
            people.popleft()
        
        boat_count += 1
        
    return boat_count