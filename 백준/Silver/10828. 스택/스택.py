import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = list(map(str, input().split()))

    if command[0] == 'push':
        stack.append(command[1])
    if command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if command[0] == 'size':
        print(len(stack))
    if command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    if command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
