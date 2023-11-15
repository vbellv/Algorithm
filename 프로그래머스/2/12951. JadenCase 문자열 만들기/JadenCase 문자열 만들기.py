def solution(s):
    answer = ''
    
    s = s.lower().split(' ')
    for word in s:
        word = word.capitalize()
        answer += word
        answer += ' '
        
    return answer[:-1]
    