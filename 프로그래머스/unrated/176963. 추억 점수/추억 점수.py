def solution(name, yearning, photo):
    photo_dict = {}
    score_list = []
    score = 0
    
    for idx in range(len(name)):
        photo_dict[name[idx]] = photo_dict.get(idx, 0)
        photo_dict[name[idx]] = yearning[idx]
    
    for name_list in photo:
        for name in name_list:
            try:
                score += photo_dict[name]
            except:
                pass
            
        score_list.append(score)
        score = 0
    
    return score_list