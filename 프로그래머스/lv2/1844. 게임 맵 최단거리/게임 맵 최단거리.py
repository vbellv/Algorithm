from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    # 상하좌우 좌표 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # bfs 알고리즘 구현
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            # 현재 위치에서 방향 이동
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 가장자리를 벗어난 경우
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue

                # 벽인 경우 무시
                if maps[nx][ny] == 0:
                    continue

                # 해당 노드를 처음 방문하는 경우메나 최단 거리 기록
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

        return maps[n-1][m-1]

    # bfs(0, 0)의 값이 1이 나오면 상대팀 진영에 도착 못했음을 의미
    if bfs(0, 0) == 1:
        return -1
    else:
        answer = bfs(0, 0)
    
    return answer