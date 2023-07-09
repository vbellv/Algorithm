def solution(array):
    arr_dict = {}
    check_list = []
    
    for i in array:
        arr_dict[i] = 0
    
    for i in array:
        arr_dict[i] += 1
    
    for idx, val in arr_dict.items():
        if val == max(arr_dict.values()):
            check_list.append(idx)
            
    if len(check_list) >= 2:
        return -1
    else:
        return check_list[0]