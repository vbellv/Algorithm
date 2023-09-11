def solution(spell, dic):
    return 1 if any(all(alphabet in word for alphabet in spell) for word in dic) else 2