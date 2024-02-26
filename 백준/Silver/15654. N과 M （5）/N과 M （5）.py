n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
arr = [0 for _ in range(m)]
visited = [False for _ in range(n+1)]


def recur(cur):
    if cur == m:
        print(*arr)
        return 
    
    for i in range(len(numbers)):
        if visited[i]:
            continue
        
        visited[i] = True
        arr[cur] = numbers[i]
        recur(cur+1)
        visited[i] = False

recur(0)