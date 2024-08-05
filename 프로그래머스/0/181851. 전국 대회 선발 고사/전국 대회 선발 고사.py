def solution(rank, attendance):
    ranks = []
    
    for i in range(len(rank)):
        if attendance[i]:
            ranks.append((rank[i], i))
            
    ranks = sorted(ranks, key=lambda x: x[0])
    return 10000 * ranks[0][1] + 100 * ranks[1][1] + ranks[2][1]