def solution(babbling):
    cnt = 0
    baby = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for idx, baby_word in enumerate(baby):
            word = word.replace(baby_word, str(idx))

        for num in range(len(word)-1):
            if word[num] == word[num+1]:
                word = word.replace(word[num], '*')
        
        if word.isdigit():
            cnt += 1
                    
    return cnt