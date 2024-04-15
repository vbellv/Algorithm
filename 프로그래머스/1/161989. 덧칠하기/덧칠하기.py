def solution(n, m, section):
    current, cnt = 0, 0
    
    for idx in range(len(section)):
        if current < section[idx]:
            current = section[idx] + m - 1
            cnt += 1

    return cnt
