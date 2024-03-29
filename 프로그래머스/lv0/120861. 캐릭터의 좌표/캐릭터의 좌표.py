def solution(keyinput, board):
    start_point = [0, 0]
    key_dict = {'up': (0, 1), 'down': (0, -1), 'left': (-1, 0), 'right': (1, 0)}
    
    WIDTH = (board[0]-1) // 2
    HEIGHT = (board[1]-1) // 2
    
    for key in keyinput:
        # 각 좌표값을 더했을 때 범위를 넘어가면 넘기기
        if start_point[0] + key_dict[key][0] > WIDTH or start_point[0] + key_dict[key][0] < -WIDTH or start_point[1] + key_dict[key][1] > HEIGHT or start_point[1] + key_dict[key][1] < -HEIGHT:
            continue
        # 그렇지 않은 경우 각 좌표값을 더해주기
        else:
            start_point[0] += key_dict[key][0]
            start_point[1] += key_dict[key][1]
                
    return start_point
        
print(solution(["up", "up", "up", "up", "up", 'right'], [7, 9]))
print(solution(["left", "left", "left", "left", "right", "right", "right", "right"], [5, 5]))