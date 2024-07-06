def solution(strArr):
    count_of_word = dict.fromkeys(list(set([len(word) for word in strArr])), 0)
    count = float('-inf')
    answer = 0

    for word in strArr:
        count_of_word[len(word)] += 1
    
    for key, value in count_of_word.items():
        if value >= count:
            count = value
            answer = value
            
    return answer
