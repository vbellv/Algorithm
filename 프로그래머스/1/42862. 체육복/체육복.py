def solution(n, lost, reserve):
    set_lost = sorted(list(set(lost) - set(reserve)))
    set_reserve = sorted(list(set(reserve) - set(lost)))
    
    check_list = [num for num in range(1, n+1) if num not in set_lost]
    
    for num in set_lost:
        if num-1 in set_reserve:
            check_list.append(num)
            set_reserve.remove(num-1)
        elif num+1 in set_reserve:
            check_list.append(num)
            set_reserve.remove(num+1)
            
    return len(check_list)
            
    
            
            
    
    
    
    
    
print(solution(5, [1, 3], [3, 2]))