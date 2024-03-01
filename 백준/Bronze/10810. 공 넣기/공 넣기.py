n, m = map(int, input().split())
numbers = [0] * (n+1)

for _ in range(m):
    i, j, k = map(int, input().split())
    for num in range(i, j+1):
        numbers[num] = k
        
print(*numbers[1:])