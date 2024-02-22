import sys
input = sys.stdin.readline

n = int(input())
stack = []
MAX = 0
answer = []

for _ in range(n):
    number = int(input())
    
    for i in range(MAX+1, number+1):
        stack.append(i)
        answer.append('+')
    MAX = i 

    if stack[-1] == number:
        stack.pop()
        answer.append('-')
        
if not stack:
    for i in answer:
        print(i)
else:
    print('NO')