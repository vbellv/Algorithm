import sys
input = sys.stdin.readline

n = int(input())
commands = [input().strip() for _ in range(n)]
stack = []

for command in commands:
    command = command.split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        print(-1) if not stack else print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0) if stack else print(1)
    elif command[0] == 'top':
        print(stack[-1]) if stack else print(-1)