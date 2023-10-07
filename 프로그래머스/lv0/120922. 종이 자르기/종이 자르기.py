def solution(M, N):
    M_cnt, N_cnt = 0, 0
    M_copy = M
    
    while True:
        if M == 1:
            break
        if M > 1:
            M -= 1
            M_cnt += 1
        
    while True:
        if N == 1:
            break
        if N > 1:
            N -= 1
            N_cnt += 1
            
    if M_cnt and N_cnt == 0:
        return 0
    elif M_cnt and N_cnt != 0:
        # print(M_cnt + M * N_cnt)
        return M_cnt + M_copy * N_cnt
    elif M_cnt == 0 or N_cnt == 0:
        return M_cnt + N_cnt
    
print(solution(1, 5))