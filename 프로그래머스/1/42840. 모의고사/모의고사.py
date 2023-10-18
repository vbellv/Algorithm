def make_dict(answers):
    N = len(answers)
    PERSON1 = [1, 2, 3, 4, 5] * N
    PERSON2 = [2, 1, 2, 3, 2, 4, 2, 5] * N
    PERSON3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * N
    
    cnt_dict = {}
    
    for num in range(1, 4):
        cnt_dict[num] = cnt_dict.get(num, 0)

    for i in range(len(answers)):
        if answers[i] == PERSON1[i]:
            cnt_dict[1] += 1
        if answers[i] == PERSON2[i]:
            cnt_dict[2] += 1
        if answers[i] == PERSON3[i]:
            cnt_dict[3] += 1
    
    return cnt_dict

def solution(answers):
    cnt_dict = make_dict(answers)
    
    return [key for key, val in cnt_dict.items() if val == max(cnt_dict.values())]
    