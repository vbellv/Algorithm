import math

def solution(names):
    return [names[i*5] for i in range(math.ceil(len(names) / 5))]