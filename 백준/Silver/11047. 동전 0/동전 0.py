n, k = map(int, input().split())
coins = sorted(list(int(input()) for _ in range(n)), reverse=True)

count = 0

for coin in coins:
    if coin <= k:
        count += k // coin
        k %= coin

print(count)