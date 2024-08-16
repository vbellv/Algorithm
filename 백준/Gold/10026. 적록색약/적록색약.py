from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))


N = int(input())
graph = list(list(str(input())) for _ in range(N))


visited = [[0] * N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
    
visited = [[0] * N for _ in range(N)]
cnt2 = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)