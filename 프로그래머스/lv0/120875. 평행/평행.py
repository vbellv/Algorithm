def slope_line(dots):
    check_list = []
    
    for i in range(len(dots)):
        for j in range(i+1, len(dots)):
            check_list.append(abs(dots[i][1]-dots[j][1]) / abs(dots[i][0]-dots[j][0]))
            
    return check_list

def solution(dots):
    check_list = slope_line(dots)
    cnt = 0
           
    for idx in range(len(check_list)//2):
        if check_list[idx] == check_list[-(idx+1)]:
            cnt += 1
            break
    
    if cnt != 0: return 1
    else: return 0

print(solution([[1, 2], [5, 1], [3, 6], [6, 3]])) # 1
print(solution([[3, 5], [4, 4], [8, 9], [6, 11]])) # 1
