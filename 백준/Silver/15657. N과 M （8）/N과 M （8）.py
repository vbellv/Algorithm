n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
arr = [0 for _ in range(m)]

def recur(cur, start):
    if cur == m:
        print(*arr)
        return 
    
    for i in range(start, len(numbers)):
        arr[cur] = numbers[i]
        recur(cur+1, i)
        
recur(0, 0)