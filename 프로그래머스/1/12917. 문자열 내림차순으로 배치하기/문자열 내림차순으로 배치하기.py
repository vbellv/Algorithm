def solution(s):
    alphabet_list = list(map(chr, range(122, 96, -1))) + [word.upper() for word in list(map(chr, range(122, 96, -1)))]
    
    check_list = sorted([(alphabet_list.index(word), word) for word in s], key=lambda x: x[0])
            
    return ''.join([word[1] for word in check_list])