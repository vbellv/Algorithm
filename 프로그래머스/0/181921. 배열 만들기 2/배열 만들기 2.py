import re

def solution(l, r):
    answer = []
    pattern = re.compile('^[05]+$')
    
    for number in range(l, r + 1):
        if number % 5 == 0:
            if pattern.match(str(number)):
                answer.append(number)
    
    return answer if answer else [-1]
    