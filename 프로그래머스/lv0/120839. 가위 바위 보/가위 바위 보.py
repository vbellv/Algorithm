def solution(rsp):
    answer = ''
    for num in rsp:
        if num == '2':
            answer += '0'
        elif num == '0':
            answer += '5'
        else:
            answer += '2'
    return answer