import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    data = input().rstrip()
    check = list(data)
    stack = []

    for i in check:
        if i == '(':
            stack.append(check)
        elif i == ')':
            if not stack:
                print('NO')
                break
            else:
                stack.pop()
    else:
        if not stack:
            print('YES')
        else:
            print('NO')