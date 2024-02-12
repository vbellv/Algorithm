n, k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]
medals = sorted(medals, key=lambda x: (x[1], x[2], x[3]), reverse=True)

ranks = []
gold, silver, bronze, cnt, real_rank = 0, 0, 0, 0, 0

for i in range(n):
    if gold == medals[i][1] and silver == medals[i][2] and bronze == medals[i][3]:
        ranks.append((real_rank, medals[i][0]))
        cnt += 1
    else:
        gold, silver, bronze = medals[i][1], medals[i][2], medals[i][3]
        real_rank += 1
        if cnt != 0:
            real_rank += cnt
        ranks.append((real_rank, medals[i][0]))
        cnt = 0

for rank, nation in ranks:
    if nation == k:
        print(rank)