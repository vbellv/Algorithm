import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
queue = deque()

for _ in range(n):
    num_list = list(map(int, input().split()))

    if num_list[0] == 1:
        queue.appendleft(num_list[1])
    elif num_list[0] == 2:
        queue.append(num_list[1])
    elif num_list[0] == 3:
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif num_list[0] == 4:
        if not queue:
            print(-1)
        else:
            print(queue.pop())
    elif num_list[0] == 5:
        print(len(queue))
    elif num_list[0] == 6:
        if not queue:
            print(1)
        else:
            print(0)
    elif num_list[0] == 7:
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif num_list[0] == 8:
        if not queue:
            print(-1)
        else:
            print(queue[-1])