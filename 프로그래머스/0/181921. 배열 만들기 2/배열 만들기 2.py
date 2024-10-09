def solution(l, r):
    answer = []
    
    for number in range(l, r + 1):
        if not set(str(number)) - set(['0', '5']):
            answer.append(number)
    
    return answer if answer else [-1]
    