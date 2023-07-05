def solution(arr):
    check_list = []
    
    for i in arr:
        if check_list[-1:] != [i]:
            check_list.append(i)
    
    return check_list