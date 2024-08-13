n, m = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0

for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            if answer < cards[i] + cards[j] + cards[k] <= m:
                answer = cards[i] + cards[j] + cards[k]
            if cards[i] + cards[j] + cards[k] == m:
                answer = m
                break

print(answer)