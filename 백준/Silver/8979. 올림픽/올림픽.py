n, k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]
medals = sorted(medals, key=lambda x: (x[1], x[2], x[3]), reverse=True)

ranks = []
cnt = 1

gold, silver, bronze = medals[0][1], medals[0][2], medals[0][3]

for i in range(n):
    if gold == medals[i][1] and silver == medals[i][2] and bronze == medals[i][3]:
        ranks.append((cnt, medals[i][0]))
    else:
        gold, silver, bronze = medals[i][1], medals[i][2], medals[i][3]
        cnt += 1
        ranks.append((cnt, medals[i][0]))

for rank, nation in ranks:
    if nation == k:
        print(rank)