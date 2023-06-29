import sys
input = sys.stdin.readline

n = int(input())
data = sorted([int(input()) for _ in range(n)])

num = 0

for i in range(n):
    if data[i] != (i+1):
        num += abs(data[i] - (i+1))
print(num) 