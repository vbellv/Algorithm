def make_index_arr(cards, goal):
    cards_index = []
    
    try:
        for word in cards:
            cards_index.append(goal.index(word))
    except:
        pass
    
    return cards_index

def solution(cards1, cards2, goal):
    cards1_index = make_index_arr(cards1, goal)
    cards2_index = make_index_arr(cards2, goal)
    
    if len(cards1_index) + len(cards2_index) == len(goal):
        if cards1_index == sorted(cards1_index) and cards2_index == sorted(cards2_index): 
            return 'Yes'
        else: 
            return 'No'
    else: 
        return 'No'