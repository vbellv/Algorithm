def solution(lines):
    check_list = []
    
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            if lines[i][0] <= lines[j][0] <= lines[i][1] or lines[j][0] <= lines[i][0] <= lines[j][1]:
                start = max(lines[i][0], lines[j][0])
                end = min(lines[i][1], lines[j][1])
                
                for num in range(start, end):
                    check_list.append(num)
                    
    return len(set(check_list))