import sys
input = sys.stdin.readline
n = int(input())
test = list(map(int, input().split()))

max_test = max(test)
changes = 0

for i in range(n):
    changes += (test[i]/max_test)*100

change = changes / n
print(change)