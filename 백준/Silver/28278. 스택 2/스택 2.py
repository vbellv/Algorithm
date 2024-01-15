import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    num_list = list(map(int, input().split()))
    
    if num_list[0] == 1:
        stack.append(num_list[1])
    
    elif num_list[0] == 2:
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    
    elif num_list[0] == 3:
        print(len(stack))

    elif num_list[0] == 4:
        if not stack:
            print(1)
        else:
            print(0)

    elif num_list[0] == 5:
        if not stack:
            print(-1)
        else:
            print(stack[-1])