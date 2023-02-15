from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
num = deque(i for i in range(1, n+1))

while len(num) > 1:
    num.popleft()
    card = num.popleft()
    num.append(card)
print(*num)