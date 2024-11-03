N = int(input())
tastes = list(map(int, input().split()))
K = int(input())

member = N // K
answer = []

for i in range(0, N, member):
    answer += sorted(tastes[i : i + member])

print(*answer)