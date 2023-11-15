from collections import deque

def new_board(board):
    total_board = []
    
    for i in range(len(board)):
        temp_list = []
        for j in range(len(board)):
            if board[j][i] != 0:
                temp_list.append(board[j][i])
        total_board.append(temp_list)
    
    return total_board

def solution(board, moves):
    moves = deque(moves)
    board = new_board(board)
    answer = []
    cnt = 0
    
    while len(moves) > 0:
        move = moves.popleft() - 1
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                try:
                    if move == i:
                        board[i] = deque(board[i])
                        print(board[i].popleft())
                        pop_num = board[i].popleft()
                        answer.append(pop_num)
                        cnt += 1
                except:
                    pass
                
                try:
                    check_num = answer.pop()
                    if check_num == pop_num:
                        pass
                    else:
                        answer.append(check_num)
                        answer.append(pop_num) 
                except:
                    pass
    
    return cnt - len(answer)