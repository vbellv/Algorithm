import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 그래프 만들기
# 인덱스 0을 제외하고 인덱스 1부터 값을 넣어주기 위해 +1
graph = [[] for _ in range(n+1)]

# 그래프로 방문한 곳 연결하기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문여부 확인
# 인덱스 0을 제외하고 인덱스 1부터 값을 넣어주기 위해 +1
visited = [False] * (n+1)

# dfs
def dfs(graph, v, visited):
    # 방문한 노드 체크하기
    visited[v] = True
    # 방문한 노드와 연결된 노드 확인하기
    # 방문하지 않았으면 dfs 함수 반복
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    # 방문한 노드 개수 구하기
    return sum(visited) - 1

print(dfs(graph, 1, visited))