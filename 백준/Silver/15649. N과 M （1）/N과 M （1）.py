n, m = map(int, input().split())
arr = [0 for _ in range(m)]
visited = [False for _ in range(n+1)]

def recursive(current):
    if current == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if visited[i] == True:
            continue
            
        arr[current] = i
        visited[i] = True
        recursive(current+1)
        visited[i] = False
        
recursive(0)