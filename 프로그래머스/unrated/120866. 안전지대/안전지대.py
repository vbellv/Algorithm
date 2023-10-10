def marking(board):
    num_list = [-1, 0, 1]
    marking_list = []
    
    n = len(board)
    m = len(board[0])
    
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if num_list[i] == 0 and num_list[j] == 0:
                continue
            else:
                marking_list.append((num_list[i], num_list[j]))
            
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                for num in marking_list:
                    nx = i + num[0]
                    ny = j + num[1]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    
                    if board[nx][ny] == 1:
                        continue
                    else:
                        board[nx][ny] = 2
            
    return board

def solution(board):
    answer = 0
    board = marking(board)
    
    for nums in board:
        answer += nums.count(0)
        
    return answer