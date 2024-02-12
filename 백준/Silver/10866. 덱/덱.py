import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
deque_list = deque()

for _ in range(n):
    orders = list(map(str, input().split()))
    
    if orders[0] == 'push_front':
        deque_list.appendleft(int(orders[1]))
        
    elif orders[0] == 'push_back':
        deque_list.append(int(orders[1]))
        
    elif orders[0] == 'pop_front':
        if not deque_list:
            print(-1)
        else:
            print(deque_list.popleft())
            
    elif orders[0] == 'pop_back':
        if not deque_list:
            print(-1)
        else:
            print(deque_list.pop())
            
    elif orders[0] == 'size':
        print(len(deque_list))
        
    elif orders[0] == 'empty':
        if not deque_list:
            print(1)
        else:
            print(0)
            
    elif orders[0] == 'front':
        if not deque_list:
            print(-1)
        else:
            print(deque_list[0])
    
    elif orders[0] == 'back':
        if not deque_list:
            print(-1)
        else:
            print(deque_list[-1])