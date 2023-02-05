from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
commands = [input().strip() for _ in range(n)]
queue = deque()

for command in commands:
    command = command.split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        print(queue.popleft()) if queue else print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(0) if queue else print(1)
    elif command[0] == 'front':
        print(queue[0]) if queue else print(-1)
    elif command[0] == 'back':
        print(-1) if not queue else print(queue[-1])
