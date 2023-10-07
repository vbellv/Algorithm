def cut_paper(num):
    num_cnt = 0
    
    while True:
        if num == 1: break
        if num > 1:
            num -= 1
            num_cnt += 1
    
    return num_cnt

def solution(M, N):
    M_cnt = cut_paper(M)
    N_cnt = cut_paper(N)    
            
    if M_cnt and N_cnt == 0:
        return 0
    elif M_cnt and N_cnt != 0:
        return M_cnt + M * N_cnt
    elif M_cnt == 0 or N_cnt == 0:
        return M_cnt + N_cnt
    
print(solution(1, 5))