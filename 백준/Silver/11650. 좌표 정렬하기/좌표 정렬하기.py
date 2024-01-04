n = int(input())
numbers = sorted(list(tuple(map(int, input().split())) for _ in range(n)), key=lambda x: (x[0], x[1]))

for num in numbers:
    print(*num)