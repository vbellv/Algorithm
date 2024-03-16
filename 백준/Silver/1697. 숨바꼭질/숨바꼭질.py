from collections import deque

n, k = map(int, input().split())
MAX = 100000
distance = [0] * (MAX+1)

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()

        if x == k:
            print(distance[x])
            break

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not distance[nx]:
                distance[nx] = distance[x] + 1
                queue.append(nx)

bfs()