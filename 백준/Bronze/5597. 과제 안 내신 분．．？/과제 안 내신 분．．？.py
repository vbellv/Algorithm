import sys
input = sys.stdin.readline

students = sorted([int(input()) for _ in range(28)])

for i in range(1, 31):
    if i not in students:
        print(i)