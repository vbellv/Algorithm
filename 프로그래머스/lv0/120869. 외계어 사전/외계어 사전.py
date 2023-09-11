def solution(spell, dic):
    if any(all(alphabet in word for alphabet in spell) for word in dic):
    	return 1
    else:
    	return 2