import math

def solution(names):
    answer = []
    
    for i in range(math.ceil(len(names) / 5)):
        answer.append(names[i*5])
    return answer