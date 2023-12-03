def solution(myString):
    answer = []
    num = 0
    
    for word in myString:
        if word != 'x':
            num += 1
        elif word == 'x':
            answer.append(num)
            num = 0
    answer.append(num)
    
    return answer