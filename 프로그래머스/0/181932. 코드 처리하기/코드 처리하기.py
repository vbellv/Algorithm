def solution(code):
    flag = 0
    answer = ''
    
    for index in range(len(code)):
        if flag:
            if code[index] == '1':
                flag = 0
            if index % 2 != 0 and code[index] not in ['0', '1']:
                answer += code[index]
        else:
            if code[index] == '1':
                flag = 1
            if index % 2 == 0 and code[index] not in ['0', '1']:
                answer += code[index]
    
    if len(answer) == 0:
        return 'EMPTY'
    else:
        return answer
