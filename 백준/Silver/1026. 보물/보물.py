import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
s = 0

for i in range(n):
    s += a[-(i+1)]*b[i]
print(s)