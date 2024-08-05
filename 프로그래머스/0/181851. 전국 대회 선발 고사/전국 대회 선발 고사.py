def solution(rank, attendance):
    ranks = sorted([(rank[i], i) for i in range(len(rank)) if attendance[i]], key=lambda x: x[0])
    return 10000 * ranks[0][1] + 100 * ranks[1][1] + ranks[2][1]