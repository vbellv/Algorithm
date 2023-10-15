def solution(s, n):
    answer = ''
    alphabet = [chr(num) for num in range(97, 123)]
    
    for word in s:
        if word in alphabet:
            answer += alphabet[(alphabet.index(word) + n) % 26]
        else:
            if word.lower() in alphabet:
                answer += alphabet[(alphabet.index(word.lower()) + n) % 26].upper()
            else:
                answer += ' '
                
    return answer