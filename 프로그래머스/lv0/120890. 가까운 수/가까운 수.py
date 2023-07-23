def solution(array, n):
    array.sort()
    check_list = []
    
    for i in array:
        check_list.append((i, abs(i-n)))

    check_list = sorted(check_list, key=lambda x : x[1])
    
    return check_list[0][0]
