def solution(picture, k):
    answer = []
    
    for words in picture:
        temp = []
        for word in words:
            temp += [word * k]
        for _ in range(k):
            answer.append(''.join(temp))
    
    return answer
