def solution(s):
    total_cnt, same_cnt, not_same_cnt = 0, 0, 0

    while len(s) >= 1:
        for i in range(len(s)):
            if s[i] == s[0]:
                same_cnt += 1
            else:
                not_same_cnt += 1

            if same_cnt == not_same_cnt:
                s = s[i+1:]
                total_cnt += 1

                same_cnt, not_same_cnt = 0, 0
                break

        if same_cnt + not_same_cnt == len(s):
            if same_cnt + not_same_cnt >= 1:
                total_cnt += 1
            break
            
    return total_cnt