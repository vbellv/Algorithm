def solution(n, words):
    word_list = []
    current_word = ''
    cnt = 0
    
    for idx, word in enumerate(words):
        if not word_list:
            current_word = word
            word_list.append(word)
            cnt += 1
        else:
            if word not in word_list and word.startswith(current_word[-1]):
                word_list.append(word)
                current_word = word
                cnt += 1
            else:
                if (idx + 1) % n == 0:
                    return [n, cnt // n + 1]
                else:
                    return [(idx + 1) % n, cnt // n + 1]
                break
    
    if words == word_list:
        return [0, 0]