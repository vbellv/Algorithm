def solution(X, Y):
    check_list = []
    point_X, point_Y = 0, 0
    
    X, Y = sorted(X), sorted(Y)
    
    if len(X) > len(Y):
        min_len = Y
        max_len = X
    else:
        min_len = X
        max_len = Y
    
    while True:
        if point_X >= len(min_len) or point_Y >= len(max_len):
            break
        
        if min_len[point_X] != max_len[point_Y]:
            if min(min_len[point_X], max_len[point_Y]) == min_len[point_X]:
                point_X += 1
            else:
                point_Y += 1
        else:
            check_list.append(min_len[point_X])
            point_X += 1
            point_Y += 1
    
    check_list = sorted(check_list, reverse=True)
    
    if len(check_list) == 0:
        return '-1'
    
    elif len(set(check_list)) == 1:
        return check_list[0]
    
    else:
        return ''.join(check_list)
