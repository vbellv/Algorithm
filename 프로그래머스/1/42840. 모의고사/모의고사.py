def make_dict(answers):
    N = len(answers)
    PERSON1 = [1, 2, 3, 4, 5] * N
    PERSON2 = [2, 1, 2, 3, 2, 4, 2, 5] * N
    PERSON3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * N
    
    cnt_dict = {}
    cnt_1, cnt_2, cnt_3 = 0, 0, 0
    
    for num in range(1, 4):
        cnt_dict[num] = cnt_dict.get(num, 0)

    for i in range(len(answers)):
        if answers[i] == PERSON1[i]:
            cnt_1 += 1
        if answers[i] == PERSON2[i]:
            cnt_2 += 1
        if answers[i] == PERSON3[i]:
            cnt_3 += 1
            
    cnt_dict[1] = cnt_1
    cnt_dict[2] = cnt_2
    cnt_dict[3] = cnt_3
    
    return cnt_dict

def solution(answers):
    cnt_dict = make_dict(answers)
    answer = []

    for key, val in cnt_dict.items():
        if val == max(cnt_dict.values()):
            answer.append(key)
    
    return answer
