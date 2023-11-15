def solution(board, moves):
    stack = []
    cnt = 0
    
    for move in moves:
        for idx in range(len(board)):
            if board[idx][move-1] != 0:
                stack.append(board[idx][move-1])
                board[idx][move-1] = 0
                
                if len(stack) >= 2:
                    if stack[-2] == stack[-1]:
                        stack.pop()
                        stack.pop()
                        cnt += 2      
                break
            
    return cnt