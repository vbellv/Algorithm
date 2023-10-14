def solution(s):
    answer = ''
    s = s.split(' ')
    
    for idx in range(len(s)):
        for num, word in enumerate(s[idx]):
            if num % 2 == 0:
                answer += word.upper()
            else:
                answer += word.lower()
        
        answer += ' '
        
    return answer[:-1]