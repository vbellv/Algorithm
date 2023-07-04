def solution(i, j, k):
    cnt = 0
    for num in range(i, j+1):
        for i in ','.join(str(num)):
            if str(k) == i:
                cnt += 1
    return cnt