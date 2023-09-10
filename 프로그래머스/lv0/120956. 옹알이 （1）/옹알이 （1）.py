from itertools import permutations

def solution(babbling):
    baby = ["aya", "ye", "woo", "ma"]
    word_list = []
    cnt = 0
    
    words = list(permutations(baby, 2)) + list(permutations(baby, 3)) + list(permutations(baby, 4))
    
    for word in words:
        word_list.append(''.join(word))
    word_list += baby
    
    for word in babbling:
        if word in word_list:
            cnt += 1
            
    return cnt