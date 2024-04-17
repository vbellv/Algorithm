def rank(number):
    if number == 6:
        return 1
    elif number == 5:
        return 2
    elif number == 4:
        return 3
    elif number == 3:
        return 4
    elif number == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    remove_lottos = lottos.copy()
    correct_cnt = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            correct_cnt += 1
            remove_lottos.remove(lotto)
    
    good_cnt = correct_cnt + remove_lottos.count(0)
    bad_cnt = correct_cnt
    
    return [rank(good_cnt), rank(bad_cnt)]
        