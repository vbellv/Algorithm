def solution(keymap, targets):
    target_dict = {}
    answer = []
    
    total_targets = keymap + targets
    
    for target in total_targets:
        for word in target:
            target_dict[word] = 999
    
    for key in keymap:
        for idx in range(len(key)):
            try:
                if target_dict[key[idx]] > idx + 1:
                    target_dict[key[idx]] = idx + 1
            except:
                pass
    
    for target in targets:
        cnt = 0
        for word in target:
            cnt += target_dict[word]
        if cnt >= 999:
            cnt = -1
        answer.append(cnt)
        
    return answer

    