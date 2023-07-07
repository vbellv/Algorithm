def solution(s):
    
    check_left = []
    check_right = []
    check = []
    
    for idx, val in enumerate(s):
        if val == '(':
            check_left.append((idx, val))
        else:
            check_right.append((idx, val))
            
    if len(check_left) != len(check_right):
        return False
    
    else:
        if check_left[0][0] == 0 and check_left[-1][0] < check_right[-1][0] :
            for i in range(len(check_left)):
                if check_left[i][0] < check_right[i][0]:
                    if check_left[i][0] - check_right[i][0] == 1 or 2:
                        check.append('True')
                else:
                    check.append('False')
        else:
            return False

    if 'False' in check:
        return False
    else:
        return True