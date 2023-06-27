def solution(num, k):
    if str(k) in str(num):
        for idx, val in enumerate(str(num)):
            if str(k) == val:
                answer = str(num).index(val)+1
    else:
        answer = -1
    return answer