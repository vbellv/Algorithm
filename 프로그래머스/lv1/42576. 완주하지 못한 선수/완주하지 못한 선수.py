from collections import Counter

def solution(participant, completion):
    answer = ''
    part = Counter(participant)
    com = Counter(completion)

    for name in part:
        if part[name] != com[name]:
            answer = name

    return answer