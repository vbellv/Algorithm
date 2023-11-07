def solution(s, skip, index):
    alphabet = list(map(chr, range(97, 123)))
    skip_alphabet = [word for word in alphabet if word not in skip]
    
    answer = ''
    
    for word in s:
        answer += skip_alphabet[(skip_alphabet.index(word)+index)%len(skip_alphabet)]

    return answer