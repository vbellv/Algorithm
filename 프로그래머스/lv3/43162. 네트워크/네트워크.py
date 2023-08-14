from collections import defaultdict, deque

def network_connect(n, computers):
    node_list = defaultdict(list)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                if computers[i][j] == 1:
                    node_list[i] += [j]
    
    return node_list


def solution(n, computers):
    node_list = network_connect(n, computers)
    visited = [False] * n
    
    cnt = 0
    
    for i in range(n):
        if not visited[i]:
            cnt += 1
            
            queue = deque([i])
            visited[i] = True

            while queue:
                v = queue.popleft()

                for i in node_list[v]:
                    if not visited[i]:
                        queue.append(i)
                        visited[i] = True

    return cnt