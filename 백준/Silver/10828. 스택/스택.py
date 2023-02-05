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
        if not stack:
            print(-1) 
        else:
            pop = stack.pop()
            print(pop)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)