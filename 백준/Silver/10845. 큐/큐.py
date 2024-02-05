import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
queue = deque()

for _ in range(n):
    orders = list(map(str, input().split()))
    
    if orders[0] == 'push':
        queue.append(int(orders[1]))
    elif orders[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif orders[0] == 'size':
        print(len(queue))
    elif orders[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif orders[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif orders[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])