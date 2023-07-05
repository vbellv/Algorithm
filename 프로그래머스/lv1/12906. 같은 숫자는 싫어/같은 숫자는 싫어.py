def solution(arr):
    check_list = [arr[0]]
    
    for i in range(len(arr)):
        if check_list[-1] != arr[i]:
            check_list.append(arr[i])
    
    return check_list