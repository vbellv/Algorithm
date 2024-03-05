from collections import deque

m, n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    x, y, a, b = map(int, input().split())
    for i in range(y, b):
        for j in range(x, a):
            graph[i][j] = 1
            
def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = deque()
    queue.append((x, y))
    
    graph[x][y] = 1
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1         
    return cnt

count = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            count.append(bfs(i, j))

print(len(count))
print(*sorted(count))