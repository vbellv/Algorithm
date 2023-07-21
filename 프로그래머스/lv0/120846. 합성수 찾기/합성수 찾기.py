def solution(n):
    check_list = []
    
    for i in range(4, n+1):
        if (i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0):
            if i != 5 and i != 7:
                check_list.append(i)
                
    return len(check_list)