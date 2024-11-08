from collections import Counter


def solution(topping):
    answer = 0
    right = Counter(topping)
    left = set()
    
    for top in topping:
        right[top] -= 1
        left.add(top)
        
        if right[top] == 0:
            del right[top]
            
        if len(right) == len(left):
            answer += 1 
    
    return answer