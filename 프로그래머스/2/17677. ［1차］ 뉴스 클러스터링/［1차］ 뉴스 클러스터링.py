from collections import Counter

def make_component(word):
    words = []
    
    for i in range(len(word) - 1):
        check_word = word[i:i+2]
        
        if check_word.isalpha():
            words.append(check_word)
    return words

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_list = make_component(str1)
    str2_list = make_component(str2)
    
    count1 = Counter(str1_list)
    count2 = Counter(str2_list)
    
    intersection = count1 & count2
    union = count1 | count2
    
    intersection_count = sum(intersection.values())
    union_count = sum(union.values())
    
    if union_count == 0:
        return 65536
    else:
        return int(intersection_count / union_count * 65536)
