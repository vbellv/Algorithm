def solution(babbling):
    cnt = 0
    baby = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for idx, baby_word in enumerate(baby):
            if baby_word*2 not in word:
                word = word.replace(baby_word, str(idx))
                
        if word.isdigit():
            cnt += 1
                
    return cnt