from collections import deque

def bfs(cases, x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x, y))

    cases[x][y] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if cases[nx][ny] == 1:
                cases[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    
    return cnt


T = int(input())

for _ in range(T):
    test_cases = list(map(int, input().split()))
    m, n, k = test_cases[0], test_cases[1], test_cases[2]

    cases = [[0 for _ in range(n)] for _ in range(m)]

    for _ in range(k):
        X, Y = map(int, input().split())
        cases[X][Y] = 1

    count = []

    for i in range(len(cases)):
        for j in range(len(cases[i])):
            if cases[i][j] == 1:
                count.append(bfs(cases, i, j))

    print(len(count))