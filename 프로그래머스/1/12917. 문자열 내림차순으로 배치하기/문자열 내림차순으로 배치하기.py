def solution(s):
    check_list = []
    
    alphabet_list = list(map(chr, range(122, 96, -1))) + [word.upper() for word in list(map(chr, range(122, 96, -1)))]
    
    for word in s:
        check_list.append((alphabet_list.index(word), word))
        
    check_list = sorted(check_list, key=lambda x: x[0])
    
    return ''.join([word[1] for word in check_list])