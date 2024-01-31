import sys
input = sys.stdin.readline

n = int(input())
sticks = [int(input()) for _ in range(n)]

stack = []

for stick in sticks:
    while stack and stack[-1] <= stick:
        stack.pop()
    stack.append(stick)

print(len(stack))