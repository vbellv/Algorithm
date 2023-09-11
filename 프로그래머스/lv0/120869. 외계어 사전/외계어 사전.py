def solution(spell, dic):
    return 1 if any(all(i in word for i in spell) for word in dic) else 2