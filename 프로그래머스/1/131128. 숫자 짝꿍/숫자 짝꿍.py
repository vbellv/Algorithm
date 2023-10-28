def solution(X, Y):
    check_list = []				# 정답을 받을 리스트 선언
    point_X, point_Y = 0, 0		# 포인터 선언
    
    # 오름차순으로 정렬
    X, Y = sorted(X), sorted(Y)
    
    while True:
        if point_X >= len(X) or point_Y >= len(Y):
            break
        
        if X[point_X] != Y[point_Y]:
            if min(X[point_X], Y[point_Y]) == X[point_X]:
                point_X += 1
            else:
                point_Y += 1
        else:
            check_list.append(X[point_X])
            point_X += 1
            point_Y += 1
    
    check_list = sorted(check_list, reverse=True)
    
    if len(check_list) == 0:
        return '-1'
    elif len(set(check_list)) == 1:
        return check_list[0]
    else:
        return ''.join(check_list)