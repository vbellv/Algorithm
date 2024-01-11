from itertools import product

def solution(word):
    WORD = ['A', 'E', 'I', 'O', 'U']
    word_list = []
    
    for i in range(1, len(WORD)+1):
        for words in list(product(WORD, repeat=i)):
            word_list.append(''.join(words))
    
    return sorted(word_list).index(word) + 1