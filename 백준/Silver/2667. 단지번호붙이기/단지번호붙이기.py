from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
count = []

def bfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))
    
    graph[x][y] = 0
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
                
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count.append(bfs(graph, i, j))
            
print(len(count))

for i in sorted(count):
    print(i)