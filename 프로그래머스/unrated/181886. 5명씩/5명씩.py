import math

def solution(names):
    answer = []
    
    if len(names) <= 5:
        return [names[0]]
    else:
        for i in range(math.ceil(len(names) / 5)):
            answer.append(names[i*5])
        return answer