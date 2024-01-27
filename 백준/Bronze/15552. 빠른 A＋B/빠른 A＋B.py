import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    A, B = map(int, input().split())
    print(A+B)