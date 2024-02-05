from collections import deque

n = int(input())
areas = []
max_num = 0

for _ in range(n):
    area = list(map(int, input().split()))
    areas.append(area)
    max_num = max(max_num, max(area))

def bfs(x, y, num):
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

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if areas[nx][ny] > num and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

answer = []

for num in range(max_num):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if areas[i][j] > num and visited[i][j] == 0:
                bfs(i, j, num)
                cnt += 1
    answer.append(cnt)

print(max(answer))