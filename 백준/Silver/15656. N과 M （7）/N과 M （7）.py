n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
arr = [0 for _ in range(m)]

def recur(cur):
    if cur == m:
        print(*arr)
        return 
    
    for i in range(len(numbers)):
        arr[cur] = numbers[i]
        recur(cur+1)
        
recur(0)