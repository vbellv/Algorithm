n = int(input())
coordinate = [list(map(int, input().split())) for _ in range(n)]
for x, y in sorted(coordinate, key=lambda x: (x[1], x[0])):
    print(x, y)