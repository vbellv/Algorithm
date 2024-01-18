def solution(myString, pat):
    words = ''
    
    for word in myString:
        if word == 'A':
            words += 'B'
        elif word == 'B':
            words += 'A'
            
    if pat in words:
        return 1
    else:
        return 0